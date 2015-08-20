require 'serverspec'
require 'spec_helper'

describe 'Zabbix Agent Packages' do
    describe package('zabbix-agent') do
        it { should be_installed }
    end
end

describe 'Zabbix Agent Configuration' do
    describe file('/etc/zabbix/zabbix_agent.conf') do
        it { should be_file}
        it { should be_owned_by 'zabbix'}
        it { should be_grouped_into 'zabbix'}
    end
end
