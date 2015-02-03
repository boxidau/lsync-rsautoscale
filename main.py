#!/usr/bin/env python
# -*- coding: utf-8 -*-

# vim: tabstop=4 shiftwidth=4 softtabstop=4

import pyrax
import argparse
import os
import jinja2

def generate_lsync_config(addresses):
  env = jinja2.Environment(autoescape=True, 
                    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))

  template = env.get_template('lsyncd.conf')

  print template.render(server_list=addresses, source_dir='/var/www', dest_dir='/var/www')
     
def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('--as-group', required=True,
                      help='The autoscale group config ID')

  args = vars(parser.parse_args())

  pyrax.set_setting("identity_type", "rackspace")

  # Using credentials file
  try:
    pyrax.set_credential_file("./.cloud_credentials")
  except Exception, e:
    sys.stderr.write("Failed to authenticate: %s" % str(e))

  au = pyrax.autoscale
  cs = pyrax.cloudservers

  as_group = au.get(args['as_group']);

  snet_ips = []

  for s_id in as_group.get_state()['active']:
    server = cs.servers.get(s_id)
    snet_ips.append(server.networks['private'][0])

  generate_lsync_config(snet_ips)

if __name__ == '__main__':
  main()
