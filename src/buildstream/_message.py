#
#  Copyright (C) 2017 Codethink Limited
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
#  Authors:
#        Tristan Van Berkom <tristan.vanberkom@codethink.co.uk>

import datetime
import os


# Types of status messages.
#
class MessageType:
    DEBUG = "debug"  # Debugging message
    STATUS = "status"  # Status message, verbose details
    INFO = "info"  # Informative messages
    WARN = "warning"  # Warning messages
    ERROR = "error"  # Error messages
    BUG = "bug"  # An unhandled exception was raised in a plugin
    LOG = "log"  # Messages for log files _only_, never in the frontend

    # Timed Messages: SUCCESS and FAIL have duration timestamps
    START = "start"  # Status start message
    SUCCESS = "success"  # Successful status complete message
    FAIL = "failure"  # Failing status complete message
    SKIPPED = "skipped"


# Messages which should be reported regardless of whether
# they are currently silenced or not
unconditional_messages = [MessageType.INFO, MessageType.WARN, MessageType.FAIL, MessageType.ERROR, MessageType.BUG]


# Message object
#
class Message:
    def __init__(
        self,
        message_type,
        message,
        *,
        task_element_name=None,
        task_element_key=None,
        element_name=None,
        element_key=None,
        detail=None,
        action_name=None,
        elapsed=None,
        logfile=None,
        sandbox=False,
        scheduler=False
    ):
        self.message_type = message_type  # Message type
        self.message = message  # The message string
        self.task_element_name = task_element_name  # The name of the issuing task element
        self.task_element_key = task_element_key  # The DisplayKey of the issuing task element
        self.element_name = element_name  # The name of the issuing element
        self.element_key = element_key  # The DisplayKey of the issuing element
        self.detail = detail  # An additional detail string
        self.action_name = action_name  # Name of the task queue (fetch, refresh, build, etc)
        self.elapsed = elapsed  # The elapsed time, in timed messages
        self.logfile = logfile  # The log file path where commands took place
        self.sandbox = sandbox  # Whether the error that caused this message used a sandbox
        self.pid = os.getpid()  # The process pid
        self.scheduler = scheduler  # Whether this is a scheduler level message
        self.creation_time = datetime.datetime.now()
        if message_type in (MessageType.SUCCESS, MessageType.FAIL):
            assert elapsed is not None
