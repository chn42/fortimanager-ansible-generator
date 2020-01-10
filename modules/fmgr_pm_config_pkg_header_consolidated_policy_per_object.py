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
module: fmgr_pm_config_pkg_header_consolidated_policy_per_object
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ clone delete get set update ] the following apis.
    - /pm/config/global/pkg/{pkg}/global/header/consolidated/policy/{policy}
    - Examples include all parameters and values need to be adjusted to data sources before usage.

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
            pkg:
                type: str
            policy:
                type: str
    schema_object0:
        methods: [clone, set, update]
        description: ''
        api_categories: [api_tag0]
        api_tag0:
            data:
                action:
                    type: str
                    choices:
                        - 'deny'
                        - 'accept'
                        - 'ipsec'
                app-category:
                    -
                        type: int
                app-group:
                    type: str
                application:
                    -
                        type: int
                application-list:
                    type: str
                auto-asic-offload:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                av-profile:
                    type: str
                cifs-profile:
                    type: str
                comments:
                    type: str
                diffserv-forward:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                diffserv-reverse:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                diffservcode-forward:
                    type: str
                diffservcode-rev:
                    type: str
                dlp-sensor:
                    type: str
                dnsfilter-profile:
                    type: str
                dstaddr4:
                    type: str
                dstaddr6:
                    type: str
                dstintf:
                    type: str
                emailfilter-profile:
                    type: str
                fixedport:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                groups:
                    type: str
                http-policy-redirect:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                icap-profile:
                    type: str
                inbound:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                inspection-mode:
                    type: str
                    choices:
                        - 'proxy'
                        - 'flow'
                ippool:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                ips-sensor:
                    type: str
                logtraffic:
                    type: str
                    choices:
                        - 'disable'
                        - 'all'
                        - 'utm'
                logtraffic-start:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                mms-profile:
                    type: str
                name:
                    type: str
                nat:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                outbound:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                per-ip-shaper:
                    type: str
                policyid:
                    type: int
                poolname4:
                    type: str
                poolname6:
                    type: str
                profile-group:
                    type: str
                profile-protocol-options:
                    type: str
                profile-type:
                    type: str
                    choices:
                        - 'single'
                        - 'group'
                schedule:
                    type: str
                schedule-timeout:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                service:
                    type: str
                session-ttl:
                    type: int
                spamfilter-profile:
                    type: str
                srcaddr4:
                    type: str
                srcaddr6:
                    type: str
                srcintf:
                    type: str
                ssh-filter-profile:
                    type: str
                ssh-policy-redirect:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                ssl-ssh-profile:
                    type: str
                status:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                tcp-mss-receiver:
                    type: int
                tcp-mss-sender:
                    type: int
                traffic-shaper:
                    type: str
                traffic-shaper-reverse:
                    type: str
                url-category:
                    -
                        type: int
                users:
                    type: str
                utm-inspection-mode:
                    type: str
                    choices:
                        - 'proxy'
                        - 'flow'
                utm-status:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                uuid:
                    type: str
                voip-profile:
                    type: str
                vpntunnel:
                    type: str
                waf-profile:
                    type: str
                webfilter-profile:
                    type: str
    schema_object1:
        methods: [delete]
        description: ''
        api_categories: [api_tag0]
        api_tag0:
    schema_object2:
        methods: [get]
        description: ''
        api_categories: [api_tag0]
        api_tag0:
            option:
                type: str
                description:
                 - 'Set fetch option for the request. If no option is specified, by default the attributes of the object will be returned.'
                 - 'object member - Return a list of object members along with other attributes.'
                 - 'chksum - Return the check-sum value instead of attributes.'
                choices:
                    - 'object member'
                    - 'chksum'
                    - 'datasrc'

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /PM/CONFIG/PKG/{PKG}/HEADER/CONSOLIDATED/POLICY/{POLICY}
      fmgr_pm_config_pkg_header_consolidated_policy_per_object:
         method: <value in [clone, set, update]>
         url_params:
            pkg: <value of string>
            policy: <value of string>
         params:
            -
               data:
                  action: <value in [deny, accept, ipsec]>
                  app-category:
                    - <value of integer>
                  app-group: <value of string>
                  application:
                    - <value of integer>
                  application-list: <value of string>
                  auto-asic-offload: <value in [disable, enable]>
                  av-profile: <value of string>
                  cifs-profile: <value of string>
                  comments: <value of string>
                  diffserv-forward: <value in [disable, enable]>
                  diffserv-reverse: <value in [disable, enable]>
                  diffservcode-forward: <value of string>
                  diffservcode-rev: <value of string>
                  dlp-sensor: <value of string>
                  dnsfilter-profile: <value of string>
                  dstaddr4: <value of string>
                  dstaddr6: <value of string>
                  dstintf: <value of string>
                  emailfilter-profile: <value of string>
                  fixedport: <value in [disable, enable]>
                  groups: <value of string>
                  http-policy-redirect: <value in [disable, enable]>
                  icap-profile: <value of string>
                  inbound: <value in [disable, enable]>
                  inspection-mode: <value in [proxy, flow]>
                  ippool: <value in [disable, enable]>
                  ips-sensor: <value of string>
                  logtraffic: <value in [disable, all, utm]>
                  logtraffic-start: <value in [disable, enable]>
                  mms-profile: <value of string>
                  name: <value of string>
                  nat: <value in [disable, enable]>
                  outbound: <value in [disable, enable]>
                  per-ip-shaper: <value of string>
                  policyid: <value of integer>
                  poolname4: <value of string>
                  poolname6: <value of string>
                  profile-group: <value of string>
                  profile-protocol-options: <value of string>
                  profile-type: <value in [single, group]>
                  schedule: <value of string>
                  schedule-timeout: <value in [disable, enable]>
                  service: <value of string>
                  session-ttl: <value of integer>
                  spamfilter-profile: <value of string>
                  srcaddr4: <value of string>
                  srcaddr6: <value of string>
                  srcintf: <value of string>
                  ssh-filter-profile: <value of string>
                  ssh-policy-redirect: <value in [disable, enable]>
                  ssl-ssh-profile: <value of string>
                  status: <value in [disable, enable]>
                  tcp-mss-receiver: <value of integer>
                  tcp-mss-sender: <value of integer>
                  traffic-shaper: <value of string>
                  traffic-shaper-reverse: <value of string>
                  url-category:
                    - <value of integer>
                  users: <value of string>
                  utm-inspection-mode: <value in [proxy, flow]>
                  utm-status: <value in [disable, enable]>
                  uuid: <value of string>
                  voip-profile: <value of string>
                  vpntunnel: <value of string>
                  waf-profile: <value of string>
                  webfilter-profile: <value of string>

    - name: REQUESTING /PM/CONFIG/PKG/{PKG}/HEADER/CONSOLIDATED/POLICY/{POLICY}
      fmgr_pm_config_pkg_header_consolidated_policy_per_object:
         method: <value in [get]>
         url_params:
            pkg: <value of string>
            policy: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

'''

RETURN = '''
return_of_api_category_0:
   description: items returned for method:[clone, set, update]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            policyid:
               type: int
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/global/pkg/{pkg}/global/header/consolidated/policy/{policy}'
return_of_api_category_0:
   description: items returned for method:[delete]
   returned: always
   suboptions:
      id:
         type: int
      result:
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/global/pkg/{pkg}/global/header/consolidated/policy/{policy}'
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            action:
               type: str
            app-category:
               type: array
               suboptions:
                  type: int
            app-group:
               type: str
            application:
               type: array
               suboptions:
                  type: int
            application-list:
               type: str
            auto-asic-offload:
               type: str
            av-profile:
               type: str
            cifs-profile:
               type: str
            comments:
               type: str
            diffserv-forward:
               type: str
            diffserv-reverse:
               type: str
            diffservcode-forward:
               type: str
            diffservcode-rev:
               type: str
            dlp-sensor:
               type: str
            dnsfilter-profile:
               type: str
            dstaddr4:
               type: str
            dstaddr6:
               type: str
            dstintf:
               type: str
            emailfilter-profile:
               type: str
            fixedport:
               type: str
            groups:
               type: str
            http-policy-redirect:
               type: str
            icap-profile:
               type: str
            inbound:
               type: str
            inspection-mode:
               type: str
            ippool:
               type: str
            ips-sensor:
               type: str
            logtraffic:
               type: str
            logtraffic-start:
               type: str
            mms-profile:
               type: str
            name:
               type: str
            nat:
               type: str
            outbound:
               type: str
            per-ip-shaper:
               type: str
            policyid:
               type: int
            poolname4:
               type: str
            poolname6:
               type: str
            profile-group:
               type: str
            profile-protocol-options:
               type: str
            profile-type:
               type: str
            schedule:
               type: str
            schedule-timeout:
               type: str
            service:
               type: str
            session-ttl:
               type: int
            spamfilter-profile:
               type: str
            srcaddr4:
               type: str
            srcaddr6:
               type: str
            srcintf:
               type: str
            ssh-filter-profile:
               type: str
            ssh-policy-redirect:
               type: str
            ssl-ssh-profile:
               type: str
            status:
               type: str
            tcp-mss-receiver:
               type: int
            tcp-mss-sender:
               type: int
            traffic-shaper:
               type: str
            traffic-shaper-reverse:
               type: str
            url-category:
               type: array
               suboptions:
                  type: int
            users:
               type: str
            utm-inspection-mode:
               type: str
            utm-status:
               type: str
            uuid:
               type: str
            voip-profile:
               type: str
            vpntunnel:
               type: str
            waf-profile:
               type: str
            webfilter-profile:
               type: str
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/global/pkg/{pkg}/global/header/consolidated/policy/{policy}'

'''
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from ansible_collections.chillancezen.fortimanager.plugins.module_utils.common import FAIL_SOCKET_MSG
from ansible_collections.chillancezen.fortimanager.plugins.module_utils.common import DEFAULT_RESULT_OBJ
from ansible_collections.chillancezen.fortimanager.plugins.module_utils.common import FMGRCommon
from ansible_collections.chillancezen.fortimanager.plugins.module_utils.common import FMGBaseException
from ansible_collections.chillancezen.fortimanager.plugins.module_utils.fortimanager import FortiManagerHandler


def main():
    jrpc_urls = [
        '/pm/config/global/pkg/{pkg}/global/header/consolidated/policy/{policy}'
    ]

    url_schema = [
        {
            'name': 'pkg',
            'type': 'string'
        },
        {
            'name': 'policy',
            'type': 'string'
        }
    ]

    body_schema = {
        'schema_objects': {
            'object0': [
                {
                    'name': 'data',
                    'type': 'dict',
                    'dict': {
                        'action': {
                            'type': 'string',
                            'enum': [
                                'deny',
                                'accept',
                                'ipsec'
                            ]
                        },
                        'app-category': {
                            'type': 'array',
                            'items': {
                                'type': 'integer'
                            }
                        },
                        'app-group': {
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
                        'cifs-profile': {
                            'type': 'string'
                        },
                        'comments': {
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
                        'dnsfilter-profile': {
                            'type': 'string'
                        },
                        'dstaddr4': {
                            'type': 'string'
                        },
                        'dstaddr6': {
                            'type': 'string'
                        },
                        'dstintf': {
                            'type': 'string'
                        },
                        'emailfilter-profile': {
                            'type': 'string'
                        },
                        'fixedport': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'groups': {
                            'type': 'string'
                        },
                        'http-policy-redirect': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
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
                        'inspection-mode': {
                            'type': 'string',
                            'enum': [
                                'proxy',
                                'flow'
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
                        'logtraffic': {
                            'type': 'string',
                            'enum': [
                                'disable',
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
                        'poolname4': {
                            'type': 'string'
                        },
                        'poolname6': {
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
                        'schedule': {
                            'type': 'string'
                        },
                        'schedule-timeout': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'service': {
                            'type': 'string'
                        },
                        'session-ttl': {
                            'type': 'integer'
                        },
                        'spamfilter-profile': {
                            'type': 'string'
                        },
                        'srcaddr4': {
                            'type': 'string'
                        },
                        'srcaddr6': {
                            'type': 'string'
                        },
                        'srcintf': {
                            'type': 'string'
                        },
                        'ssh-filter-profile': {
                            'type': 'string'
                        },
                        'ssh-policy-redirect': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
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
                        'tcp-mss-receiver': {
                            'type': 'integer'
                        },
                        'tcp-mss-sender': {
                            'type': 'integer'
                        },
                        'traffic-shaper': {
                            'type': 'string'
                        },
                        'traffic-shaper-reverse': {
                            'type': 'string'
                        },
                        'url-category': {
                            'type': 'array',
                            'items': {
                                'type': 'integer'
                            }
                        },
                        'users': {
                            'type': 'string'
                        },
                        'utm-inspection-mode': {
                            'type': 'string',
                            'enum': [
                                'proxy',
                                'flow'
                            ]
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
                        'voip-profile': {
                            'type': 'string'
                        },
                        'vpntunnel': {
                            'type': 'string'
                        },
                        'waf-profile': {
                            'type': 'string'
                        },
                        'webfilter-profile': {
                            'type': 'string'
                        }
                    },
                    'api_tag': 0
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
                    'name': 'url',
                    'api_tag': 0
                }
            ],
            'object2': [
                {
                    'name': 'option',
                    'type': 'dict',
                    'dict': {
                        'type': 'string',
                        'enum': [
                            'object member',
                            'chksum',
                            'datasrc'
                        ]
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
            'clone': 'object0',
            'delete': 'object1',
            'get': 'object2',
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
                'clone',
                'delete',
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
    module = AnsibleModule(argument_spec=module_arg_spec,
                           supports_check_mode=False)
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
        fmgr.govern_response(module=module, results=response,
                             msg='Operation Finished',
                             ansible_facts=fmgr.construct_ansible_facts(response, module.params, module.params))
    except Exception as e:
        raise FMGBaseException(e)

    module.exit_json(**response[1])


if __name__ == '__main__':
    main()