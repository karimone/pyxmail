# -*- coding: utf-8 -*-
"""
"""
import logging

_logger = logging.getLogger(__name__)


class ReceivedEmail:
    def __init__(self, text, from_address, to_address, *args, **kwargs):
        """"""
        self.text = text
        self.from_address = from_address
        self.to_address = to_address

