dj-wasabi.zabbix-agent
=========

This is an role for installing and maintaining the zabbix-agent.

This is one of the 'dj-wasabi' roles which configures your whole zabbix environment. See an list for the complete list:

 * zabbix-server (https://galaxy.ansible.com/list#/roles/2070)
 * zabbix-proxy (https://galaxy.ansible.com/list#/roles/2073)
 * zabbix-javagateway (https://galaxy.ansible.com/list#/roles/2076)
 * zabbix-agent (https://galaxy.ansible.com/list#/roles/2079)

Requirements
------------

This role will work on:
 * Red Hat
 * Debian
 * Ubuntu

So, you'll need one of those operating systems.. :-)

Role Variables
--------------

There are some variables in de default/main.yml which can (Or needs to) be changed/overriden:
* `agent_server`: The ipaddress for the zabbix-server or zabbix-proxy.
* `agent_serveractive`: The ipaddress for the zabbix-server or zabbix-proxy for active checks.
* `zabbix_version`: This is the version of zabbix. Default it is 2.4, but can be overriden to 2.2 or 2.0.

Dependencies
------------


Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: ALL
      sudo: yes
      roles:
         - { role: dj-wasabi.agent, agent_server: 192.168.33.30, agent_serveractive: 192.168.33.30}

Extra Information
----------------

You can install so-called userparameter files by adding the following into your roles:
```
- name: Installing sample file
  copy: src=sample.conf
        dest="{{ agent_include }}/mysql.conf"
        owner=zabbix
        group=zabbix
        mode=0755
  notify: zabbix-agent restarted
```
Example of the "sample.conf" file:
```
UserParameter=mysql.ping_to,mysqladmin -uroot ping | grep -c alive
```

You can extend your zabbix configuration by adding items yourself that do specific checks which aren't in the zabbix core itself. You can change offcourse the name of the file to whatever you want (Same for the UserParameter line(s) ;-) )

License
-------

GPLv3

Author Information
------------------

This is my first attempt to create an ansible role, so please send suggestion or pull requests to make this role better. 

Github: https://github.com/dj-wasabi/ansible-zabbix-agent

mail: ikben [ at ] werner-dijkerman . nl
