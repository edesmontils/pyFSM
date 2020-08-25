#!/usr/bin/env python3.7
# coding: utf8

from pyFSA import *

# ==================================================
# ==================================================
# ==================================================


class Event(object):
    def __init__(self):
        super(Event, self).__init__()

    def declencher(self) :
        pass
# ==================================================
# OUT
# ==================================================


class OutEvent(Event):
    def __init__(self):
        super(OutEvent, self).__init__()

# ==================================================

class DisplayEvent(OutEvent):
    def __init__(self):
        super(DisplayEvent, self).__init__()


class StdoutDisplayEvent(DisplayEvent):
    def __init__(self, cdc=None):
        super(StdoutDisplayEvent, self).__init__()
        self.cdc = cdc

    def declencher(self) :
        print(self.cdc)

# ==================================================
# IN
# ==================================================


class InEvent(Event):
    def __init__(self):
        super(InEvent, self).__init__()

    def estDeclenchable(self) :
        return False

    def declencher(self) :
        pass









