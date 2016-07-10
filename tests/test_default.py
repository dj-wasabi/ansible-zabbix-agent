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
