# -*- coding: utf-8 -*-
"""
Module Docstring
Author: Karim N. Gorjux
"""
import sys

from json import loads
from subprocess import call
from datetime import datetime
import logging

from json import loads
from subprocess import call
from datetime import datetime

import asyncio
from websocket import create_connection

from .base import AbstractMailbox

_logger = logging.getLogger(__name__)


class DropMail(AbstractMailbox):

    CONNECTION_URI = "wss://dropmail.me/websocket"

    def __init__(self):
        super(DropMail, self).__init__()
        self._ws = None
        self.email_address = None
        self._connect()

    def _set_email(self):
        self.email_address = self._receive()[1:].split(":")[0]

    def _receive(self):
        if self._ws:
            return self._ws.recv()
        return None

    def _close(self):
        if self._ws:
            return self._ws.close()
        return None

    def _connect(self):
        self._ws = create_connection(self.CONNECTION_URI)
        self._set_email()

    def refresh(self):
        """Receive the last message"""
        pass

    def get_email_address(self):
        return self.email_address
