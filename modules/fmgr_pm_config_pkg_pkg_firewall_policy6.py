#!/usr/bin/python
from __future__ import absolute_import, division, print_function
# Copyright 2019 Fortinet, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

__metaclass__ = type

ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'community',
                    'metadata_version': '1.1'}

DOCUMENTATION = '''
---
module: fmgr_pm_config_pkg_pkg_firewall_policy6
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ add get set update ] the following apis:
    - /pm/config/adom/{adom}/pkg/{pkg}/firewall/policy6
    - Examples include all parameters and values need to be adjusted to data 
      sources before usage.
     

version_added: "2.10"
author:
    - Frank Shen (@fshen01)
    - Link Zheng (@zhengl)
notes:
    - There are only three top-level parameters where 'method' is always required
      while other two 'params' and 'url_params' can be optional
    - Due to the complexity of fortimanager api schema, the validation is done
      out of Ansible native parameter validation procedure.
    - The syntax of OPTIONS doen not comply with the standard Ansible argument 
      specification, but with the structure of fortimanager API schema, we need
      a trivial transformation when we are filling the ansible playbook
options:
    url_params: 
        description: the parameters in url path
        required: True
        type: dict
        suboptions:
            adom:
                type: str
                description: the domain prefix, the none and global are reserved
                choices:
                  - none
                  - global
                  - custom dom
            pkg:
                type: str
    schema_object0:
        methods: [add, set, update]
        description: 'Configure IPv6 policies.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                -
                    action:
                        type: str
                        description: 'Policy action (allow/deny/ipsec).'
                        choices:
                            - deny
                            - accept
                            - ipsec
                            - ssl-vpn
                    app-category:
                        type: str
                        description: 'Application category ID list.'
                    application:
                        -
                            type: int
                    application-list:
                        type: str
                        description: 'Name of an existing Application list.'
                    auto-asic-offload:
                        type: str
                        description: 'Enable/disable policy traffic ASIC offloading.'
                        choices:
                            - disable
                            - enable
                    av-profile:
                        type: str
                        description: 'Name of an existing Antivirus profile.'
                    comments:
                        type: str
                        description: 'Comment.'
                    custom-log-fields:
                        type: str
                        description: 'Log field index numbers to append custom log fields to log messages for this policy.'
                    devices:
                        type: str
                        description: 'Names of devices or device groups that can be matched by the policy.'
                    diffserv-forward:
                        type: str
                        description: 'Enable to change packet's DiffServ values to the specified diffservcode-forward value.'
                        choices:
                            - disable
                            - enable
                    diffserv-reverse:
                        type: str
                        description: 'Enable to change packet's reverse (reply) DiffServ values to the specified diffservcode-rev value.'
                        choices:
                            - disable
                            - enable
                    diffservcode-forward:
                        type: str
                        description: 'Change packet's DiffServ to this value.'
                    diffservcode-rev:
                        type: str
                        description: 'Change packet's reverse (reply) DiffServ to this value.'
                    dlp-sensor:
                        type: str
                        description: 'Name of an existing DLP sensor.'
                    dscp-match:
                        type: str
                        description: 'Enable DSCP check.'
                        choices:
                            - disable
                            - enable
                    dscp-negate:
                        type: str
                        description: 'Enable negated DSCP match.'
                        choices:
                            - disable
                            - enable
                    dscp-value:
                        type: str
                        description: 'DSCP value.'
                    dsri:
                        type: str
                        description: 'Enable DSRI to ignore HTTP server responses.'
                        choices:
                            - disable
                            - enable
                    dstaddr:
                        type: str
                        description: 'Destination address and address group names.'
                    dstaddr-negate:
                        type: str
                        description: 'When enabled dstaddr specifies what the destination address must NOT be.'
                        choices:
                            - disable
                            - enable
                    dstintf:
                        type: str
                        description: 'Outgoing (egress) interface.'
                    firewall-session-dirty:
                        type: str
                        description: 'How to handle sessions if the configuration of this firewall policy changes.'
                        choices:
                            - check-all
                            - check-new
                    fixedport:
                        type: str
                        description: 'Enable to prevent source NAT from changing a session's source port.'
                        choices:
                            - disable
                            - enable
                    global-label:
                        type: str
                        description: 'Label for the policy that appears when the GUI is in Global View mode.'
                    groups:
                        type: str
                        description: 'Names of user groups that can authenticate with this policy.'
                    icap-profile:
                        type: str
                        description: 'Name of an existing ICAP profile.'
                    inbound:
                        type: str
                        description: 'Policy-based IPsec VPN: only traffic from the remote network can initiate a VPN.'
                        choices:
                            - disable
                            - enable
                    ippool:
                        type: str
                        description: 'Enable to use IP Pools for source NAT.'
                        choices:
                            - disable
                            - enable
                    ips-sensor:
                        type: str
                        description: 'Name of an existing IPS sensor.'
                    label:
                        type: str
                        description: 'Label for the policy that appears when the GUI is in Section View mode.'
                    logtraffic:
                        type: str
                        description: 'Enable or disable logging. Log all sessions or security profile sessions.'
                        choices:
                            - disable
                            - enable
                            - all
                            - utm
                    logtraffic-start:
                        type: str
                        description: 'Record logs when a session starts and ends.'
                        choices:
                            - disable
                            - enable
                    mms-profile:
                        type: str
                        description: 'Name of an existing MMS profile.'
                    name:
                        type: str
                        description: 'Policy name.'
                    nat:
                        type: str
                        description: 'Enable/disable source NAT.'
                        choices:
                            - disable
                            - enable
                    natinbound:
                        type: str
                        description: 'Policy-based IPsec VPN: apply destination NAT to inbound traffic.'
                        choices:
                            - disable
                            - enable
                    natoutbound:
                        type: str
                        description: 'Policy-based IPsec VPN: apply source NAT to outbound traffic.'
                        choices:
                            - disable
                            - enable
                    np-accelation:
                        type: str
                        description: 'Enable/disable UTM Network Processor acceleration.'
                        choices:
                            - disable
                            - enable
                    outbound:
                        type: str
                        description: 'Policy-based IPsec VPN: only traffic from the internal network can initiate a VPN.'
                        choices:
                            - disable
                            - enable
                    per-ip-shaper:
                        type: str
                        description: 'Per-IP traffic shaper.'
                    policyid:
                        type: int
                        description: 'Policy ID.'
                    poolname:
                        type: str
                        description: 'IP Pool names.'
                    profile-group:
                        type: str
                        description: 'Name of profile group.'
                    profile-protocol-options:
                        type: str
                        description: 'Name of an existing Protocol options profile.'
                    profile-type:
                        type: str
                        description: 'Determine whether the firewall policy allows security profile groups or single profiles only.'
                        choices:
                            - single
                            - group
                    replacemsg-override-group:
                        type: str
                        description: 'Override the default replacement message group for this policy.'
                    rsso:
                        type: str
                        description: 'Enable/disable RADIUS single sign-on (RSSO).'
                        choices:
                            - disable
                            - enable
                    schedule:
                        type: str
                        description: 'Schedule name.'
                    send-deny-packet:
                        type: str
                        description: 'Enable/disable return of deny-packet.'
                        choices:
                            - disable
                            - enable
                    service:
                        type: str
                        description: 'Service and service group names.'
                    service-negate:
                        type: str
                        description: 'When enabled service specifies what the service must NOT be.'
                        choices:
                            - disable
                            - enable
                    session-ttl:
                        type: int
                        description: 'Session TTL in seconds for sessions accepted by this policy. 0 means use the system default session TTL.'
                    spamfilter-profile:
                        type: str
                        description: 'Name of an existing Spam filter profile.'
                    srcaddr:
                        type: str
                        description: 'Source address and address group names.'
                    srcaddr-negate:
                        type: str
                        description: 'When enabled srcaddr specifies what the source address must NOT be.'
                        choices:
                            - disable
                            - enable
                    srcintf:
                        type: str
                        description: 'Incoming (ingress) interface.'
                    ssl-mirror:
                        type: str
                        description: 'Enable to copy decrypted SSL traffic to a FortiGate interface (called SSL mirroring).'
                        choices:
                            - disable
                            - enable
                    ssl-mirror-intf:
                        type: str
                        description: 'SSL mirror interface name.'
                    ssl-ssh-profile:
                        type: str
                        description: 'Name of an existing SSL SSH profile.'
                    status:
                        type: str
                        description: 'Enable or disable this policy.'
                        choices:
                            - disable
                            - enable
                    tags:
                        type: str
                        description: 'Names of object-tags applied to this policy.'
                    tcp-mss-receiver:
                        type: int
                        description: 'Receiver TCP maximum segment size (MSS).'
                    tcp-mss-sender:
                        type: int
                        description: 'Sender TCP maximum segment size (MSS).'
                    tcp-session-without-syn:
                        type: str
                        description: 'Enable/disable creation of TCP session without SYN flag.'
                        choices:
                            - all
                            - data-only
                            - disable
                    timeout-send-rst:
                        type: str
                        description: 'Enable/disable sending RST packets when TCP sessions expire.'
                        choices:
                            - disable
                            - enable
                    traffic-shaper:
                        type: str
                        description: 'Reverse traffic shaper.'
                    traffic-shaper-reverse:
                        type: str
                        description: 'Reverse traffic shaper.'
                    url-category:
                        type: str
                        description: 'URL category ID list.'
                    users:
                        type: str
                        description: 'Names of individual users that can authenticate with this policy.'
                    utm-status:
                        type: str
                        description: 'Enable AV/web/ips protection profile.'
                        choices:
                            - disable
                            - enable
                    uuid:
                        type: str
                        description: 'Universally Unique Identifier (UUID; automatically assigned but can be manually reset).'
                    vlan-cos-fwd:
                        type: int
                        description: 'VLAN forward direction user priority: 255 passthrough, 0 lowest, 7 highest'
                    vlan-cos-rev:
                        type: int
                        description: 'VLAN reverse direction user priority: 255 passthrough, 0 lowest, 7 highest'
                    voip-profile:
                        type: str
                        description: 'Name of an existing VoIP profile.'
                    vpntunnel:
                        type: str
                        description: 'Policy-based IPsec VPN: name of the IPsec VPN Phase 1.'
                    webfilter-profile:
                        type: str
                        description: 'Name of an existing Web filter profile.'
    schema_object1:
        methods: [get]
        description: 'Configure IPv6 policies.'
        api_categories: [api_tag0]
        api_tag0:
            attr:
                type: str
                description: 'The name of the attribute to retrieve its datasource. Only used with &lt;i&gt;datasrc&lt;/i&gt; option.'
            fields:
                -
                    -
                        type: str
                        choices:
                            - action
                            - app-category
                            - application
                            - application-list
                            - auto-asic-offload
                            - av-profile
                            - comments
                            - custom-log-fields
                            - devices
                            - diffserv-forward
                            - diffserv-reverse
                            - diffservcode-forward
                            - diffservcode-rev
                            - dlp-sensor
                            - dscp-match
                            - dscp-negate
                            - dscp-value
                            - dsri
                            - dstaddr
                            - dstaddr-negate
                            - dstintf
                            - firewall-session-dirty
                            - fixedport
                            - global-label
                            - groups
                            - icap-profile
                            - inbound
                            - ippool
                            - ips-sensor
                            - label
                            - logtraffic
                            - logtraffic-start
                            - mms-profile
                            - name
                            - nat
                            - natinbound
                            - natoutbound
                            - np-accelation
                            - outbound
                            - per-ip-shaper
                            - policyid
                            - poolname
                            - profile-group
                            - profile-protocol-options
                            - profile-type
                            - replacemsg-override-group
                            - rsso
                            - schedule
                            - send-deny-packet
                            - service
                            - service-negate
                            - session-ttl
                            - spamfilter-profile
                            - srcaddr
                            - srcaddr-negate
                            - srcintf
                            - ssl-mirror
                            - ssl-mirror-intf
                            - ssl-ssh-profile
                            - status
                            - tags
                            - tcp-mss-receiver
                            - tcp-mss-sender
                            - tcp-session-without-syn
                            - timeout-send-rst
                            - traffic-shaper
                            - traffic-shaper-reverse
                            - url-category
                            - users
                            - utm-status
                            - uuid
                            - vlan-cos-fwd
                            - vlan-cos-rev
                            - voip-profile
                            - vpntunnel
                            - webfilter-profile
            filter:
                -
                    type: str
            get used:
                type: int
            loadsub:
                type: int
                description: 'Enable or disable the return of any sub-objects. If not specified, the default is to return all sub-objects.'
            option:
                type: str
                description:
                 - 'Set fetch option for the request. If no option is specified, by default the attributes of the objects will be returned.'
                 - 'count - Return the number of matching entries instead of the actual entry data.'
                 - 'object member - Return a list of object members along with other attributes.'
                 - 'datasrc - Return all objects that can be referenced by an attribute. Require <i>attr</i> parameter.'
                 - 'get reserved - Also return reserved objects in the result.'
                 - 'syntax - Return the attribute syntax of a table or an object, instead of the actual entry data. All filter parameters will be ignored.'
                choices:
                    - count
                    - object member
                    - datasrc
                    - get reserved
                    - syntax
            range:
                -
                    type: int
            sortings:
                -
                    \{attr_name\}:
                        type: int
                        choices:
                            - 1
                            - -1

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:
    - name: send request to /pm/config/pkg/{pkg}/firewall/policy6
      fmgr_pm_config_pkg_pkg_firewall_policy6:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            pkg: <value of string>
         params:
            - 
               data: 
                - 
                     action: <value in [deny, accept, ipsec, ...]>
                     app-category: <value of string>
                     application: 
                      - <value of integer>
                     application-list: <value of string>
                     auto-asic-offload: <value in [disable, enable]>
                     av-profile: <value of string>
                     comments: <value of string>
                     custom-log-fields: <value of string>
                     devices: <value of string>
                     diffserv-forward: <value in [disable, enable]>
                     diffserv-reverse: <value in [disable, enable]>
                     diffservcode-forward: <value of string>
                     diffservcode-rev: <value of string>
                     dlp-sensor: <value of string>
                     dscp-match: <value in [disable, enable]>
                     dscp-negate: <value in [disable, enable]>
                     dscp-value: <value of string>
                     dsri: <value in [disable, enable]>
                     dstaddr: <value of string>
                     dstaddr-negate: <value in [disable, enable]>
                     dstintf: <value of string>
                     firewall-session-dirty: <value in [check-all, check-new]>
                     fixedport: <value in [disable, enable]>
                     global-label: <value of string>
                     groups: <value of string>
                     icap-profile: <value of string>
                     inbound: <value in [disable, enable]>
                     ippool: <value in [disable, enable]>
                     ips-sensor: <value of string>
                     label: <value of string>
                     logtraffic: <value in [disable, enable, all, ...]>
                     logtraffic-start: <value in [disable, enable]>
                     mms-profile: <value of string>
                     name: <value of string>
                     nat: <value in [disable, enable]>
                     natinbound: <value in [disable, enable]>
                     natoutbound: <value in [disable, enable]>
                     np-accelation: <value in [disable, enable]>
                     outbound: <value in [disable, enable]>
                     per-ip-shaper: <value of string>
                     policyid: <value of integer>
                     poolname: <value of string>
                     profile-group: <value of string>
                     profile-protocol-options: <value of string>
                     profile-type: <value in [single, group]>
                     replacemsg-override-group: <value of string>
                     rsso: <value in [disable, enable]>
                     schedule: <value of string>
                     send-deny-packet: <value in [disable, enable]>
                     service: <value of string>
                     service-negate: <value in [disable, enable]>
                     session-ttl: <value of integer>
                     spamfilter-profile: <value of string>
                     srcaddr: <value of string>
                     srcaddr-negate: <value in [disable, enable]>
                     srcintf: <value of string>
                     ssl-mirror: <value in [disable, enable]>
                     ssl-mirror-intf: <value of string>
                     ssl-ssh-profile: <value of string>
                     status: <value in [disable, enable]>
                     tags: <value of string>
                     tcp-mss-receiver: <value of integer>
                     tcp-mss-sender: <value of integer>
                     tcp-session-without-syn: <value in [all, data-only, disable]>
                     timeout-send-rst: <value in [disable, enable]>
                     traffic-shaper: <value of string>
                     traffic-shaper-reverse: <value of string>
                     url-category: <value of string>
                     users: <value of string>
                     utm-status: <value in [disable, enable]>
                     uuid: <value of string>
                     vlan-cos-fwd: <value of integer>
                     vlan-cos-rev: <value of integer>
                     voip-profile: <value of string>
                     vpntunnel: <value of string>
                     webfilter-profile: <value of string>
    - name: send request to /pm/config/pkg/{pkg}/firewall/policy6
      fmgr_pm_config_pkg_pkg_firewall_policy6:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            pkg: <value of string>
         params:
            - 
               attr: <value of string>
               fields: 
                - 
                   - <value in [action, app-category, application, ...]>
               filter: 
                - <value of string>
               get used: <value of integer>
               loadsub: <value of integer>
               option: <value in [count, object member, datasrc, ...]>
               range: 
                - <value of integer>
               sortings: 
                - 
                     \{attr_name\}: <value in [1, -1]>

'''

RETURN = '''
return_of_api_category_0:
   description: items returned for method:[add, set, update]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            type: array
            suboptions:
               policyid:
                  type: int
                  description: 'Policy ID.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: /pm/config/adom/{adom}/pkg/{pkg}/firewall/policy6
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            type: array
            suboptions:
               action:
                  type: str
                  description: 'Policy action (allow/deny/ipsec).'
               app-category:
                  type: str
                  description: 'Application category ID list.'
               application:
                  type: array
                  suboptions:
                     type: int
               application-list:
                  type: str
                  description: 'Name of an existing Application list.'
               auto-asic-offload:
                  type: str
                  description: 'Enable/disable policy traffic ASIC offloading.'
               av-profile:
                  type: str
                  description: 'Name of an existing Antivirus profile.'
               comments:
                  type: str
                  description: 'Comment.'
               custom-log-fields:
                  type: str
                  description: 'Log field index numbers to append custom log fields to log messages for this policy.'
               devices:
                  type: str
                  description: 'Names of devices or device groups that can be matched by the policy.'
               diffserv-forward:
                  type: str
                  description: 'Enable to change packet's DiffServ values to the specified diffservcode-forward value.'
               diffserv-reverse:
                  type: str
                  description: 'Enable to change packet's reverse (reply) DiffServ values to the specified diffservcode-rev value.'
               diffservcode-forward:
                  type: str
                  description: 'Change packet's DiffServ to this value.'
               diffservcode-rev:
                  type: str
                  description: 'Change packet's reverse (reply) DiffServ to this value.'
               dlp-sensor:
                  type: str
                  description: 'Name of an existing DLP sensor.'
               dscp-match:
                  type: str
                  description: 'Enable DSCP check.'
               dscp-negate:
                  type: str
                  description: 'Enable negated DSCP match.'
               dscp-value:
                  type: str
                  description: 'DSCP value.'
               dsri:
                  type: str
                  description: 'Enable DSRI to ignore HTTP server responses.'
               dstaddr:
                  type: str
                  description: 'Destination address and address group names.'
               dstaddr-negate:
                  type: str
                  description: 'When enabled dstaddr specifies what the destination address must NOT be.'
               dstintf:
                  type: str
                  description: 'Outgoing (egress) interface.'
               firewall-session-dirty:
                  type: str
                  description: 'How to handle sessions if the configuration of this firewall policy changes.'
               fixedport:
                  type: str
                  description: 'Enable to prevent source NAT from changing a session's source port.'
               global-label:
                  type: str
                  description: 'Label for the policy that appears when the GUI is in Global View mode.'
               groups:
                  type: str
                  description: 'Names of user groups that can authenticate with this policy.'
               icap-profile:
                  type: str
                  description: 'Name of an existing ICAP profile.'
               inbound:
                  type: str
                  description: 'Policy-based IPsec VPN: only traffic from the remote network can initiate a VPN.'
               ippool:
                  type: str
                  description: 'Enable to use IP Pools for source NAT.'
               ips-sensor:
                  type: str
                  description: 'Name of an existing IPS sensor.'
               label:
                  type: str
                  description: 'Label for the policy that appears when the GUI is in Section View mode.'
               logtraffic:
                  type: str
                  description: 'Enable or disable logging. Log all sessions or security profile sessions.'
               logtraffic-start:
                  type: str
                  description: 'Record logs when a session starts and ends.'
               mms-profile:
                  type: str
                  description: 'Name of an existing MMS profile.'
               name:
                  type: str
                  description: 'Policy name.'
               nat:
                  type: str
                  description: 'Enable/disable source NAT.'
               natinbound:
                  type: str
                  description: 'Policy-based IPsec VPN: apply destination NAT to inbound traffic.'
               natoutbound:
                  type: str
                  description: 'Policy-based IPsec VPN: apply source NAT to outbound traffic.'
               np-accelation:
                  type: str
                  description: 'Enable/disable UTM Network Processor acceleration.'
               outbound:
                  type: str
                  description: 'Policy-based IPsec VPN: only traffic from the internal network can initiate a VPN.'
               per-ip-shaper:
                  type: str
                  description: 'Per-IP traffic shaper.'
               policyid:
                  type: int
                  description: 'Policy ID.'
               poolname:
                  type: str
                  description: 'IP Pool names.'
               profile-group:
                  type: str
                  description: 'Name of profile group.'
               profile-protocol-options:
                  type: str
                  description: 'Name of an existing Protocol options profile.'
               profile-type:
                  type: str
                  description: 'Determine whether the firewall policy allows security profile groups or single profiles only.'
               replacemsg-override-group:
                  type: str
                  description: 'Override the default replacement message group for this policy.'
               rsso:
                  type: str
                  description: 'Enable/disable RADIUS single sign-on (RSSO).'
               schedule:
                  type: str
                  description: 'Schedule name.'
               send-deny-packet:
                  type: str
                  description: 'Enable/disable return of deny-packet.'
               service:
                  type: str
                  description: 'Service and service group names.'
               service-negate:
                  type: str
                  description: 'When enabled service specifies what the service must NOT be.'
               session-ttl:
                  type: int
                  description: 'Session TTL in seconds for sessions accepted by this policy. 0 means use the system default session TTL.'
               spamfilter-profile:
                  type: str
                  description: 'Name of an existing Spam filter profile.'
               srcaddr:
                  type: str
                  description: 'Source address and address group names.'
               srcaddr-negate:
                  type: str
                  description: 'When enabled srcaddr specifies what the source address must NOT be.'
               srcintf:
                  type: str
                  description: 'Incoming (ingress) interface.'
               ssl-mirror:
                  type: str
                  description: 'Enable to copy decrypted SSL traffic to a FortiGate interface (called SSL mirroring).'
               ssl-mirror-intf:
                  type: str
                  description: 'SSL mirror interface name.'
               ssl-ssh-profile:
                  type: str
                  description: 'Name of an existing SSL SSH profile.'
               status:
                  type: str
                  description: 'Enable or disable this policy.'
               tags:
                  type: str
                  description: 'Names of object-tags applied to this policy.'
               tcp-mss-receiver:
                  type: int
                  description: 'Receiver TCP maximum segment size (MSS).'
               tcp-mss-sender:
                  type: int
                  description: 'Sender TCP maximum segment size (MSS).'
               tcp-session-without-syn:
                  type: str
                  description: 'Enable/disable creation of TCP session without SYN flag.'
               timeout-send-rst:
                  type: str
                  description: 'Enable/disable sending RST packets when TCP sessions expire.'
               traffic-shaper:
                  type: str
                  description: 'Reverse traffic shaper.'
               traffic-shaper-reverse:
                  type: str
                  description: 'Reverse traffic shaper.'
               url-category:
                  type: str
                  description: 'URL category ID list.'
               users:
                  type: str
                  description: 'Names of individual users that can authenticate with this policy.'
               utm-status:
                  type: str
                  description: 'Enable AV/web/ips protection profile.'
               uuid:
                  type: str
                  description: 'Universally Unique Identifier (UUID; automatically assigned but can be manually reset).'
               vlan-cos-fwd:
                  type: int
                  description: 'VLAN forward direction user priority: 255 passthrough, 0 lowest, 7 highest'
               vlan-cos-rev:
                  type: int
                  description: 'VLAN reverse direction user priority: 255 passthrough, 0 lowest, 7 highest'
               voip-profile:
                  type: str
                  description: 'Name of an existing VoIP profile.'
               vpntunnel:
                  type: str
                  description: 'Policy-based IPsec VPN: name of the IPsec VPN Phase 1.'
               webfilter-profile:
                  type: str
                  description: 'Name of an existing Web filter profile.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: /pm/config/adom/{adom}/pkg/{pkg}/firewall/policy6

'''
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from ansible.module_utils.network.fortimanager.common import FAIL_SOCKET_MSG
from ansible.module_utils.network.fortimanager.common import DEFAULT_RESULT_OBJ
from ansible.module_utils.network.fortimanager.common import FMGRCommon
from ansible.module_utils.network.fortimanager.common import FMGBaseException
from ansible.module_utils.network.fortimanager.fortimanager import FortiManagerHandler

def main():
    jrpc_urls = [
        '/pm/config/adom/{adom}/pkg/{pkg}/firewall/policy6'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'pkg',
            'type': 'string'
        }
    ]

    body_schema =  {
        'schema_objects': {
            'object0': [
                {
                    'name': 'data',
                    'api_tag': 0,
                    'type': 'array',
                    'items': {
                        'action': {
                            'type': 'string',
                            'enum': [
                                'deny',
                                'accept',
                                'ipsec',
                                'ssl-vpn'
                            ]
                        },
                        'app-category': {
                            'type': 'string'
                        },
                        'application': {
                            'type': 'array',
                            'items': {
                                'type': 'integer'
                            }
                        },
                        'application-list': {
                            'type': 'string'
                        },
                        'auto-asic-offload': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'av-profile': {
                            'type': 'string'
                        },
                        'comments': {
                            'type': 'string'
                        },
                        'custom-log-fields': {
                            'type': 'string'
                        },
                        'devices': {
                            'type': 'string'
                        },
                        'diffserv-forward': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'diffserv-reverse': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'diffservcode-forward': {
                            'type': 'string'
                        },
                        'diffservcode-rev': {
                            'type': 'string'
                        },
                        'dlp-sensor': {
                            'type': 'string'
                        },
                        'dscp-match': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'dscp-negate': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'dscp-value': {
                            'type': 'string'
                        },
                        'dsri': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'dstaddr': {
                            'type': 'string'
                        },
                        'dstaddr-negate': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'dstintf': {
                            'type': 'string'
                        },
                        'firewall-session-dirty': {
                            'type': 'string',
                            'enum': [
                                'check-all',
                                'check-new'
                            ]
                        },
                        'fixedport': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'global-label': {
                            'type': 'string'
                        },
                        'groups': {
                            'type': 'string'
                        },
                        'icap-profile': {
                            'type': 'string'
                        },
                        'inbound': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ippool': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ips-sensor': {
                            'type': 'string'
                        },
                        'label': {
                            'type': 'string'
                        },
                        'logtraffic': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable',
                                'all',
                                'utm'
                            ]
                        },
                        'logtraffic-start': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'mms-profile': {
                            'type': 'string'
                        },
                        'name': {
                            'type': 'string'
                        },
                        'nat': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'natinbound': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'natoutbound': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'np-accelation': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'outbound': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'per-ip-shaper': {
                            'type': 'string'
                        },
                        'policyid': {
                            'type': 'integer'
                        },
                        'poolname': {
                            'type': 'string'
                        },
                        'profile-group': {
                            'type': 'string'
                        },
                        'profile-protocol-options': {
                            'type': 'string'
                        },
                        'profile-type': {
                            'type': 'string',
                            'enum': [
                                'single',
                                'group'
                            ]
                        },
                        'replacemsg-override-group': {
                            'type': 'string'
                        },
                        'rsso': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'schedule': {
                            'type': 'string'
                        },
                        'send-deny-packet': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'service': {
                            'type': 'string'
                        },
                        'service-negate': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'session-ttl': {
                            'type': 'integer'
                        },
                        'spamfilter-profile': {
                            'type': 'string'
                        },
                        'srcaddr': {
                            'type': 'string'
                        },
                        'srcaddr-negate': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'srcintf': {
                            'type': 'string'
                        },
                        'ssl-mirror': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ssl-mirror-intf': {
                            'type': 'string'
                        },
                        'ssl-ssh-profile': {
                            'type': 'string'
                        },
                        'status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'tags': {
                            'type': 'string'
                        },
                        'tcp-mss-receiver': {
                            'type': 'integer'
                        },
                        'tcp-mss-sender': {
                            'type': 'integer'
                        },
                        'tcp-session-without-syn': {
                            'type': 'string',
                            'enum': [
                                'all',
                                'data-only',
                                'disable'
                            ]
                        },
                        'timeout-send-rst': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'traffic-shaper': {
                            'type': 'string'
                        },
                        'traffic-shaper-reverse': {
                            'type': 'string'
                        },
                        'url-category': {
                            'type': 'string'
                        },
                        'users': {
                            'type': 'string'
                        },
                        'utm-status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'uuid': {
                            'type': 'string'
                        },
                        'vlan-cos-fwd': {
                            'type': 'integer'
                        },
                        'vlan-cos-rev': {
                            'type': 'integer'
                        },
                        'voip-profile': {
                            'type': 'string'
                        },
                        'vpntunnel': {
                            'type': 'string'
                        },
                        'webfilter-profile': {
                            'type': 'string'
                        }
                    }
                },
                {
                    'type': 'string',
                    'name': 'url',
                    'api_tag': 0
                }
            ],
            'object1': [
                {
                    'type': 'string',
                    'name': 'attr',
                    'api_tag': 0
                },
                {
                    'name': 'fields',
                    'api_tag': 0,
                    'type': 'array',
                    'items': {
                        'type': 'array',
                        'items': {
                            'type': 'string',
                            'enum': [
                                'action',
                                'app-category',
                                'application',
                                'application-list',
                                'auto-asic-offload',
                                'av-profile',
                                'comments',
                                'custom-log-fields',
                                'devices',
                                'diffserv-forward',
                                'diffserv-reverse',
                                'diffservcode-forward',
                                'diffservcode-rev',
                                'dlp-sensor',
                                'dscp-match',
                                'dscp-negate',
                                'dscp-value',
                                'dsri',
                                'dstaddr',
                                'dstaddr-negate',
                                'dstintf',
                                'firewall-session-dirty',
                                'fixedport',
                                'global-label',
                                'groups',
                                'icap-profile',
                                'inbound',
                                'ippool',
                                'ips-sensor',
                                'label',
                                'logtraffic',
                                'logtraffic-start',
                                'mms-profile',
                                'name',
                                'nat',
                                'natinbound',
                                'natoutbound',
                                'np-accelation',
                                'outbound',
                                'per-ip-shaper',
                                'policyid',
                                'poolname',
                                'profile-group',
                                'profile-protocol-options',
                                'profile-type',
                                'replacemsg-override-group',
                                'rsso',
                                'schedule',
                                'send-deny-packet',
                                'service',
                                'service-negate',
                                'session-ttl',
                                'spamfilter-profile',
                                'srcaddr',
                                'srcaddr-negate',
                                'srcintf',
                                'ssl-mirror',
                                'ssl-mirror-intf',
                                'ssl-ssh-profile',
                                'status',
                                'tags',
                                'tcp-mss-receiver',
                                'tcp-mss-sender',
                                'tcp-session-without-syn',
                                'timeout-send-rst',
                                'traffic-shaper',
                                'traffic-shaper-reverse',
                                'url-category',
                                'users',
                                'utm-status',
                                'uuid',
                                'vlan-cos-fwd',
                                'vlan-cos-rev',
                                'voip-profile',
                                'vpntunnel',
                                'webfilter-profile'
                            ]
                        }
                    }
                },
                {
                    'name': 'filter',
                    'type': 'dict',
                    'dict': {
                        'type': 'array',
                        'items': {
                            'type': 'string',
                            'example': [
                                '<attr>',
                                '==',
                                'test'
                            ]
                        }
                    },
                    'api_tag': 0
                },
                {
                    'type': 'integer',
                    'name': 'get used',
                    'api_tag': 0
                },
                {
                    'type': 'integer',
                    'name': 'loadsub',
                    'api_tag': 0
                },
                {
                    'name': 'option',
                    'type': 'dict',
                    'dict': {
                        'type': 'string',
                        'enum': [
                            'count',
                            'object member',
                            'datasrc',
                            'get reserved',
                            'syntax'
                        ]
                    },
                    'api_tag': 0
                },
                {
                    'name': 'range',
                    'type': 'dict',
                    'dict': {
                        'type': 'array',
                        'items': {
                            'type': 'integer',
                            'example': [
                                2,
                                5
                            ]
                        }
                    },
                    'api_tag': 0
                },
                {
                    'name': 'sortings',
                    'type': 'dict',
                    'dict': {
                        'type': 'array',
                        'items': {
                            '{attr_name}': {
                                'type': 'integer',
                                'enum': [
                                    1,
                                    -1
                                ]
                            }
                        }
                    },
                    'api_tag': 0
                },
                {
                    'type': 'string',
                    'name': 'url',
                    'api_tag': 0
                }
            ]
        },
        'method_mapping': {
            'add': 'object0',
            'get': 'object1',
            'set': 'object0',
            'update': 'object0'
        }
    }


    module_arg_spec = {
        'params': {
            'type': 'list',
            'required': False
        },
        'method': {
            'type': 'str',
            'required': True,
            'choices': [
                'add',
                'get',
                'set',
                'update'
            ]
        },
        'url_params': {
            'type': 'dict',
            'required': False
        }
    }
    module = AnsibleModule(argument_spec = module_arg_spec,
                           supports_check_mode = False)
    method = module.params['method']

    fmgr = None
    payload = None
    response = DEFAULT_RESULT_OBJ

    if module._socket_path:
        connection = Connection(module._socket_path)
        tools = FMGRCommon()
        tools.validate_module_params(module, body_schema)
        tools.validate_module_url_params(module, jrpc_urls, url_schema)
        full_url = tools.get_full_url_path(module, jrpc_urls)
        payload = tools.get_full_payload(module, full_url)
        fmgr = FortiManagerHandler(connection, module)
        fmgr.tools = tools
    else:
        module.fail_json(**FAIL_SOCKET_MSG)

    try:
        response = fmgr._conn.send_request(method, payload)
        fmgr.govern_response(module = module, results = response,
                             msg = 'Operation Finished',
                             ansible_facts = fmgr.construct_ansible_facts(
                                response, module.params, module.params))
    except Exception as e:
        raise FMGBaseException(e)

    module.exit_json(**response[1])

if __name__ == '__main__':
    main()