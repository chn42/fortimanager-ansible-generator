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
module: fmgr_pm_config_obj_spamfilter_bwl_entries_per_object
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ clone delete get move set update ] the following apis.
    - /pm/config/adom/{adom}/obj/spamfilter/bwl/{bwl}/entries/{entries}
    - /pm/config/global/obj/spamfilter/bwl/{bwl}/entries/{entries}
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
            bwl:
                type: str
            entries:
                type: str
    schema_object0:
        methods: [clone, set, update]
        description: 'Anti-spam black/white list entries.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                action:
                    type: str
                    description: 'Reject, mark as spam or good email.'
                    choices:
                        - 'spam'
                        - 'clear'
                        - 'reject'
                addr-type:
                    type: str
                    description: 'IP address type.'
                    choices:
                        - 'ipv4'
                        - 'ipv6'
                email-pattern:
                    type: str
                    description: 'Email address pattern.'
                id:
                    type: int
                    description: 'Entry ID.'
                ip4-subnet:
                    type: str
                    description: 'IPv4 network address/subnet mask bits.'
                ip6-subnet:
                    type: str
                    description: 'IPv6 network address/subnet mask bits.'
                pattern-type:
                    type: str
                    description: 'Wildcard pattern or regular expression.'
                    choices:
                        - 'wildcard'
                        - 'regexp'
                status:
                    type: str
                    description: 'Enable/disable status.'
                    choices:
                        - 'disable'
                        - 'enable'
                type:
                    type: str
                    description: 'Entry type.'
                    choices:
                        - 'ip'
                        - 'email'
    schema_object1:
        methods: [delete]
        description: 'Anti-spam black/white list entries.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object2:
        methods: [get]
        description: 'Anti-spam black/white list entries.'
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
    schema_object3:
        methods: [move]
        description: 'Anti-spam black/white list entries.'
        api_categories: [api_tag0]
        api_tag0:
            option:
                type: str
                choices:
                    - 'before'
                    - 'after'
            target:
                type: str
                description: 'Key to the target entry.'

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /PM/CONFIG/OBJ/SPAMFILTER/BWL/{BWL}/ENTRIES/{ENTRIES}
      fmgr_pm_config_obj_spamfilter_bwl_entries_per_object:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            bwl: <value of string>
            entries: <value of string>
         params:
            -
               data:
                  action: <value in [spam, clear, reject]>
                  addr-type: <value in [ipv4, ipv6]>
                  email-pattern: <value of string>
                  id: <value of integer>
                  ip4-subnet: <value of string>
                  ip6-subnet: <value of string>
                  pattern-type: <value in [wildcard, regexp]>
                  status: <value in [disable, enable]>
                  type: <value in [ip, email]>

    - name: REQUESTING /PM/CONFIG/OBJ/SPAMFILTER/BWL/{BWL}/ENTRIES/{ENTRIES}
      fmgr_pm_config_obj_spamfilter_bwl_entries_per_object:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            bwl: <value of string>
            entries: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/OBJ/SPAMFILTER/BWL/{BWL}/ENTRIES/{ENTRIES}
      fmgr_pm_config_obj_spamfilter_bwl_entries_per_object:
         method: <value in [move]>
         url_params:
            adom: <value in [none, global, custom dom]>
            bwl: <value of string>
            entries: <value of string>
         params:
            -
               option: <value in [before, after]>
               target: <value of string>

'''

RETURN = '''
return_of_api_category_0:
   description: items returned for method:[clone, move, set, update]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            id:
               type: int
               description: 'Entry ID.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/spamfilter/bwl/{bwl}/entries/{entries}'
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
            example: '/pm/config/adom/{adom}/obj/spamfilter/bwl/{bwl}/entries/{entries}'
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
               description: 'Reject, mark as spam or good email.'
            addr-type:
               type: str
               description: 'IP address type.'
            email-pattern:
               type: str
               description: 'Email address pattern.'
            id:
               type: int
               description: 'Entry ID.'
            ip4-subnet:
               type: str
               description: 'IPv4 network address/subnet mask bits.'
            ip6-subnet:
               type: str
               description: 'IPv6 network address/subnet mask bits.'
            pattern-type:
               type: str
               description: 'Wildcard pattern or regular expression.'
            status:
               type: str
               description: 'Enable/disable status.'
            type:
               type: str
               description: 'Entry type.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/spamfilter/bwl/{bwl}/entries/{entries}'

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
        '/pm/config/adom/{adom}/obj/spamfilter/bwl/{bwl}/entries/{entries}',
        '/pm/config/global/obj/spamfilter/bwl/{bwl}/entries/{entries}'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'bwl',
            'type': 'string'
        },
        {
            'name': 'entries',
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
                                'spam',
                                'clear',
                                'reject'
                            ]
                        },
                        'addr-type': {
                            'type': 'string',
                            'enum': [
                                'ipv4',
                                'ipv6'
                            ]
                        },
                        'email-pattern': {
                            'type': 'string'
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
                        'pattern-type': {
                            'type': 'string',
                            'enum': [
                                'wildcard',
                                'regexp'
                            ]
                        },
                        'status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'type': {
                            'type': 'string',
                            'enum': [
                                'ip',
                                'email'
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
            ],
            'object3': [
                {
                    'name': 'option',
                    'type': 'dict',
                    'dict': {
                        'type': 'string',
                        'enum': [
                            'before',
                            'after'
                        ]
                    },
                    'api_tag': 0
                },
                {
                    'type': 'string',
                    'name': 'target',
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
            'move': 'object3',
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
                'move',
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