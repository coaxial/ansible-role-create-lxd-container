create-lxd-container
=========
  [![Build Status](https://travis-ci.org/coaxial/ansible-role-create-lxd-container.svg?branch=master)](https://travis-ci.org/coaxial/ansible-role-create-lxd-container)

Create LXD containers on target hosts

Requirements
------------

Assumes a host with a functional LXD setup (i.e. initialized, and with a storage pool.) If required, see my [LXD role](https://github.com/coaxial/ansible-role-lxd).


Role Variables
--------------

Name | Default | Possible values | Description
---|---|---|---
`cc__containers` | unset | A list of maps conforming to the format detailed below | The list describing containers to create

`cc__containers` format:

Key | Default | Possible values | Description
---|---|---|---
`autostart` | `"true"` | `"true"` or `"false"` **Note the double quotes, this needs to be a string and not a boolean** | Sets the `boot.autostart` property for the container (cf. https://github.com/lxc/lxd/blob/master/doc/containers.md)
`devices` | `{}` | Any dict of devices | Configures the devices on the container (cf. https://github.com/lxc/lxd/blob/master/doc/containers.md#devices-configuration)
`limits_cpu_allowance` | `100%` | Limit container's CPU time share (cf. https://stgraber.org/2016/03/26/lxd-2-0-resource-control-412/ and https://github.com/lxc/lxd/blob/master/doc/containers.md#cpu-limits)
`limits_cpu` | `""` i.e. all | Integers | Limit container's CPU/core usage (cf. https://stgraber.org/2016/03/26/lxd-2-0-resource-control-412/ and https://github.com/lxc/lxd/blob/master/doc/containers.md#cpu-limits)
`limits_cpu_allowance` | `100%` | String (including `%` sign) | Limit container's CPU consumption (cf. https://stgraber.org/2016/03/26/lxd-2-0-resource-control-412 and https://github.com/lxc/lxd/blob/master/doc/containers.md#cpu-limits/)
`limits_memory` | `""` i.e. all | Percentage or absolute value in kB, MB, GB, GB, and EB | Limit container's memory footpring (cf. https://stgraber.org/2016/03/26/lxd-2-0-resource-control-412/ and https://github.com/lxc/lxd/blob/master/doc/containers.md)
`name` (required) | unset | Any valid hostname (container names have to be legal hostnames) | The container name
`profiles` | `["default"]` | List of existing profiles in an array | Profiles attached to the container, cf. https://github.com/lxc/lxd/blob/master/doc/rest-api.md#post-1
`security_nesting` | `"false"` | `"true"` or `"false"` **Note the double quotes, this needs to be a string and not a boolean** | Enables nesting (so LXD or Docker can run within a container), cf. https://stgraber.org/2016/04/14/lxd-2-0-lxd-in-lxd-812/ and https://stgraber.org/2016/04/13/lxd-2-0-docker-in-lxd-712/
`security_privileged` | `false` | `"true"` or "`false"` **Note the double quotes, this needs to be a string and not a boolean** | Whether the container is privileged, cf. https://linuxcontainers.org/lxc/manpages//man5/lxc.container.conf.5.html -- search for "privileged"
`source_alias` | `ubuntu:18.04` | Any valid alias | cf. `lxc image list {images:,ubuntu:,mysource:}` and https://images.linuxcontainers.org/
`source_protocol` | `simplestreams` | Any valid protocol (`lxd` or `simplestreams`)
`source_server` | `https://cloud-images.ubuntu.com/releases` | Any valid image server (the `images:` server is at https://images.linuxcontainers.org) | Where will the image be downloaded from
`source_type` | `image` | One of `image`, `migration`, `copy`, or `none` | Describe the source type, cf. https://github.com/lxc/lxd/blob/master/doc/rest-api.md#post-1
`state` | `started` | `started`, `stopped`, `restarted`, `absent`, `frozen` | cf. https://docs.ansible.com/ansible/2.5/modules/lxd_container_module.html?highlight=state
`wait_for_ipv4_addresses` | `"true"` | `"true"` or `"false"` **Note the double quotes, this needs to be a string and not a boolean** | Whether to return from the task before the container has acquired an IPv4 or not


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
            ...
      - name: mycontainer-customdevices
        config:
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
