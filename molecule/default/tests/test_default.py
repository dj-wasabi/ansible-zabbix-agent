import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_zabbixagent_running_and_enabled(Service, SystemInfo):
    zabbixagent = Service("zabbix-agent")
    # Find out why this is not working for linuxmint and opensuse
    if SystemInfo.distribution not in ['linuxmint', 'opensuse', 'ubuntu']:
        assert zabbixagent.is_running
        assert zabbixagent.is_enabled


def test_zabbix_agent_dot_conf(File, SystemInfo):
    if SystemInfo.distribution in ['opensuse']:
        passwd = File("/etc/zabbix/zabbix-agentd.conf")
    else:
        passwd = File("/etc/zabbix/zabbix_agentd.conf")
    assert passwd.user == "root"
    assert passwd.group == "root"
    assert passwd.mode == 0o644

    assert passwd.contains("Server=192.168.3.33")
    assert passwd.contains("ServerActive=192.168.3.33")
    assert passwd.contains("ListenIP=0.0.0.0")
    assert passwd.contains("DebugLevel=3")
    assert passwd.contains("TLSAccept=psk")
    assert passwd.contains("TLSPSKIdentity=my_Identity")
    assert passwd.contains("TLSPSKFile=/data/certs/zabbix.psk")


def test_zabbix_agent_psk(File):
    psk_file = File("/data/certs/zabbix.psk")
    assert psk_file.user == "zabbix"
    assert psk_file.group == "zabbix"
    assert psk_file.mode == 0o400
    assert psk_file.contains("97defd6bd126d5ba7fa5f296595f82eac905d5eda270207a580ab7c0cb9e8eab")


def test_zabbix_include_dir(File):
    zabbixagent = File("/etc/zabbix/zabbix_agentd.d")
    assert zabbixagent.is_directory
    assert zabbixagent.user == "root"
    assert zabbixagent.group == "root"


def test_socker(Socket, SystemInfo):
    # Find out why this is not working for linuxmint and opensus
    if SystemInfo.distribution not in ['linuxmint', 'opensuse']:
        assert Socket("tcp://0.0.0.0:10050").is_listening


def test_zabbix_package(Package, SystemInfo):
    zabbixagent = Package('zabbix-agent')
    assert zabbixagent.is_installed

    if SystemInfo.distribution == 'debian':
        assert zabbixagent.version.startswith("1:3.4")
    if SystemInfo.distribution == 'centos':
        assert zabbixagent.version.startswith("3.4")
