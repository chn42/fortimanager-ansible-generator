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
module: fmgr_cli_system_log_settings_rolling_analyzer
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ get set update ] the following apis:
    - /cli/global/system/log/settings/rolling-analyzer
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
        description: 'Log rolling policy for Network Analyzer logs.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object1:
        methods: [set, update]
        description: 'Log rolling policy for Network Analyzer logs.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                days:
                    -
                        type: str
                        choices:
                            - sun
                            - mon
                            - tue
                            - wed
                            - thu
                            - fri
                            - sat
                del-files:
                    type: str
                    default: disable
                    description:
                     - 'Enable/disable log file deletion after uploading.'
                     - 'disable - Disable log file deletion.'
                     - 'enable - Enable log file deletion.'
                    choices:
                        - disable
                        - enable
                directory:
                    type: str
                    description: 'Upload server directory, for Unix server, use absolute'
                file-size:
                    type: int
                    default: 200
                    description: 'Roll log files when they reach this size (MB).'
                gzip-format:
                    type: str
                    default: disable
                    description:
                     - 'Enable/disable compression of uploaded log files.'
                     - 'disable - Disable compression.'
                     - 'enable - Enable compression.'
                    choices:
                        - disable
                        - enable
                hour:
                    type: int
                    default: 0
                    description: 'Log files rolling schedule (hour).'
                ip:
                    type: str
                    default: 0.0.0.0
                    description: 'Upload server IP address.'
                ip2:
                    type: str
                    default: 0.0.0.0
                    description: 'Upload server IP2 address.'
                ip3:
                    type: str
                    default: 0.0.0.0
                    description: 'Upload server IP3 address.'
                log-format:
                    type: str
                    default: native
                    description:
                     - 'Format of uploaded log files.'
                     - 'native - Native format (text or compact).'
                     - 'text - Text format (convert if necessary).'
                     - 'csv - CSV (comma-separated value) format.'
                    choices:
                        - native
                        - text
                        - csv
                min:
                    type: int
                    default: 0
                    description: 'Log files rolling schedule (minutes).'
                password:
                    -
                        type: str
                        default: ENC MzQ3NjYyODIxOTc1MTg3NhVVByJnhjVIRIq22N8+MG0by/Mxs5TUnkVnhHtwoRdEVnaNNj6P9rGxNsGaBAn2SVhBLt6V9QWnTm1fbC1hAWycBDzkxK37kTzWEwu5NE66yvC4sVh53l+CSOPZabxA2n7XCNB9Kce1X8EeGUr4PqPCtCej
                password2:
                    -
                        type: str
                        default: ENC MTAwODg0NTQxNDE5OTQwMaPdJv8JESXhogoJmBIvID8+U03pvD8I9Yr/Q1NGxPnlvLKVEOISmJ/IRPZauTQ/oJ5KlJE3LSzrXEOWAhn2mNaoS+nFbu0seQqMEhUdLbx41Q0yi4dCM9n3PF8RETPiFayOQ5sWWPRD7ALjlthRLogqkua5
                password3:
                    -
                        type: str
                        default: ENC MTMyOTA3MjY4MTgxMTk2N1UB1GKpBMmb5vgQRJTsjWS9sBfCvYmhBhdgf+ipyNKwY43YcyKBx3TaUcf6QLEdeVgFD2ymJHzfX99dusp8IfxNYj7ITnobzP+GcHYMOyPtjtcORJqwHTpEy9rnqCfy6nKz2Sdj1D1SnqOfRhn0R8sonnED
                server-type:
                    type: str
                    default: ftp
                    description:
                     - 'Upload server type.'
                     - 'ftp - Upload via FTP.'
                     - 'sftp - Upload via SFTP.'
                     - 'scp - Upload via SCP.'
                    choices:
                        - ftp
                        - sftp
                        - scp
                upload:
                    type: str
                    default: disable
                    description:
                     - 'Enable/disable log file uploads.'
                     - 'disable - Disable log files uploading.'
                     - 'enable - Enable log files uploading.'
                    choices:
                        - disable
                        - enable
                upload-hour:
                    type: int
                    default: 0
                    description: 'Log files upload schedule (hour).'
                upload-mode:
                    type: str
                    default: backup
                    description:
                     - 'Upload mode with multiple servers.'
                     - 'backup - Servers are attempted and used one after the other upon failure to connect.'
                     - 'mirror - All configured servers are attempted and used.'
                    choices:
                        - backup
                        - mirror
                upload-trigger:
                    type: str
                    default: on-roll
                    description:
                     - 'Event triggering log files upload.'
                     - 'on-roll - Upload log files after they are rolled.'
                     - 'on-schedule - Upload log files daily.'
                    choices:
                        - on-roll
                        - on-schedule
                username:
                    type: str
                    description: 'Upload server login username.'
                username2:
                    type: str
                    description: 'Upload server login username2.'
                username3:
                    type: str
                    description: 'Upload server login username3.'
                when:
                    type: str
                    default: none
                    description:
                     - 'Roll log files periodically.'
                     - 'none - Do not roll log files periodically.'
                     - 'daily - Roll log files daily.'
                     - 'weekly - Roll log files on certain days of week.'
                    choices:
                        - none
                        - daily
                        - weekly

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:
    - name: send request to /cli/system/log/settings/rolling-analyzer
      fmgr_cli_system_log_settings_rolling_analyzer:
         method: <value in [set, update]>
         params:
            - 
               data: 
                  days: 
                   - <value in [sun, mon, tue, ...]>
                  del-files: <value in [disable, enable] default: disable>
                  directory: <value of string>
                  file-size: <value of integer default: 200>
                  gzip-format: <value in [disable, enable] default: disable>
                  hour: <value of integer default: 0>
                  ip: <value of string default: 0.0.0.0>
                  ip2: <value of string default: 0.0.0.0>
                  ip3: <value of string default: 0.0.0.0>
                  log-format: <value in [native, text, csv] default: native>
                  min: <value of integer default: 0>
                  password: 
                   - <value of string default: ENC MzQ3NjYyODIxOTc1MTg3NhVVByJnhjVIRIq22N8+MG0by/Mxs5TUnkVnhHtwoRdEVnaNNj6P9rGxNsGaBAn2SVhBLt6V9QWnTm1fbC1hAWycBDzkxK37kTzWEwu5NE66yvC4sVh53l+CSOPZabxA2n7XCNB9Kce1X8EeGUr4PqPCtCej>
                  password2: 
                   - <value of string default: ENC MTAwODg0NTQxNDE5OTQwMaPdJv8JESXhogoJmBIvID8+U03pvD8I9Yr/Q1NGxPnlvLKVEOISmJ/IRPZauTQ/oJ5KlJE3LSzrXEOWAhn2mNaoS+nFbu0seQqMEhUdLbx41Q0yi4dCM9n3PF8RETPiFayOQ5sWWPRD7ALjlthRLogqkua5>
                  password3: 
                   - <value of string default: ENC MTMyOTA3MjY4MTgxMTk2N1UB1GKpBMmb5vgQRJTsjWS9sBfCvYmhBhdgf+ipyNKwY43YcyKBx3TaUcf6QLEdeVgFD2ymJHzfX99dusp8IfxNYj7ITnobzP+GcHYMOyPtjtcORJqwHTpEy9rnqCfy6nKz2Sdj1D1SnqOfRhn0R8sonnED>
                  server-type: <value in [ftp, sftp, scp] default: ftp>
                  upload: <value in [disable, enable] default: disable>
                  upload-hour: <value of integer default: 0>
                  upload-mode: <value in [backup, mirror] default: backup>
                  upload-trigger: <value in [on-roll, on-schedule] default: on-roll>
                  username: <value of string>
                  username2: <value of string>
                  username3: <value of string>
                  when: <value in [none, daily, weekly] default: none>

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
            days:
               type: array
               suboptions:
                  type: str
            del-files:
               type: str
               description: |
                  'Enable/disable log file deletion after uploading.'
                  'disable - Disable log file deletion.'
                  'enable - Enable log file deletion.'
               example: disable
            directory:
               type: str
               description: 'Upload server directory, for Unix server, use absolute'
            file-size:
               type: int
               description: 'Roll log files when they reach this size (MB).'
               example: 200
            gzip-format:
               type: str
               description: |
                  'Enable/disable compression of uploaded log files.'
                  'disable - Disable compression.'
                  'enable - Enable compression.'
               example: disable
            hour:
               type: int
               description: 'Log files rolling schedule (hour).'
               example: 0
            ip:
               type: str
               description: 'Upload server IP address.'
               example: 0.0.0.0
            ip2:
               type: str
               description: 'Upload server IP2 address.'
               example: 0.0.0.0
            ip3:
               type: str
               description: 'Upload server IP3 address.'
               example: 0.0.0.0
            log-format:
               type: str
               description: |
                  'Format of uploaded log files.'
                  'native - Native format (text or compact).'
                  'text - Text format (convert if necessary).'
                  'csv - CSV (comma-separated value) format.'
               example: native
            min:
               type: int
               description: 'Log files rolling schedule (minutes).'
               example: 0
            password:
               type: array
               suboptions:
                  type: str
                  example: ENC MzQ3NjYyODIxOTc1MTg3NhVVByJnhjVIRIq22N8+MG0by/Mxs5TUnkVnhHtwoRdEVnaNNj6P9rGxNsGaBAn2SVhBLt6V9QWnTm1fbC1hAWycBDzkxK37kTzWEwu5NE66yvC4sVh53l+CSOPZabxA2n7XCNB9Kce1X8EeGUr4PqPCtCej
            password2:
               type: array
               suboptions:
                  type: str
                  example: ENC MTAwODg0NTQxNDE5OTQwMaPdJv8JESXhogoJmBIvID8+U03pvD8I9Yr/Q1NGxPnlvLKVEOISmJ/IRPZauTQ/oJ5KlJE3LSzrXEOWAhn2mNaoS+nFbu0seQqMEhUdLbx41Q0yi4dCM9n3PF8RETPiFayOQ5sWWPRD7ALjlthRLogqkua5
            password3:
               type: array
               suboptions:
                  type: str
                  example: ENC MTMyOTA3MjY4MTgxMTk2N1UB1GKpBMmb5vgQRJTsjWS9sBfCvYmhBhdgf+ipyNKwY43YcyKBx3TaUcf6QLEdeVgFD2ymJHzfX99dusp8IfxNYj7ITnobzP+GcHYMOyPtjtcORJqwHTpEy9rnqCfy6nKz2Sdj1D1SnqOfRhn0R8sonnED
            server-type:
               type: str
               description: |
                  'Upload server type.'
                  'ftp - Upload via FTP.'
                  'sftp - Upload via SFTP.'
                  'scp - Upload via SCP.'
               example: ftp
            upload:
               type: str
               description: |
                  'Enable/disable log file uploads.'
                  'disable - Disable log files uploading.'
                  'enable - Enable log files uploading.'
               example: disable
            upload-hour:
               type: int
               description: 'Log files upload schedule (hour).'
               example: 0
            upload-mode:
               type: str
               description: |
                  'Upload mode with multiple servers.'
                  'backup - Servers are attempted and used one after the other upon failure to connect.'
                  'mirror - All configured servers are attempted and used.'
               example: backup
            upload-trigger:
               type: str
               description: |
                  'Event triggering log files upload.'
                  'on-roll - Upload log files after they are rolled.'
                  'on-schedule - Upload log files daily.'
               example: on-roll
            username:
               type: str
               description: 'Upload server login username.'
            username2:
               type: str
               description: 'Upload server login username2.'
            username3:
               type: str
               description: 'Upload server login username3.'
            when:
               type: str
               description: |
                  'Roll log files periodically.'
                  'none - Do not roll log files periodically.'
                  'daily - Roll log files daily.'
                  'weekly - Roll log files on certain days of week.'
               example: none
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: /cli/global/system/log/settings/rolling-analyzer
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
            example: /cli/global/system/log/settings/rolling-analyzer

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
        '/cli/global/system/log/settings/rolling-analyzer'
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
                        'days': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'sun',
                                    'mon',
                                    'tue',
                                    'wed',
                                    'thu',
                                    'fri',
                                    'sat'
                                ]
                            }
                        },
                        'del-files': {
                            'type': 'string',
                            'default': 'disable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'directory': {
                            'type': 'string'
                        },
                        'file-size': {
                            'type': 'integer',
                            'default': 200,
                            'example': 200
                        },
                        'gzip-format': {
                            'type': 'string',
                            'default': 'disable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'hour': {
                            'type': 'integer',
                            'default': 0,
                            'example': 0
                        },
                        'ip': {
                            'type': 'string',
                            'default': '0.0.0.0'
                        },
                        'ip2': {
                            'type': 'string',
                            'default': '0.0.0.0'
                        },
                        'ip3': {
                            'type': 'string',
                            'default': '0.0.0.0'
                        },
                        'log-format': {
                            'type': 'string',
                            'default': 'native',
                            'enum': [
                                'native',
                                'text',
                                'csv'
                            ]
                        },
                        'min': {
                            'type': 'integer',
                            'default': 0,
                            'example': 0
                        },
                        'password': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'default': 'ENC MzQ3NjYyODIxOTc1MTg3NhVVByJnhjVIRIq22N8+MG0by/Mxs5TUnkVnhHtwoRdEVnaNNj6P9rGxNsGaBAn2SVhBLt6V9QWnTm1fbC1hAWycBDzkxK37kTzWEwu5NE66yvC4sVh53l+CSOPZabxA2n7XCNB9Kce1X8EeGUr4PqPCtCej'
                            }
                        },
                        'password2': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'default': 'ENC MTAwODg0NTQxNDE5OTQwMaPdJv8JESXhogoJmBIvID8+U03pvD8I9Yr/Q1NGxPnlvLKVEOISmJ/IRPZauTQ/oJ5KlJE3LSzrXEOWAhn2mNaoS+nFbu0seQqMEhUdLbx41Q0yi4dCM9n3PF8RETPiFayOQ5sWWPRD7ALjlthRLogqkua5'
                            }
                        },
                        'password3': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'default': 'ENC MTMyOTA3MjY4MTgxMTk2N1UB1GKpBMmb5vgQRJTsjWS9sBfCvYmhBhdgf+ipyNKwY43YcyKBx3TaUcf6QLEdeVgFD2ymJHzfX99dusp8IfxNYj7ITnobzP+GcHYMOyPtjtcORJqwHTpEy9rnqCfy6nKz2Sdj1D1SnqOfRhn0R8sonnED'
                            }
                        },
                        'server-type': {
                            'type': 'string',
                            'default': 'ftp',
                            'enum': [
                                'ftp',
                                'sftp',
                                'scp'
                            ]
                        },
                        'upload': {
                            'type': 'string',
                            'default': 'disable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'upload-hour': {
                            'type': 'integer',
                            'default': 0,
                            'example': 0
                        },
                        'upload-mode': {
                            'type': 'string',
                            'default': 'backup',
                            'enum': [
                                'backup',
                                'mirror'
                            ]
                        },
                        'upload-trigger': {
                            'type': 'string',
                            'default': 'on-roll',
                            'enum': [
                                'on-roll',
                                'on-schedule'
                            ]
                        },
                        'username': {
                            'type': 'string'
                        },
                        'username2': {
                            'type': 'string'
                        },
                        'username3': {
                            'type': 'string'
                        },
                        'when': {
                            'type': 'string',
                            'default': 'none',
                            'enum': [
                                'none',
                                'daily',
                                'weekly'
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