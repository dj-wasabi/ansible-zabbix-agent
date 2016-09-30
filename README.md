Table of Contents

1. [Overview](#overview)
   * [Upgrade](#upgrade)
2. [Requirements for this role](#requirements)
   * [List of Operating systems](#zabbix-versions)
   * [Zabbix API Usage](#zabbix-api)
3. [Installing this role](#installation)
4. [Overview of variables which can be used](#role-variables)
   * [Main variables](#main-variables)
   * [Zabbix 3.x](#zabbix-30)
   * [Zabbix API Variables](#zabbix-api-variables)
4. [Dependencies](#dependencies)
5. [Example of using this role](#example-playbook)
   * [ Vars in role configuration](#vars-in-role-configuration)
   * [Combination of group_vars and playbook](#combination-of-group_vars-and-playbook)
6. [Molecule](#molecule)
7. [Extra information](#extra-information)
8. [License](#license)
9. [Author Information](#author-information)

#Overview

Build Status:

[![Build Status](https://travis-ci.org/dj-wasabi/ansible-zabbix-agent.svg?branch=master)](https://travis-ci.org/dj-wasabi/ansible-zabbix-agent)

This is an role for installing and maintaining the zabbix-agent.

This is one of the 'dj-wasabi' roles which configures your whole zabbix environment. See an list for the complete list:

 * zabbix-server (https://galaxy.ansible.com/dj-wasabi/zabbix-server/)
 * zabbix-proxy (https://galaxy.ansible.com/dj-wasabi/zabbix-proxy/)
 * zabbix-javagateway (https://galaxy.ansible.com/dj-wasabi/zabbix-javagateway/)
 * zabbix-agent (https://galaxy.ansible.com/dj-wasabi/zabbix-agent/)

## Upgrade

### 0.8.0

As of version 0.8.0, the property `zabbix_api_use` isn't available anymore. It is replaced by the properties `zabbix_api_create_hostgroup` and `zabbix_api_create_hosts`

#Requirements
##Operating systems
This role will work on the following operating systems:

 * Red Hat
 * Debian
 * Ubuntu
 * opensuse

So, you'll need one of those operating systems.. :-)
Please sent Pull Requests or suggestions when you want to use this role for other Operating systems.

##Zabbix Versions

See the following list of supported Operating systems with the Zabbix releases:

Zabbix 3.2:

  * CentOS 7.x
  * Amazon 7.x
  * RedHat 7.x
  * OracleLinux 7.x
  * Scientific Linux 7.x
  * Ubuntu 14.04, 16.04
  * Debian 7, 8

Zabbix 3.0:

  * CentOS 5.x, 6.x, 7.x
  * Amazon 5.x, 6.x, 7.x
  * RedHat 5.x, 6.x, 7.x
  * OracleLinux 5.x, 6.x, 7.x
  * Scientific Linux 5.x, 6.x, 7.x
  * Ubuntu 14.04
  * Debian 7, 8

Zabbix 2.4:

  * CentOS 6.x, 7.x
  * Amazon 6.x, 7.x
  * RedHat 6.x, 7.x
  * OracleLinux 6.x, 7.x
  * Scientific Linux 6.x, 7.x
  * Ubuntu 12.04 14.04
  * Debian 7

Zabbix 2.2:

  * CentOS 5.x, 6.x
  * RedHat 5.x, 6.x
  * OracleLinux 5.x, 6.x
  * Scientific Linux 5.x, 6.x
  * Ubuntu 12.04
  * Debian 7
  * xenserver 6


## Zabbix API
When you want to automatically create the hosts in the webinterface, you'll need on your own machine the zabbix-api package. 

You can install this locally with the following command: `pip install zabbix-api`.

This ansible role uses the modules from "Cove" found in this pull request: https://github.com/ansible/ansible-modules-extras/pull/44. So all credits goes to this guy!

#Installation

Installing this role is very simple: `ansible-galaxy install dj-wasabi.zabbix-agent`

#Role Variables

## Main variables
There are some variables in de default/main.yml which can (Or needs to) be changed/overriden:

* `agent_server`: The ipaddress for the zabbix-server or zabbix-proxy.

* `agent_serveractive`: The ipaddress for the zabbix-server or zabbix-proxy for active checks.

* `zabbix_version`: This is the version of zabbix. Default it is 3.2, but can be overriden to 3.0, 2.4, 2.2 or 2.0.

* `zabbix_repo`: Default: _zabbix_
  * _epel_ (default) install agent from EPEL repo
  * _zabbix_ install agent from Zabbix repo
  * _other_ install agent from pre-existing or other repo

* `agent_listeninterface`: Interface zabbix-agent listens on. Leave blank for all.

* `zabbix_agent_package_state`: If Zabbix-agent needs to be present or latest.

* `agent_interfaces`: A list that configured the interfaces you can use when configuring via API.

## Zabbix 3.0

These variables are specific for Zabbix 3.0/

* `agent_tlsconnect`: How the agent should connect to server or proxy. Used for active checks.

    Possible values:
    
    * unencrypted
    * psk
    * cert

* `agent_tlsaccept`: What incoming connections to accept.

    Possible values:
    
    * unencrypted
    * psk
    * cert

* `agent_tlscafile`: Full pathname of a file containing the top-level CA(s) certificates for peer certificate verification.

* `agent_tlscrlfile`: Full pathname of a file containing revoked certificates.

* `agent_tlsservercertissuer`: Allowed server certificate issuer.

* `agent_tlsservercertsubject`: Allowed server certificate subject.

* `agent_tlscertfile`: Full pathname of a file containing the agent certificate or certificate chain.

* `agent_tlskeyfile`: Full pathname of a file containing the agent private key.

* `agent_tlspskidentity`: Unique, case sensitive string used to identify the pre-shared key.

* `agent_tlspskfile`: Full pathname of a file containing the pre-shared key.

## Zabbix API variables
These variables needs to be changed/overriden when you want to make use of the zabbix-api for automatically creating and or updating hosts.

* `zabbix_url`: The url on which the Zabbix webpage is available. Example: http://zabbix.example.com

* `zabbix_api_create_hosts`: When you want to enable the Zabbix API to create/delete the host. This has to be set to `True` if you want to make use of `zabbix_create_host`. Default: `False`

* `zabbix_api_create_hostgroup`: When you want to enable the Zabbix API to create/delete the hostgroups. This has to be set to `True` if you want to make use of `zabbix_create_hostgroup`.Default: `False`

* `zabbix_api_user`: Username of user which has API access.

* `zabbix_api_pass`: Password for the user which has API access.

* `zabbix_create_hostgroup`: present (Default) if the hostgroup needs to be created or absent if you want to delete it. This only works when `zabbix_api_create_hostgroup` is set to `True`.

* `zabbix_host_status`: enabled (Default) when host in monitored, disabled when host is disabled for monitoring.

* `zabbix_create_host`: present (Default) if the host needs to be created or absent is you want to delete it. This only works when `zabbix_api_create_hosts` is set to `True`.

* `zabbix_useuip`: 1 if connection to zabbix-agent is made via ip, 0 for fqdn.

* `zabbix_host_groups`: An list of hostgroups which this host belongs to.

* `zabbix_link_templates`: An list of templates which needs to be link to this host. The templates should exist.

* `zabbix_macros`: An list with macro_key and macro_value for creating hostmacro's.


#Dependencies

There are no dependencies on other roles.

#Example Playbook

## agent_interfaces

This will configure the Zabbix Agent interface on the host. 
```
agent_interfaces:
  - type: 1
    main: 1
    useip: "{{ zabbix_useuip }}"
    ip: "{{ agent_ip }}"
    dns: "{{ ansible_fqdn }}"
    port: "{{ agent_listenport }}"
```

## Other interfaces

You can also configure the `agent_interfaces` to add/configure snmp, jmx and ipmi interfaces.

You'll have to use one of the following type numbers when configuring it:

| Type Interface  |  Nr   |
|-----------------|-------|
| Zabbix Agent  | 1  |
| snmp | 2  |
| jmx  | 3  |
| ipmi | 4  |

Configuring a snmp interface will look like this:

```
agent_interfaces:
  - type: 2
    main: 1
    useip: "{{ zabbix_useuip }}"
    ip: "{{ agent_ip }}"
    dns: "{{ ansible_fqdn }}"
    port: "{{ agent_listenport }}"
```

##Vars in role configuration
Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: all
      roles:
         - role: dj-wasabi.zabbix-agent
           agent_server: 192.168.33.30
           agent_serveractive: 192.168.33.30
           zabbix_url: http://zabbix.example.com
           zabbix_api_use: true
           zabbix_api_user: Admin
           zabbix_api_pass: zabbix
           zabbix_create_host: present
           zabbix_host_groups:
             - Linux Servers
           zabbix_link_templates:
             - Template OS Linux
             - Apache APP Template
           zabbix_macros:
             - macro_key: apache_type
               macro_value: reverse_proxy

##Combination of group_vars and playbook 
You can also use the group_vars or the host_vars files for setting the variables needed for this role. File you should change: `group_vars/all` or `host_vars/<zabbix_server>` (Where <zabbix_server> is the hostname of the machine running Zabbix Server)

		agent_server: 192.168.33.30
        agent_serveractive: 192.168.33.30
        zabbix_url: http://zabbix.example.com
        zabbix_api_use: true
        zabbix_api_user: Admin
        zabbix_api_pass: zabbix
        zabbix_create_host: present
        zabbix_host_groups:
          - Linux Servers
        zabbix_link_templates:
          - Template OS Linux
          - Apache APP Template
        zabbix_macros:
          - macro_key: apache_type
            macro_value: reverse_proxy

and in the playbook only specifying:

    - hosts: all
      roles:
         - role: dj-wasabi.zabbix-agent

#Molecule

This roles is configured to be tested with Molecule. You can find on this page some more information regarding Molecule: https://werner-dijkerman.nl/2016/07/10/testing-ansible-roles-with-molecule-testinfra-and-docker/
Molecule will boot 3 docker containers, containing the following OS:

* Debian 8
* CentOS 7
* Ubuntu 14.04

On these containers, this Ansible role is executed. After this, a idempotence check is run.
When all is executed correctly, TestInfra is executed to validate the installation/configuration.

#Extra Information

You can install so-called userparameter files by adding the following into your roles:

```
- name: "Installing sample file"
  copy: src=sample.conf
        dest="{{ agent_include }}/mysql.conf"
        owner=zabbix
        group=zabbix
        mode=0755
  notify: restart zabbix-agent
```

Example of the "sample.conf" file:

```
UserParameter=mysql.ping_to,mysqladmin -uroot ping | grep -c alive
```

You can extend your zabbix configuration by adding items yourself that do specific checks which aren't in the zabbix core itself. You can change offcourse the name of the file to whatever you want (Same for the UserParameter line(s) ;-) 

(Maybe in near future doing it with variables.)

#License

GPLv3

#Author Information

Please send suggestion or pull requests to make this role better. Also let me know if you encouter any issues installing or using this role.

Github: https://github.com/dj-wasabi/ansible-zabbix-agent

mail: ikben [ at ] werner-dijkerman . nl
