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
module: fmgr_firewall_vip64_obj
short_description: Configure IPv6 to IPv4 virtual IPs.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ clone delete get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/firewall/vip64/{vip64}
    - /pm/config/global/obj/firewall/vip64/{vip64}
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
            adom:
                type: str
                description: the domain prefix, the none and global are reserved
                choices:
                  - none
                  - global
                  - custom dom
            vip64:
                type: str
    schema_object0:
        methods: [clone, set, update]
        description: 'Configure IPv6 to IPv4 virtual IPs.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                arp-reply:
                    type: str
                    description: 'Enable ARP reply.'
                    choices:
                        - 'disable'
                        - 'enable'
                color:
                    type: int
                    description: 'Color of icon on the GUI.'
                comment:
                    type: str
                    description: 'Comment.'
                dynamic_mapping:
                    -
                        _scope:
                            -
                                name:
                                    type: str
                                vdom:
                                    type: str
                        arp-reply:
                            type: str
                            choices:
                                - 'disable'
                                - 'enable'
                        color:
                            type: int
                        comment:
                            type: str
                        extip:
                            type: str
                        extport:
                            type: str
                        id:
                            type: int
                        ldb-method:
                            type: str
                            choices:
                                - 'static'
                                - 'round-robin'
                                - 'weighted'
                                - 'least-session'
                                - 'least-rtt'
                                - 'first-alive'
                        mappedip:
                            type: str
                        mappedport:
                            type: str
                        monitor:
                            type: str
                        portforward:
                            type: str
                            choices:
                                - 'disable'
                                - 'enable'
                        protocol:
                            type: str
                            choices:
                                - 'tcp'
                                - 'udp'
                        server-type:
                            type: str
                            choices:
                                - 'http'
                                - 'tcp'
                                - 'udp'
                                - 'ip'
                        src-filter:
                            -
                                type: str
                        type:
                            type: str
                            choices:
                                - 'static-nat'
                                - 'server-load-balance'
                        uuid:
                            type: str
                extip:
                    type: str
                    description: 'Start-external-IP [-end-external-IP].'
                extport:
                    type: str
                    description: 'External service port.'
                id:
                    type: int
                    description: 'Custom defined id.'
                ldb-method:
                    type: str
                    description: 'Load balance method.'
                    choices:
                        - 'static'
                        - 'round-robin'
                        - 'weighted'
                        - 'least-session'
                        - 'least-rtt'
                        - 'first-alive'
                mappedip:
                    type: str
                    description: 'Start-mapped-IP [-end-mapped-IP].'
                mappedport:
                    type: str
                    description: 'Mapped service port.'
                monitor:
                    type: str
                    description: 'Health monitors.'
                name:
                    type: str
                    description: 'VIP64 name.'
                portforward:
                    type: str
                    description: 'Enable port forwarding.'
                    choices:
                        - 'disable'
                        - 'enable'
                protocol:
                    type: str
                    description: 'Mapped port protocol.'
                    choices:
                        - 'tcp'
                        - 'udp'
                realservers:
                    -
                        client-ip:
                            type: str
                            description: 'Restrict server to a client IP in this range.'
                        healthcheck:
                            type: str
                            description: 'Per server health check.'
                            choices:
                                - 'disable'
                                - 'enable'
                                - 'vip'
                        holddown-interval:
                            type: int
                            description: 'Hold down interval.'
                        id:
                            type: int
                            description: 'Real server ID.'
                        ip:
                            type: str
                            description: 'Mapped server IP.'
                        max-connections:
                            type: int
                            description: 'Maximum number of connections allowed to server.'
                        monitor:
                            type: str
                            description: 'Health monitors.'
                        port:
                            type: int
                            description: 'Mapped server port.'
                        status:
                            type: str
                            description: 'Server administrative status.'
                            choices:
                                - 'active'
                                - 'standby'
                                - 'disable'
                        weight:
                            type: int
                server-type:
                    type: str
                    description: 'Server type.'
                    choices:
                        - 'http'
                        - 'tcp'
                        - 'udp'
                        - 'ip'
                src-filter:
                    -
                        type: str
                type:
                    type: str
                    description: 'VIP type: static NAT.'
                    choices:
                        - 'static-nat'
                        - 'server-load-balance'
                uuid:
                    type: str
                    description: 'Universally Unique Identifier (UUID; automatically assigned but can be manually reset).'
    schema_object1:
        methods: [delete]
        description: 'Configure IPv6 to IPv4 virtual IPs.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object2:
        methods: [get]
        description: 'Configure IPv6 to IPv4 virtual IPs.'
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
   collections:
     - fortinet.fortimanager
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/VIP64/{VIP64}
      fmgr_firewall_vip64_obj:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            vip64: <value of string>
         params:
            -
               data:
                  arp-reply: <value in [disable, enable]>
                  color: <value of integer>
                  comment: <value of string>
                  dynamic_mapping:
                    -
                        _scope:
                          -
                              name: <value of string>
                              vdom: <value of string>
                        arp-reply: <value in [disable, enable]>
                        color: <value of integer>
                        comment: <value of string>
                        extip: <value of string>
                        extport: <value of string>
                        id: <value of integer>
                        ldb-method: <value in [static, round-robin, weighted, ...]>
                        mappedip: <value of string>
                        mappedport: <value of string>
                        monitor: <value of string>
                        portforward: <value in [disable, enable]>
                        protocol: <value in [tcp, udp]>
                        server-type: <value in [http, tcp, udp, ...]>
                        src-filter:
                          - <value of string>
                        type: <value in [static-nat, server-load-balance]>
                        uuid: <value of string>
                  extip: <value of string>
                  extport: <value of string>
                  id: <value of integer>
                  ldb-method: <value in [static, round-robin, weighted, ...]>
                  mappedip: <value of string>
                  mappedport: <value of string>
                  monitor: <value of string>
                  name: <value of string>
                  portforward: <value in [disable, enable]>
                  protocol: <value in [tcp, udp]>
                  realservers:
                    -
                        client-ip: <value of string>
                        healthcheck: <value in [disable, enable, vip]>
                        holddown-interval: <value of integer>
                        id: <value of integer>
                        ip: <value of string>
                        max-connections: <value of integer>
                        monitor: <value of string>
                        port: <value of integer>
                        status: <value in [active, standby, disable]>
                        weight: <value of integer>
                  server-type: <value in [http, tcp, udp, ...]>
                  src-filter:
                    - <value of string>
                  type: <value in [static-nat, server-load-balance]>
                  uuid: <value of string>

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/VIP64/{VIP64}
      fmgr_firewall_vip64_obj:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            vip64: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

'''

RETURN = '''
return_of_api_category_0:
   description: items returned for method:[clone, delete, set, update]
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
            example: '/pm/config/adom/{adom}/obj/firewall/vip64/{vip64}'
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            arp-reply:
               type: str
               description: 'Enable ARP reply.'
            color:
               type: int
               description: 'Color of icon on the GUI.'
            comment:
               type: str
               description: 'Comment.'
            dynamic_mapping:
               type: array
               suboptions:
                  _scope:
                     type: array
                     suboptions:
                        name:
                           type: str
                        vdom:
                           type: str
                  arp-reply:
                     type: str
                  color:
                     type: int
                  comment:
                     type: str
                  extip:
                     type: str
                  extport:
                     type: str
                  id:
                     type: int
                  ldb-method:
                     type: str
                  mappedip:
                     type: str
                  mappedport:
                     type: str
                  monitor:
                     type: str
                  portforward:
                     type: str
                  protocol:
                     type: str
                  server-type:
                     type: str
                  src-filter:
                     type: array
                     suboptions:
                        type: str
                  type:
                     type: str
                  uuid:
                     type: str
            extip:
               type: str
               description: 'Start-external-IP [-end-external-IP].'
            extport:
               type: str
               description: 'External service port.'
            id:
               type: int
               description: 'Custom defined id.'
            ldb-method:
               type: str
               description: 'Load balance method.'
            mappedip:
               type: str
               description: 'Start-mapped-IP [-end-mapped-IP].'
            mappedport:
               type: str
               description: 'Mapped service port.'
            monitor:
               type: str
               description: 'Health monitors.'
            name:
               type: str
               description: 'VIP64 name.'
            portforward:
               type: str
               description: 'Enable port forwarding.'
            protocol:
               type: str
               description: 'Mapped port protocol.'
            realservers:
               type: array
               suboptions:
                  client-ip:
                     type: str
                     description: 'Restrict server to a client IP in this range.'
                  healthcheck:
                     type: str
                     description: 'Per server health check.'
                  holddown-interval:
                     type: int
                     description: 'Hold down interval.'
                  id:
                     type: int
                     description: 'Real server ID.'
                  ip:
                     type: str
                     description: 'Mapped server IP.'
                  max-connections:
                     type: int
                     description: 'Maximum number of connections allowed to server.'
                  monitor:
                     type: str
                     description: 'Health monitors.'
                  port:
                     type: int
                     description: 'Mapped server port.'
                  status:
                     type: str
                     description: 'Server administrative status.'
                  weight:
                     type: int
            server-type:
               type: str
               description: 'Server type.'
            src-filter:
               type: array
               suboptions:
                  type: str
            type:
               type: str
               description: 'VIP type: static NAT.'
            uuid:
               type: str
               description: 'Universally Unique Identifier (UUID; automatically assigned but can be manually reset).'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/firewall/vip64/{vip64}'

'''
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from ansible_collections.fortinet.fortimanager.plugins.module_utils.common import FAIL_SOCKET_MSG
from ansible_collections.fortinet.fortimanager.plugins.module_utils.common import DEFAULT_RESULT_OBJ
from ansible_collections.fortinet.fortimanager.plugins.module_utils.common import FMGRCommon
from ansible_collections.fortinet.fortimanager.plugins.module_utils.common import FMGBaseException
from ansible_collections.fortinet.fortimanager.plugins.module_utils.fortimanager import FortiManagerHandler


def main():
    jrpc_urls = [
        '/pm/config/adom/{adom}/obj/firewall/vip64/{vip64}',
        '/pm/config/global/obj/firewall/vip64/{vip64}'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'vip64',
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
                        'arp-reply': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'color': {
                            'type': 'integer'
                        },
                        'comment': {
                            'type': 'string'
                        },
                        'dynamic_mapping': {
                            'type': 'array',
                            'items': {
                                '_scope': {
                                    'type': 'array',
                                    'items': {
                                        'name': {
                                            'type': 'string'
                                        },
                                        'vdom': {
                                            'type': 'string'
                                        }
                                    }
                                },
                                'arp-reply': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'color': {
                                    'type': 'integer'
                                },
                                'comment': {
                                    'type': 'string'
                                },
                                'extip': {
                                    'type': 'string'
                                },
                                'extport': {
                                    'type': 'string'
                                },
                                'id': {
                                    'type': 'integer'
                                },
                                'ldb-method': {
                                    'type': 'string',
                                    'enum': [
                                        'static',
                                        'round-robin',
                                        'weighted',
                                        'least-session',
                                        'least-rtt',
                                        'first-alive'
                                    ]
                                },
                                'mappedip': {
                                    'type': 'string'
                                },
                                'mappedport': {
                                    'type': 'string'
                                },
                                'monitor': {
                                    'type': 'string'
                                },
                                'portforward': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'protocol': {
                                    'type': 'string',
                                    'enum': [
                                        'tcp',
                                        'udp'
                                    ]
                                },
                                'server-type': {
                                    'type': 'string',
                                    'enum': [
                                        'http',
                                        'tcp',
                                        'udp',
                                        'ip'
                                    ]
                                },
                                'src-filter': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'string'
                                    }
                                },
                                'type': {
                                    'type': 'string',
                                    'enum': [
                                        'static-nat',
                                        'server-load-balance'
                                    ]
                                },
                                'uuid': {
                                    'type': 'string'
                                }
                            }
                        },
                        'extip': {
                            'type': 'string'
                        },
                        'extport': {
                            'type': 'string'
                        },
                        'id': {
                            'type': 'integer'
                        },
                        'ldb-method': {
                            'type': 'string',
                            'enum': [
                                'static',
                                'round-robin',
                                'weighted',
                                'least-session',
                                'least-rtt',
                                'first-alive'
                            ]
                        },
                        'mappedip': {
                            'type': 'string'
                        },
                        'mappedport': {
                            'type': 'string'
                        },
                        'monitor': {
                            'type': 'string'
                        },
                        'name': {
                            'type': 'string'
                        },
                        'portforward': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'protocol': {
                            'type': 'string',
                            'enum': [
                                'tcp',
                                'udp'
                            ]
                        },
                        'realservers': {
                            'type': 'array',
                            'items': {
                                'client-ip': {
                                    'type': 'string'
                                },
                                'healthcheck': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable',
                                        'vip'
                                    ]
                                },
                                'holddown-interval': {
                                    'type': 'integer'
                                },
                                'id': {
                                    'type': 'integer'
                                },
                                'ip': {
                                    'type': 'string'
                                },
                                'max-connections': {
                                    'type': 'integer'
                                },
                                'monitor': {
                                    'type': 'string'
                                },
                                'port': {
                                    'type': 'integer'
                                },
                                'status': {
                                    'type': 'string',
                                    'enum': [
                                        'active',
                                        'standby',
                                        'disable'
                                    ]
                                },
                                'weight': {
                                    'type': 'integer'
                                }
                            }
                        },
                        'server-type': {
                            'type': 'string',
                            'enum': [
                                'http',
                                'tcp',
                                'udp',
                                'ip'
                            ]
                        },
                        'src-filter': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'type': {
                            'type': 'string',
                            'enum': [
                                'static-nat',
                                'server-load-balance'
                            ]
                        },
                        'uuid': {
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
        'loose_validation': {
            'type': 'bool',
            'required': False,
            'default': False
        },
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
    loose_validation = module.params['loose_validation']

    fmgr = None
    payload = None
    response = DEFAULT_RESULT_OBJ

    if module._socket_path:
        connection = Connection(module._socket_path)
        tools = FMGRCommon()
        if loose_validation == False:
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

    module.exit_json(meta=response[1])


if __name__ == '__main__':
    main()
