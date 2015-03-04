lsyncd-autoscale
================

Generate lsyncd config for autoscale group automatically

Currently lsync config files need to be generated on the master and need to contain all slave servers.
If slave servers come and go (such as in an autoscale environment) these need to be managed automatically in the lsyncd config file.

This project aims to read autoscale group members from API calls and generate an lsyncd configuration file from this information.


Setup
=====

Create a file called .cloud_credentials with contents like the following

```
[rackspace_cloud]
username = yourusernamehere
api_key = yourapikeyhere
```

By default this script will have source and destination directories set to /var/www
modify main.py to change this

TODO: config files ;)

pyrax throws some warning output to stderr so to execute this script use the following command line


```
python main.py --as-group=AUTOSCALE_GROUP_ID 2>/dev/null > lsyncd.conf
```

This can be added to a cronjob
```
* * * * * root python /root/lsync-rsautoscale/main.py --as-group=<as-group> --region=HKG 2>/var/log/lsync-autoscale.error_log > /etc/lsyncd.conf; service lsyncd reload
```
