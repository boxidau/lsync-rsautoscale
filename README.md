lsyncd-autoscale
================

Generate lsyncd config for autoscale group automatically

Currently lsync config files need to be generated on the master and need to contain all slave servers.
If slave servers come and go (such as in an autoscale environment) these need to be managed automatically in the lsyncd config file.

This project aims to read autoscale group members from API calls and generate an lsyncd configuration file from this information.
