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
module: fmgr_pm_config_obj_spamfilter_iptrust
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ add get set update ] the following apis:
    - /pm/config/adom/{adom}/obj/spamfilter/iptrust
    - /pm/config/global/obj/spamfilter/iptrust
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
    schema_object0:
        methods: [add, set, update]
        description: 'Configure AntiSpam IP trust.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                -
                    comment:
                        type: str
                        description: 'Optional comments.'
                    entries:
                        -
                            addr-type:
                                type: str
                                description: 'Type of address.'
                                choices:
                                    - ipv4
                                    - ipv6
                            id:
                                type: int
                                description: 'Trusted IP entry ID.'
                            ip4-subnet:
                                type: str
                                description: 'IPv4 network address or network address/subnet mask bits.'
                            ip6-subnet:
                                type: str
                                description: 'IPv6 network address/subnet mask bits.'
                            status:
                                type: str
                                description: 'Enable/disable status.'
                                choices:
                                    - disable
                                    - enable
                    id:
                        type: int
                        description: 'ID.'
                    name:
                        type: str
                        description: 'Name of table.'
    schema_object1:
        methods: [get]
        description: 'Configure AntiSpam IP trust.'
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
                            - comment
                            - id
                            - name
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
    - name: send request to /pm/config/obj/spamfilter/iptrust
      fmgr_pm_config_obj_spamfilter_iptrust:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            - 
               data: 
                - 
                     comment: <value of string>
                     entries: 
                      - 
                           addr-type: <value in [ipv4, ipv6]>
                           id: <value of integer>
                           ip4-subnet: <value of string>
                           ip6-subnet: <value of string>
                           status: <value in [disable, enable]>
                     id: <value of integer>
                     name: <value of string>
    - name: send request to /pm/config/obj/spamfilter/iptrust
      fmgr_pm_config_obj_spamfilter_iptrust:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            - 
               attr: <value of string>
               fields: 
                - 
                   - <value in [comment, id, name]>
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
               id:
                  type: int
                  description: 'ID.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: /pm/config/adom/{adom}/obj/spamfilter/iptrust
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
               comment:
                  type: str
                  description: 'Optional comments.'
               entries:
                  type: array
                  suboptions:
                     addr-type:
                        type: str
                        description: 'Type of address.'
                     id:
                        type: int
                        description: 'Trusted IP entry ID.'
                     ip4-subnet:
                        type: str
                        description: 'IPv4 network address or network address/subnet mask bits.'
                     ip6-subnet:
                        type: str
                        description: 'IPv6 network address/subnet mask bits.'
                     status:
                        type: str
                        description: 'Enable/disable status.'
               id:
                  type: int
                  description: 'ID.'
               name:
                  type: str
                  description: 'Name of table.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: /pm/config/adom/{adom}/obj/spamfilter/iptrust

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
        '/pm/config/adom/{adom}/obj/spamfilter/iptrust',
        '/pm/config/global/obj/spamfilter/iptrust'
    ]

    url_schema = [
        {
            'name': 'adom',
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
                        'comment': {
                            'type': 'string'
                        },
                        'entries': {
                            'type': 'array',
                            'items': {
                                'addr-type': {
                                    'type': 'string',
                                    'enum': [
                                        'ipv4',
                                        'ipv6'
                                    ]
                                },
                                'id': {
                                    'type': 'integer'
                                },
                                'ip4-subnet': {
                                    'type': 'string'
                                },
                                'ip6-subnet': {
                                    'type': 'string'
                                },
                                'status': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                }
                            }
                        },
                        'id': {
                            'type': 'integer'
                        },
                        'name': {
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
                                'comment',
                                'id',
                                'name'
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