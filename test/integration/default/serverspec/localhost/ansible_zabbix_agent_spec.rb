require 'serverspec'
require 'spec_helper'

describe 'Zabbix Agent Packages' do
    describe package('zabbix-agent') do
        it { should be_installed }
    end
end

describe 'Zabbix Agent Services' do
    describe service('zabbix-agent') do
        it { should be_enabled }
        it { should be_running }
    end

    describe port(10050) do
        it { should be_listening }
    end
end

describe 'Zabbix Agent Configuration' do
    describe file('/etc/zabbix/zabbix_agentd.conf') do
        it { should be_file}
        it { should be_owned_by 'zabbix'}
        it { should be_grouped_into 'zabbix'}

        it { should contain "ListenPort=10050" }
        it { should contain "Server=192.168.3.33" }
        it { should contain "ServerActive=192.168.3.33" }
    end
end
