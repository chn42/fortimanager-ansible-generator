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
module: fmgr_wanopt_profile_mapi
short_description: Enable/disable MAPI email WAN Optimization and configure MAPI WAN Optimization features.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/wanopt/profile/{profile}/mapi
    - /pm/config/global/obj/wanopt/profile/{profile}/mapi
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
            profile:
                type: str
    schema_object0:
        methods: [get]
        description: 'Enable/disable MAPI email WAN Optimization and configure MAPI WAN Optimization features.'
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
    schema_object1:
        methods: [set, update]
        description: 'Enable/disable MAPI email WAN Optimization and configure MAPI WAN Optimization features.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                byte-caching:
                    type: str
                    description: 'Enable/disable byte-caching for HTTP. Byte caching reduces the amount of traffic by caching file data sent across the WAN ...'
                    choices:
                        - 'disable'
                        - 'enable'
                log-traffic:
                    type: str
                    description: 'Enable/disable logging.'
                    choices:
                        - 'disable'
                        - 'enable'
                port:
                    -
                        type: int
                secure-tunnel:
                    type: str
                    description: 'Enable/disable securing the WAN Opt tunnel using SSL. Secure and non-secure tunnels use the same TCP port (7810).'
                    choices:
                        - 'disable'
                        - 'enable'
                status:
                    type: str
                    description: 'Enable/disable HTTP WAN Optimization.'
                    choices:
                        - 'disable'
                        - 'enable'
                tunnel-sharing:
                    type: str
                    description: 'Tunnel sharing mode for aggressive/non-aggressive and/or interactive/non-interactive protocols.'
                    choices:
                        - 'private'
                        - 'shared'
                        - 'express-shared'

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

    - name: REQUESTING /PM/CONFIG/OBJ/WANOPT/PROFILE/{PROFILE}/MAPI
      fmgr_wanopt_profile_mapi:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            profile: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/OBJ/WANOPT/PROFILE/{PROFILE}/MAPI
      fmgr_wanopt_profile_mapi:
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            profile: <value of string>
         params:
            -
               data:
                  byte-caching: <value in [disable, enable]>
                  log-traffic: <value in [disable, enable]>
                  port:
                    - <value of integer>
                  secure-tunnel: <value in [disable, enable]>
                  status: <value in [disable, enable]>
                  tunnel-sharing: <value in [private, shared, express-shared]>

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
            byte-caching:
               type: str
               description: 'Enable/disable byte-caching for HTTP. Byte caching reduces the amount of traffic by caching file data sent across the WAN and i...'
            log-traffic:
               type: str
               description: 'Enable/disable logging.'
            port:
               type: array
               suboptions:
                  type: int
            secure-tunnel:
               type: str
               description: 'Enable/disable securing the WAN Opt tunnel using SSL. Secure and non-secure tunnels use the same TCP port (7810).'
            status:
               type: str
               description: 'Enable/disable HTTP WAN Optimization.'
            tunnel-sharing:
               type: str
               description: 'Tunnel sharing mode for aggressive/non-aggressive and/or interactive/non-interactive protocols.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/wanopt/profile/{profile}/mapi'
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
            example: '/pm/config/adom/{adom}/obj/wanopt/profile/{profile}/mapi'

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
        '/pm/config/adom/{adom}/obj/wanopt/profile/{profile}/mapi',
        '/pm/config/global/obj/wanopt/profile/{profile}/mapi'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'profile',
            'type': 'string'
        }
    ]

    body_schema = {
        'schema_objects': {
            'object0': [
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
            ],
            'object1': [
                {
                    'name': 'data',
                    'type': 'dict',
                    'dict': {
                        'byte-caching': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'log-traffic': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'port': {
                            'type': 'array',
                            'items': {
                                'type': 'integer'
                            }
                        },
                        'secure-tunnel': {
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
                        'tunnel-sharing': {
                            'type': 'string',
                            'enum': [
                                'private',
                                'shared',
                                'express-shared'
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
