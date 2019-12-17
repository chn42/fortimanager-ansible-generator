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
module: fmgr_cli_system_password_policy
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ get set update ] the following apis:
    - /cli/global/system/password-policy
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
    schema_object0:
        methods: [get]
        description: 'Password policy.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object1:
        methods: [set, update]
        description: 'Password policy.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                change-4-characters:
                    type: str
                    default: disable
                    description:
                     - 'Enable/disable changing at least 4 characters for new password.'
                     - 'disable - Disable changing at least 4 characters for new password.'
                     - 'enable - Enable changing at least 4 characters for new password.'
                    choices:
                        - disable
                        - enable
                expire:
                    type: int
                    default: 0
                    description: 'Number of days after which admin users' password will expire (0 - 3650, 0 = never expire).'
                minimum-length:
                    type: int
                    default: 8
                    description: 'Minimum password length.'
                must-contain:
                    -
                        type: str
                        choices:
                            - upper-case-letter
                            - lower-case-letter
                            - number
                            - non-alphanumeric
                status:
                    type: str
                    default: disable
                    description:
                     - 'Enable/disable password policy.'
                     - 'disable - Disable password policy.'
                     - 'enable - Enable password policy.'
                    choices:
                        - disable
                        - enable

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:
    - name: send request to /cli/system/password-policy
      fmgr_cli_system_password_policy:
         method: <value in [set, update]>
         params:
            - 
               data: 
                  change-4-characters: <value in [disable, enable] default: disable>
                  expire: <value of integer default: 0>
                  minimum-length: <value of integer default: 8>
                  must-contain: 
                   - <value in [upper-case-letter, lower-case-letter, number, ...]>
                  status: <value in [disable, enable] default: disable>

'''

RETURN = '''
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            change-4-characters:
               type: str
               description: |
                  'Enable/disable changing at least 4 characters for new password.'
                  'disable - Disable changing at least 4 characters for new password.'
                  'enable - Enable changing at least 4 characters for new password.'
               example: disable
            expire:
               type: int
               description: 'Number of days after which admin users' password will expire (0 - 3650, 0 = never expire).'
               example: 0
            minimum-length:
               type: int
               description: 'Minimum password length.'
               example: 8
            must-contain:
               type: array
               suboptions:
                  type: str
            status:
               type: str
               description: |
                  'Enable/disable password policy.'
                  'disable - Disable password policy.'
                  'enable - Enable password policy.'
               example: disable
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: /cli/global/system/password-policy
return_of_api_category_0:
   description: items returned for method:[set, update]
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
            example: /cli/global/system/password-policy

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
        '/cli/global/system/password-policy'
    ]

    url_schema = [
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
                    'name': 'data',
                    'type': 'dict',
                    'dict': {
                        'change-4-characters': {
                            'type': 'string',
                            'default': 'disable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'expire': {
                            'type': 'integer',
                            'default': 0,
                            'example': 0
                        },
                        'minimum-length': {
                            'type': 'integer',
                            'default': 8,
                            'example': 8
                        },
                        'must-contain': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'upper-case-letter',
                                    'lower-case-letter',
                                    'number',
                                    'non-alphanumeric'
                                ]
                            }
                        },
                        'status': {
                            'type': 'string',
                            'default': 'disable',
                            'enum': [
                                'disable',
                                'enable'
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