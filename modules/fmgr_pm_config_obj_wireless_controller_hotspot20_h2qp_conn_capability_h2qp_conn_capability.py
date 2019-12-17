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
module: fmgr_pm_config_obj_wireless_controller_hotspot20_h2qp_conn_capability_h2qp_conn_capability
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ clone delete get set update ] the following apis:
    - /pm/config/adom/{adom}/obj/wireless-controller/hotspot20/h2qp-conn-capability/{h2qp-conn-capability}
    - /pm/config/global/obj/wireless-controller/hotspot20/h2qp-conn-capability/{h2qp-conn-capability}
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
            h2qp-conn-capability:
                type: str
    schema_object0:
        methods: [clone, set, update]
        description: 'Configure connection capability.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                esp-port:
                    type: str
                    description: 'Set ESP port service (used by IPsec VPNs) status.'
                    choices:
                        - closed
                        - open
                        - unknown
                ftp-port:
                    type: str
                    description: 'Set FTP port service status.'
                    choices:
                        - closed
                        - open
                        - unknown
                http-port:
                    type: str
                    description: 'Set HTTP port service status.'
                    choices:
                        - closed
                        - open
                        - unknown
                icmp-port:
                    type: str
                    description: 'Set ICMP port service status.'
                    choices:
                        - closed
                        - open
                        - unknown
                ikev2-port:
                    type: str
                    description: 'Set IKEv2 port service for IPsec VPN status.'
                    choices:
                        - closed
                        - open
                        - unknown
                ikev2-xx-port:
                    type: str
                    description: 'Set UDP port 4500 (which may be used by IKEv2 for IPsec VPN) service status.'
                    choices:
                        - closed
                        - open
                        - unknown
                name:
                    type: str
                    description: 'Connection capability name.'
                pptp-vpn-port:
                    type: str
                    description: 'Set Point to Point Tunneling Protocol (PPTP) VPN port service status.'
                    choices:
                        - closed
                        - open
                        - unknown
                ssh-port:
                    type: str
                    description: 'Set SSH port service status.'
                    choices:
                        - closed
                        - open
                        - unknown
                tls-port:
                    type: str
                    description: 'Set TLS VPN (HTTPS) port service status.'
                    choices:
                        - closed
                        - open
                        - unknown
                voip-tcp-port:
                    type: str
                    description: 'Set VoIP TCP port service status.'
                    choices:
                        - closed
                        - open
                        - unknown
                voip-udp-port:
                    type: str
                    description: 'Set VoIP UDP port service status.'
                    choices:
                        - closed
                        - open
                        - unknown
    schema_object1:
        methods: [delete]
        description: 'Configure connection capability.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object2:
        methods: [get]
        description: 'Configure connection capability.'
        api_categories: [api_tag0]
        api_tag0:
            option:
                type: str
                description:
                 - 'Set fetch option for the request. If no option is specified, by default the attributes of the object will be returned.'
                 - 'object member - Return a list of object members along with other attributes.'
                 - 'chksum - Return the check-sum value instead of attributes.'
                choices:
                    - object member
                    - chksum
                    - datasrc

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:
    - name: send request to /pm/config/obj/wireless-controller/hotspot20/h2qp-conn-capability/{h2qp-conn-capability}
      fmgr_pm_config_obj_wireless_controller_hotspot20_h2qp_conn_capability_h2qp_conn_capability:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            h2qp-conn-capability: <value of string>
         params:
            - 
               data: 
                  esp-port: <value in [closed, open, unknown]>
                  ftp-port: <value in [closed, open, unknown]>
                  http-port: <value in [closed, open, unknown]>
                  icmp-port: <value in [closed, open, unknown]>
                  ikev2-port: <value in [closed, open, unknown]>
                  ikev2-xx-port: <value in [closed, open, unknown]>
                  name: <value of string>
                  pptp-vpn-port: <value in [closed, open, unknown]>
                  ssh-port: <value in [closed, open, unknown]>
                  tls-port: <value in [closed, open, unknown]>
                  voip-tcp-port: <value in [closed, open, unknown]>
                  voip-udp-port: <value in [closed, open, unknown]>
    - name: send request to /pm/config/obj/wireless-controller/hotspot20/h2qp-conn-capability/{h2qp-conn-capability}
      fmgr_pm_config_obj_wireless_controller_hotspot20_h2qp_conn_capability_h2qp_conn_capability:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            h2qp-conn-capability: <value of string>
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
            example: /pm/config/adom/{adom}/obj/wireless-controller/hotspot20/h2qp-conn-capability/{h2qp-conn-capability}
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            esp-port:
               type: str
               description: 'Set ESP port service (used by IPsec VPNs) status.'
            ftp-port:
               type: str
               description: 'Set FTP port service status.'
            http-port:
               type: str
               description: 'Set HTTP port service status.'
            icmp-port:
               type: str
               description: 'Set ICMP port service status.'
            ikev2-port:
               type: str
               description: 'Set IKEv2 port service for IPsec VPN status.'
            ikev2-xx-port:
               type: str
               description: 'Set UDP port 4500 (which may be used by IKEv2 for IPsec VPN) service status.'
            name:
               type: str
               description: 'Connection capability name.'
            pptp-vpn-port:
               type: str
               description: 'Set Point to Point Tunneling Protocol (PPTP) VPN port service status.'
            ssh-port:
               type: str
               description: 'Set SSH port service status.'
            tls-port:
               type: str
               description: 'Set TLS VPN (HTTPS) port service status.'
            voip-tcp-port:
               type: str
               description: 'Set VoIP TCP port service status.'
            voip-udp-port:
               type: str
               description: 'Set VoIP UDP port service status.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: /pm/config/adom/{adom}/obj/wireless-controller/hotspot20/h2qp-conn-capability/{h2qp-conn-capability}

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
        '/pm/config/adom/{adom}/obj/wireless-controller/hotspot20/h2qp-conn-capability/{h2qp-conn-capability}',
        '/pm/config/global/obj/wireless-controller/hotspot20/h2qp-conn-capability/{h2qp-conn-capability}'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'h2qp-conn-capability',
            'type': 'string'
        }
    ]

    body_schema =  {
        'schema_objects': {
            'object0': [
                {
                    'name': 'data',
                    'type': 'dict',
                    'dict': {
                        'esp-port': {
                            'type': 'string',
                            'enum': [
                                'closed',
                                'open',
                                'unknown'
                            ]
                        },
                        'ftp-port': {
                            'type': 'string',
                            'enum': [
                                'closed',
                                'open',
                                'unknown'
                            ]
                        },
                        'http-port': {
                            'type': 'string',
                            'enum': [
                                'closed',
                                'open',
                                'unknown'
                            ]
                        },
                        'icmp-port': {
                            'type': 'string',
                            'enum': [
                                'closed',
                                'open',
                                'unknown'
                            ]
                        },
                        'ikev2-port': {
                            'type': 'string',
                            'enum': [
                                'closed',
                                'open',
                                'unknown'
                            ]
                        },
                        'ikev2-xx-port': {
                            'type': 'string',
                            'enum': [
                                'closed',
                                'open',
                                'unknown'
                            ]
                        },
                        'name': {
                            'type': 'string'
                        },
                        'pptp-vpn-port': {
                            'type': 'string',
                            'enum': [
                                'closed',
                                'open',
                                'unknown'
                            ]
                        },
                        'ssh-port': {
                            'type': 'string',
                            'enum': [
                                'closed',
                                'open',
                                'unknown'
                            ]
                        },
                        'tls-port': {
                            'type': 'string',
                            'enum': [
                                'closed',
                                'open',
                                'unknown'
                            ]
                        },
                        'voip-tcp-port': {
                            'type': 'string',
                            'enum': [
                                'closed',
                                'open',
                                'unknown'
                            ]
                        },
                        'voip-udp-port': {
                            'type': 'string',
                            'enum': [
                                'closed',
                                'open',
                                'unknown'
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