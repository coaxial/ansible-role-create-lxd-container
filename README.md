create-lxd-container
=========
  [![Build Status](https://travis-ci.org/coaxial/ansible-role-create-lxd-container.svg?branch=master)](https://travis-ci.org/coaxial/ansible-role-create-lxd-container)

Create LXD containers on target hosts

Requirements
------------

Assumes a host with a functional LXD setup (i.e. initialized, and with a storage pool.) If required, see my [LXD role](https://github.com/coaxial/ansible-role-lxd).


Role Variables
--------------

Name | Default | Description
---|---|---
`cc__containers` | unset | A list describing the containers to create, see below for format.

### `cc__containers` format

Key | Default | Possible values | Description
---|---|---|---
`name` (required) | unset | Any valid hostname (container names must be legal hostnames) | The container name
`config` | see below | Any valid `config` dict (see `lxd_container` documentation) | Container's configuration
`source` | see below | Any valid `source` dict (see `lxd_container` documentation) | Where to get the image from
`devices` | `{}` | Any valid `devices` dict (see `lxd_container` documentation) | Container's devices
`profiles` | `["default"]` | List of (existing) profiles | A list of profiles to apply to the container
`state` | `started` | `started`, `stopped`, `restarted`, `absent`, `frozen` | Initial container's state, cf. [lxd_container](https://docs.ansible.com/ansible/2.5/modules/lxd_container_module.html?highlight=state)
`wait_for_ipv4_addresses` | `"true"` | `"true"` or `"false"` as strings | Wait for the container to get an IPv4, see `lxd_container` documentation

#### Default `config:` values (unless overridden):

Key | Default
---|---
`boot.autostart` | `"true"` (string)
`limits.cpu` | `""`
`limits.cpu.allowance` | `"100%"`
`limits.memory` | `""`
`security.nesting` | `"false"` (string)
`security.privileged` | `"false"` (string)

#### Default `source:` values (unless overridden):

Key | Default
---|---
`alias` | `"16.04"` (string)
`protocol` | `simplestreams`
`server` | `https://cloud-images.ubuntu.com/releases`
`type` | `image`


Example Playbook
----------------

```yaml
- hosts: all
  vars:
    cc__containers:
      - name: mycontainer
        config:
          boot.autostart: false
          user.network-config: |
            # cf. https://github.com/lxc/lxd/blob/master/doc/cloud-init.md
            version: 1
            # ...
      - name: mycontainer-customdevices
        devices:
          eth0:
            name: eth0
            nictype: macvlan
            parent: lxdbr0
            type: nic
  tasks:
    - name: Configure containers
      include_role:
        name: ansible-role-create-lxd-container
      with_items: "{{ cc__containers }}"
```

License
-------

MIT

Author Information
------------------

Coaxial ([64b.it](https://64b.it))
