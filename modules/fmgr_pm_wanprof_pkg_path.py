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
module: fmgr_pm_wanprof_pkg_path
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ delete get set update ] the following apis:
    - /pm/wanprof/adom/{adom}/{pkg_path}
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
            pkg_path:
                type: str
    schema_object0:
        methods: [delete]
        description: ''
        api_categories: [api_tag0]
        api_tag0:
    schema_object1:
        methods: [get]
        description: ''
        api_categories: [api_tag0]
        api_tag0:
            fields:
                -
                    -
                        type: str
                        choices:
                            - description
                            - name
                            - oid
                            - scope member
                            - type
    schema_object2:
        methods: [set, update]
        description: ''
        api_categories: [api_tag0]
        api_tag0:
            data:
                description:
                    type: str
                name:
                    type: str
                oid:
                    type: int
                scope member:
                    -
                        name:
                            type: str
                        vdom:
                            type: str
                type:
                    type: str
                    choices:
                        - wanprof

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:
    - name: send request to /pm/wanprof/{pkg_path}
      fmgr_pm_wanprof_pkg_path:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            pkg_path: <value of string>
         params:
            - 
               fields: 
                - 
                   - <value in [description, name, oid, ...]>
    - name: send request to /pm/wanprof/{pkg_path}
      fmgr_pm_wanprof_pkg_path:
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            pkg_path: <value of string>
         params:
            - 
               data: 
                  description: <value of string>
                  name: <value of string>
                  oid: <value of integer>
                  scope member: 
                   - 
                        name: <value of string>
                        vdom: <value of string>
                  type: <value in [wanprof]>

'''

RETURN = '''
return_of_api_category_0:
   description: items returned for method:[delete, set, update]
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
            example: /pm/wanprof/adom/{adom}/{pkg_path}
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            description:
               type: str
            name:
               type: str
            oid:
               type: int
            scope member:
               type: array
               suboptions:
                  name:
                     type: str
                  vdom:
                     type: str
            type:
               type: str
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: /pm/wanprof/adom/{adom}/{pkg_path}

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
        '/pm/wanprof/adom/{adom}/{pkg_path}'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'pkg_path',
            'type': 'string'
        }
    ]

    body_schema =  {
        'schema_objects': {
            'object0': [
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
                                'description',
                                'name',
                                'oid',
                                'scope member',
                                'type'
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
            'object2': [
                {
                    'name': 'data',
                    'type': 'dict',
                    'dict': {
                        'description': {
                            'type': 'string'
                        },
                        'name': {
                            'type': 'string'
                        },
                        'oid': {
                            'type': 'integer'
                        },
                        'scope member': {
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
                        'type': {
                            'type': 'string',
                            'enum': [
                                'wanprof'
                            ]
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
            'delete': 'object0',
            'get': 'object1',
            'set': 'object2',
            'update': 'object2'
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