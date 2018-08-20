import os

import testinfra.utils.ansible_runner

import yaml
from distutils.util import strtobool

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_container_creation_defaults(host):
    c = yaml.load(host.check_output('lxc config show test-container-1'))

    assert strtobool(c['config']['boot.autostart'])
    assert c['config']['limits.cpu'] == ""
    assert c['config']['limits.cpu.allowance'] == '100%'
    assert c['config']['limits.memory'] == ""
    assert not strtobool(c['config']['security.nesting'])
    assert not strtobool(c['config']['security.privileged'])
    assert c['profiles'] == ['default']
    assert c['config']['image.version'] == '18.04'
    assert c['profiles'] == ['default']


def test_container_creation_override_defaults(host):
    c = yaml.load(host.check_output('lxc config show test-container-2'))

    assert not strtobool(c['config']['boot.autostart'])
    assert c['config']['limits.cpu'] == "1"
    assert c['config']['limits.cpu.allowance'] == '90%'
    assert c['config']['limits.memory'] == "512MB"
    assert strtobool(c['config']['security.nesting'])
    assert strtobool(c['config']['security.privileged'])
    assert c['devices']['eth1']['parent'] == 'lxdbr0'
    assert c['devices']['eth1']['nictype'] == 'macvlan'
    assert c['devices']['eth1']['ipv4.address'] == '10.100.12.10'
    assert c['config']['image.version'] == '16.04'
    assert c['profiles'] == ['default', 'testprofile']
