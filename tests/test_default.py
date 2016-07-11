def test_hosts_file(File):
    hosts = File('/etc/hosts')

    assert hosts.user == 'root'
    assert hosts.group == 'root'


def test_zabbix_package(Package):
    zabbixagent = Package('zabbix-agent')
    assert zabbixagent.is_installed
    assert zabbixagent.version.startswith("1:3.0")


def test_zabbixagent_running_and_enabled(Service):
    zabbixagent = Service("zabbix-agent")
    # assert zabbixagent.is_running
    assert zabbixagent.is_enabled


def test_zabbix_agent_dot_conf(File):
    passwd = File("/etc/zabbix/zabbix_agentd.conf")
    assert passwd.user == "root"
    assert passwd.group == "root"
    assert passwd.mode == 0o644

    assert passwd.contains("Server=192.168.3.33")
    assert passwd.contains("ServerActive=192.168.3.33")
    assert passwd.contains("ListenIP=0.0.0.0")


def test_zabbix_include_dir(File):
    zabbixagent = File("/etc/zabbix/zabbix_agentd.d")
    assert zabbixagent.is_directory
    assert zabbixagent.user == "root"
    assert zabbixagent.group == "root"
