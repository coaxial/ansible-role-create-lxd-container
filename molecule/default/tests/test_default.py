import os

import testinfra.utils.ansible_runner

import yaml
from distutils.util import strtobool

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_example(host):
    file = host.file('/etc/hosts')

    assert file.exists
    assert file.user == 'root'
    assert file.group == 'root'


def test_container_creation(host):
    c = yaml.load(host.check_output('lxc config show test-container'))

    assert strtobool(c['config']['boot.autostart'])
    assert c['config']['limits.cpu'] == ""
    assert c['config']['limits.cpu.allowance'] == '100%'
    assert c['config']['limits.memory'] == ""
    assert not strtobool(c['config']['security.nesting'])
    assert not strtobool(c['config']['security.privileged'])
    assert c['profiles'] == ['default']
    assert c['devices']['eth0']['parent'] == 'lxdbr0'
    assert c['devices']['eth0']['ipv4.address'] == 'auto'
    assert c['devices']['eth0']['ipv6.address'] == 'auto'
