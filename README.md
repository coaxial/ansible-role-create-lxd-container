create-lxd-container
=========
  [![Build Status](https://travis-ci.org/coaxial/ansible-role-create-lxd-container.svg?branch=master)](https://travis-ci.org/coaxial/ansible-role-create-lxd-container)

Create LXD containers on target hosts

Requirements
------------

Assumes a host with a functional LXD setup. If required, see my [LXD role](https://github.com/coaxial/ansible-role-lxd).


Role Variables
--------------

Name | Default | Possible values | Description
---|---|---|---
`example_variable` | `true` | `true` or `false` | This is an example to populate the table.


Example Playbook
----------------

```yaml
- hosts: all
  roles:
    - create-lxd-container
```

License
-------

MIT

Author Information
------------------

Coaxial ([64b.it](https://64b.it))