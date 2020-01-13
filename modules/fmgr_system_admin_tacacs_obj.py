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
module: fmgr_system_admin_tacacs_obj
short_description: TACACS+ server entry configuration.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ delete get set update ] the following apis.
    - /cli/global/system/admin/tacacs/{tacacs}
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
            tacacs:
                type: str
    schema_object0:
        methods: [delete, get]
        description: 'TACACS+ server entry configuration.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object1:
        methods: [set, update]
        description: 'TACACS+ server entry configuration.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                authen-type:
                    type: str
                    default: 'auto'
                    description:
                     - 'Authentication type.'
                     - 'auto - Use PAP, MSCHAP, and CHAP (in that order).'
                     - 'ascii - ASCII.'
                     - 'pap - PAP.'
                     - 'chap - CHAP.'
                     - 'mschap - MSCHAP.'
                    choices:
                        - 'auto'
                        - 'ascii'
                        - 'pap'
                        - 'chap'
                        - 'mschap'
                authorization:
                    type: str
                    default: 'disable'
                    description:
                     - 'Enable/disable TACACS+ authorization.'
                     - 'disable - Disable TACACS+ authorization.'
                     - 'enable - Enable TACACS+ authorization (service = fortigate).'
                    choices:
                        - 'disable'
                        - 'enable'
                key:
                    -
                        type: str
                        default: 'ENC MTM1NzgxNTEwMTQ3MzkyN6Bf+SUc1DH38ALtjfXS+4tsPEStofpzICCe9zH2nI/U1uDRuS4ysXoRMhkM/i6ypV7BvpqVqu3wnaI3lWsFOh6+06ydV9EyG...'
                name:
                    type: str
                    description: 'TACACS+ server entry name.'
                port:
                    type: int
                    default: 49
                    description: 'Port number of TACACS+ server.'
                secondary-key:
                    -
                        type: str
                        default: 'ENC MTM3MzM0NTI4MzQ3MTQ4OftOEtzg8U8bz+L2zW2yOkzO1vkOesoOkTy2j02IrPnwTVEVz7aOODvx+zGMUtELHdsY22GW20r4Q0OasjCqkmZgjt9PbfLA2...'
                secondary-server:
                    type: str
                    description: '{<name_str|ip_str>} secondary server domain name or IP.'
                server:
                    type: str
                    description: '{<name_str|ip_str>} server domain name or IP.'
                tertiary-key:
                    -
                        type: str
                        default: 'ENC MjAzNTE3MDIwNDI1OTEwMgAtMeOT5CzyMlsFCmOGJ8cTlQYpjv7BJI+uC5QN2LxVGteUJ87W++EYhPaChx42doThcM3Gtb7w8PfrihahuU7S+qoi9weI6...'
                tertiary-server:
                    type: str
                    description: '{<name_str|ip_str>} tertiary server domain name or IP.'

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /CLI/SYSTEM/ADMIN/TACACS/{TACACS}
      fmgr_system_admin_tacacs_obj:
         method: <value in [set, update]>
         url_params:
            tacacs: <value of string>
         params:
            -
               data:
                  authen-type: <value in [auto, ascii, pap, ...] default: 'auto'>
                  authorization: <value in [disable, enable] default: 'disable'>
                  key:
                    - <value of string default: 'ENC MTM1NzgxNTEwMTQ3MzkyN6Bf+SUc1DH38ALtjfXS+4tsPEStofpzICCe9zH2nI/U1uDRuS4y...'>
                  name: <value of string>
                  port: <value of integer default: 49>
                  secondary-key:
                    - <value of string default: 'ENC MTM3MzM0NTI4MzQ3MTQ4OftOEtzg8U8bz+L2zW2yOkzO1vkOesoOkTy2j02IrPnwTVEVz7aO...'>
                  secondary-server: <value of string>
                  server: <value of string>
                  tertiary-key:
                    - <value of string default: 'ENC MjAzNTE3MDIwNDI1OTEwMgAtMeOT5CzyMlsFCmOGJ8cTlQYpjv7BJI+uC5QN2LxVGteUJ87W...'>
                  tertiary-server: <value of string>

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
            example: '/cli/global/system/admin/tacacs/{tacacs}'
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            authen-type:
               type: str
               description: |
                  'Authentication type.'
                  'auto - Use PAP, MSCHAP, and CHAP (in that order).'
                  'ascii - ASCII.'
                  'pap - PAP.'
                  'chap - CHAP.'
                  'mschap - MSCHAP.'
               example: 'auto'
            authorization:
               type: str
               description: |
                  'Enable/disable TACACS+ authorization.'
                  'disable - Disable TACACS+ authorization.'
                  'enable - Enable TACACS+ authorization (service = fortigate).'
               example: 'disable'
            key:
               type: array
               suboptions:
                  type: str
                  example: 'ENC MTM1NzgxNTEwMTQ3MzkyN6Bf+SUc1DH38ALtjfXS+4tsPEStofpzICCe9zH2nI/U1uDRuS4y...'
            name:
               type: str
               description: 'TACACS+ server entry name.'
            port:
               type: int
               description: 'Port number of TACACS+ server.'
               example: 49
            secondary-key:
               type: array
               suboptions:
                  type: str
                  example: 'ENC MTM3MzM0NTI4MzQ3MTQ4OftOEtzg8U8bz+L2zW2yOkzO1vkOesoOkTy2j02IrPnwTVEVz7aO...'
            secondary-server:
               type: str
               description: '{<name_str|ip_str>} secondary server domain name or IP.'
            server:
               type: str
               description: '{<name_str|ip_str>} server domain name or IP.'
            tertiary-key:
               type: array
               suboptions:
                  type: str
                  example: 'ENC MjAzNTE3MDIwNDI1OTEwMgAtMeOT5CzyMlsFCmOGJ8cTlQYpjv7BJI+uC5QN2LxVGteUJ87W...'
            tertiary-server:
               type: str
               description: '{<name_str|ip_str>} tertiary server domain name or IP.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/cli/global/system/admin/tacacs/{tacacs}'

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
        '/cli/global/system/admin/tacacs/{tacacs}'
    ]

    url_schema = [
        {
            'name': 'tacacs',
            'type': 'string'
        }
    ]

    body_schema = {
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
                    'name': 'data',
                    'type': 'dict',
                    'dict': {
                        'authen-type': {
                            'type': 'string',
                            'enum': [
                                'auto',
                                'ascii',
                                'pap',
                                'chap',
                                'mschap'
                            ]
                        },
                        'authorization': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'key': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'name': {
                            'type': 'string'
                        },
                        'port': {
                            'type': 'integer',
                            'default': 49,
                            'example': 49
                        },
                        'secondary-key': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'secondary-server': {
                            'type': 'string'
                        },
                        'server': {
                            'type': 'string'
                        },
                        'tertiary-key': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'tertiary-server': {
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
            ]
        },
        'method_mapping': {
            'delete': 'object0',
            'get': 'object0',
            'set': 'object1',
            'update': 'object1'
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