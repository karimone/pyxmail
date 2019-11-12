# -*- coding: utf-8 -*-
"""
Module Docstring
Author: Karim N. Gorjux
"""
import abc
import logging

_logger = logging.getLogger(__name__)


class AbstractMailbox(abc.ABC):
    """Abstract for a Mailbox"""

    LABEL = None
    CONNECTION_URI = None

    def __init__(self):
        self.mailbox = []

    @abc.abstractmethod
    def refresh(self) -> int:
        """Returns the new email(s) retrieved"""
        pass

    @abc.abstractmethod
    def get_email_address(self) -> str:
        pass
