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
`cc__containers` | unset | A list of maps conforming to the format detailed below | The list describing containers to create

`cc__containers` format:
Key | Default | Possible values | Description
---|---|---|---
`name` (required) | unset | Any valid hostname (container names have to be legal hostnames) | The container name
`ipv4` | `auto` | Any valid value for `ipv4.address` (cf. https://github.com/lxc/lxd/blob/master/doc/networks.md) | The IPv4 this container will assume
`ipv6` | `auto` | Any valid value for `ipv6.address` (cf. https://github.com/lxc/lxd/blob/master/doc/networks.md) | The IPv6 this container will assume
`source_server` | `https://cloud-images.ubuntu.com/releases` | Any valid image server (the `images:` server is at https://images.linuxcontainers.org) | Where will the image be downloaded from
`source_protocol` | `simplestreams` | Any valid protocol (`lxd` or `simplestreams`)
`source_type` | `image` | One of `image`, `migration`, `copy`, or `none` | Describe the source type, cf. https://github.com/lxc/lxd/blob/master/doc/rest-api.md#post-1
`source_alias` | `ubuntu:18.04` | Any valid alias | cf. `lxc image list {images:,ubuntu:,mysource:}` and https://images.linuxcontainers.org/
`autostart` | `true` | `true` or `false` | Sets the `boot.autostart` property for the container (cf. https://github.com/lxc/lxd/blob/master/doc/containers.md)
`limits_cpu` | `all` | Integers | Limit container's CPU/core usage (cf. https://stgraber.org/2016/03/26/lxd-2-0-resource-control-412/ and https://github.com/lxc/lxd/blob/master/doc/containers.md#cpu-limits)
`limits_cpu_allowance` | `100%` | String (including `%` sign) | Limit container's CPU consumption (cf. https://stgraber.org/2016/03/26/lxd-2-0-resource-control-412 and https://github.com/lxc/lxd/blob/master/doc/containers.md#cpu-limits/)
`limits_memory` | `all` | Percentage or absolute value in kB, MB, GB, GB, and EB | Limit container's memory footpring (cf. https://stgraber.org/2016/03/26/lxd-2-0-resource-control-412/ and https://github.com/lxc/lxd/blob/master/doc/containers.md)
`security_nesting` | `false` | `true` or `false` | Enables nesting (so LXD or Docker can run within a container), cf. https://stgraber.org/2016/04/14/lxd-2-0-lxd-in-lxd-812/ and https://stgraber.org/2016/04/13/lxd-2-0-docker-in-lxd-712/
`security_privileged` | `false` | `true` or `false` | Whether the container is privileged, cf. https://linuxcontainers.org/lxc/manpages//man5/lxc.container.conf.5.html -- search for "privileged"
`profiles` | `["default"]` | List of existing profiles in an array | Profiles attached to the container, cf. https://github.com/lxc/lxd/blob/master/doc/rest-api.md#post-1


Example Playbook
----------------

```yaml
- hosts: all
  vars:
    cc__containers:
      - name: mycontainer
  roles:
    - create-lxd-container
```

License
-------

MIT

Author Information
------------------

Coaxial ([64b.it](https://64b.it))
