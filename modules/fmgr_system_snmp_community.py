#!/usr/bin/python
from __future__ import absolute_import, division, print_function
# Copyright 2019-2020 Fortinet, Inc.
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
module: fmgr_system_snmp_community
short_description: SNMP community configuration.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ add get set update ] the following apis.
    - /cli/global/system/snmp/community
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
    schema_object0:
        methods: [add, set, update]
        description: 'SNMP community configuration.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                -
                    events:
                        -
                            type: str
                            choices:
                                - 'disk_low'
                                - 'ha_switch'
                                - 'intf_ip_chg'
                                - 'sys_reboot'
                                - 'cpu_high'
                                - 'mem_low'
                                - 'log-alert'
                                - 'log-rate'
                                - 'log-data-rate'
                                - 'lic-gbday'
                                - 'lic-dev-quota'
                                - 'cpu-high-exclude-nice'
                    hosts:
                        -
                            id:
                                type: int
                                default: 0
                                description: 'Host entry ID.'
                            interface:
                                type: str
                                description: 'Allow interface name.'
                            ip:
                                type: str
                                default: '0.0.0.0 0.0.0.0'
                                description: 'Allow host IP address.'
                    hosts6:
                        -
                            id:
                                type: int
                                default: 0
                                description: 'Host entry ID.'
                            interface:
                                type: str
                                description: 'Allow interface name.'
                            ip:
                                type: str
                                default: '::/0'
                                description: 'Allow host IP address.'
                    id:
                        type: int
                        default: 0
                        description: 'Community ID.'
                    name:
                        type: str
                        description: 'Community name.'
                    query_v1_port:
                        type: int
                        default: 161
                        description: 'SNMP v1 query port.'
                    query_v1_status:
                        type: str
                        default: 'enable'
                        description:
                         - 'Enable/disable SNMP v1 query.'
                         - 'disable - Disable setting.'
                         - 'enable - Enable setting.'
                        choices:
                            - 'disable'
                            - 'enable'
                    query_v2c_port:
                        type: int
                        default: 161
                        description: 'SNMP v2c query port.'
                    query_v2c_status:
                        type: str
                        default: 'enable'
                        description:
                         - 'Enable/disable SNMP v2c query.'
                         - 'disable - Disable setting.'
                         - 'enable - Enable setting.'
                        choices:
                            - 'disable'
                            - 'enable'
                    status:
                        type: str
                        default: 'enable'
                        description:
                         - 'Enable/disable community.'
                         - 'disable - Disable setting.'
                         - 'enable - Enable setting.'
                        choices:
                            - 'disable'
                            - 'enable'
                    trap_v1_rport:
                        type: int
                        default: 162
                        description: 'SNMP v1 trap remote port.'
                    trap_v1_status:
                        type: str
                        default: 'enable'
                        description:
                         - 'Enable/disable SNMP v1 trap.'
                         - 'disable - Disable setting.'
                         - 'enable - Enable setting.'
                        choices:
                            - 'disable'
                            - 'enable'
                    trap_v2c_rport:
                        type: int
                        default: 162
                        description: 'SNMP v2c trap remote port.'
                    trap_v2c_status:
                        type: str
                        default: 'enable'
                        description:
                         - 'Enable/disable SNMP v2c trap.'
                         - 'disable - Disable setting.'
                         - 'enable - Enable setting.'
                        choices:
                            - 'disable'
                            - 'enable'
    schema_object1:
        methods: [get]
        description: 'SNMP community configuration.'
        api_categories: [api_tag0]
        api_tag0:
            fields:
                -
                    -
                        type: str
                        choices:
                            - 'events'
                            - 'id'
                            - 'name'
                            - 'query_v1_port'
                            - 'query_v1_status'
                            - 'query_v2c_port'
                            - 'query_v2c_status'
                            - 'status'
                            - 'trap_v1_rport'
                            - 'trap_v1_status'
                            - 'trap_v2c_rport'
                            - 'trap_v2c_status'
            filter:
                -
                    type: str
            loadsub:
                type: int
                description: 'Enable or disable the return of any sub-objects. If not specified, the default is to return all sub-objects.'
            option:
                type: str
                description:
                 - 'Set fetch option for the request. If no option is specified, by default the attributes of the objects will be returned.'
                 - 'count - Return the number of matching entries instead of the actual entry data.'
                 - 'syntax - Return the attribute syntax of a table or an object, instead of the actual entry data. All filter parameters will be ignored.'
                choices:
                    - 'count'
                    - 'syntax'

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /CLI/SYSTEM/SNMP/COMMUNITY
      fmgr_system_snmp_community:
         method: <value in [add, set, update]>
         params:
            -
               data:
                 -
                     events:
                       - <value in [disk_low, ha_switch, intf_ip_chg, ...]>
                     hosts:
                       -
                           id: <value of integer default: 0>
                           interface: <value of string>
                           ip: <value of string default: '0.0.0.0 0.0.0.0'>
                     hosts6:
                       -
                           id: <value of integer default: 0>
                           interface: <value of string>
                           ip: <value of string default: '::/0'>
                     id: <value of integer default: 0>
                     name: <value of string>
                     query_v1_port: <value of integer default: 161>
                     query_v1_status: <value in [disable, enable] default: 'enable'>
                     query_v2c_port: <value of integer default: 161>
                     query_v2c_status: <value in [disable, enable] default: 'enable'>
                     status: <value in [disable, enable] default: 'enable'>
                     trap_v1_rport: <value of integer default: 162>
                     trap_v1_status: <value in [disable, enable] default: 'enable'>
                     trap_v2c_rport: <value of integer default: 162>
                     trap_v2c_status: <value in [disable, enable] default: 'enable'>

    - name: REQUESTING /CLI/SYSTEM/SNMP/COMMUNITY
      fmgr_system_snmp_community:
         method: <value in [get]>
         params:
            -
               fields:
                 -
                    - <value in [events, id, name, ...]>
               filter:
                 - <value of string>
               loadsub: <value of integer>
               option: <value in [count, syntax]>

'''

RETURN = '''
return_of_api_category_0:
   description: items returned for method:[add, set, update]
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
            example: '/cli/global/system/snmp/community'
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
               events:
                  type: array
                  suboptions:
                     type: str
               hosts:
                  type: array
                  suboptions:
                     id:
                        type: int
                        description: 'Host entry ID.'
                        example: 0
                     interface:
                        type: str
                        description: 'Allow interface name.'
                     ip:
                        type: str
                        description: 'Allow host IP address.'
                        example: '0.0.0.0 0.0.0.0'
               hosts6:
                  type: array
                  suboptions:
                     id:
                        type: int
                        description: 'Host entry ID.'
                        example: 0
                     interface:
                        type: str
                        description: 'Allow interface name.'
                     ip:
                        type: str
                        description: 'Allow host IP address.'
                        example: '::/0'
               id:
                  type: int
                  description: 'Community ID.'
                  example: 0
               name:
                  type: str
                  description: 'Community name.'
               query_v1_port:
                  type: int
                  description: 'SNMP v1 query port.'
                  example: 161
               query_v1_status:
                  type: str
                  description: |
                     'Enable/disable SNMP v1 query.'
                     'disable - Disable setting.'
                     'enable - Enable setting.'
                  example: 'enable'
               query_v2c_port:
                  type: int
                  description: 'SNMP v2c query port.'
                  example: 161
               query_v2c_status:
                  type: str
                  description: |
                     'Enable/disable SNMP v2c query.'
                     'disable - Disable setting.'
                     'enable - Enable setting.'
                  example: 'enable'
               status:
                  type: str
                  description: |
                     'Enable/disable community.'
                     'disable - Disable setting.'
                     'enable - Enable setting.'
                  example: 'enable'
               trap_v1_rport:
                  type: int
                  description: 'SNMP v1 trap remote port.'
                  example: 162
               trap_v1_status:
                  type: str
                  description: |
                     'Enable/disable SNMP v1 trap.'
                     'disable - Disable setting.'
                     'enable - Enable setting.'
                  example: 'enable'
               trap_v2c_rport:
                  type: int
                  description: 'SNMP v2c trap remote port.'
                  example: 162
               trap_v2c_status:
                  type: str
                  description: |
                     'Enable/disable SNMP v2c trap.'
                     'disable - Disable setting.'
                     'enable - Enable setting.'
                  example: 'enable'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/cli/global/system/snmp/community'

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
        '/cli/global/system/snmp/community'
    ]

    url_schema = [
    ]

    body_schema = {
        'schema_objects': {
            'object0': [
                {
                    'name': 'data',
                    'api_tag': 0,
                    'type': 'array',
                    'items': {
                        'events': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'disk_low',
                                    'ha_switch',
                                    'intf_ip_chg',
                                    'sys_reboot',
                                    'cpu_high',
                                    'mem_low',
                                    'log-alert',
                                    'log-rate',
                                    'log-data-rate',
                                    'lic-gbday',
                                    'lic-dev-quota',
                                    'cpu-high-exclude-nice'
                                ]
                            }
                        },
                        'hosts': {
                            'type': 'array',
                            'items': {
                                'id': {
                                    'type': 'integer',
                                    'default': 0,
                                    'example': 0
                                },
                                'interface': {
                                    'type': 'string'
                                },
                                'ip': {
                                    'type': 'string'
                                }
                            }
                        },
                        'hosts6': {
                            'type': 'array',
                            'items': {
                                'id': {
                                    'type': 'integer',
                                    'default': 0,
                                    'example': 0
                                },
                                'interface': {
                                    'type': 'string'
                                },
                                'ip': {
                                    'type': 'string'
                                }
                            }
                        },
                        'id': {
                            'type': 'integer',
                            'default': 0,
                            'example': 0
                        },
                        'name': {
                            'type': 'string'
                        },
                        'query_v1_port': {
                            'type': 'integer',
                            'default': 161,
                            'example': 161
                        },
                        'query_v1_status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'query_v2c_port': {
                            'type': 'integer',
                            'default': 161,
                            'example': 161
                        },
                        'query_v2c_status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'trap_v1_rport': {
                            'type': 'integer',
                            'default': 162,
                            'example': 162
                        },
                        'trap_v1_status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'trap_v2c_rport': {
                            'type': 'integer',
                            'default': 162,
                            'example': 162
                        },
                        'trap_v2c_status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
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
                    'name': 'fields',
                    'api_tag': 0,
                    'type': 'array',
                    'items': {
                        'type': 'array',
                        'items': {
                            'type': 'string',
                            'enum': [
                                'events',
                                'id',
                                'name',
                                'query_v1_port',
                                'query_v1_status',
                                'query_v2c_port',
                                'query_v2c_status',
                                'status',
                                'trap_v1_rport',
                                'trap_v1_status',
                                'trap_v2c_rport',
                                'trap_v2c_status'
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
                            'syntax'
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