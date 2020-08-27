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


class DynaFSD(FSD):

    def __init__(self):
        FSD.__init__(self)
        # self.F_In = [list() for i in range(self.nbt)]
        self.FT_Out = [list() for i in range(len(self.mu))]
        self.FQ_Out = [list() for i in range(len(self.Q))]

    def setQOutEvent(self, q, outEvt):
        assert isinstance(outEvt, OutEvent), "[setOutEvent] mauvais type d'event"
        if q in self.Q:
            i = self.Q.index(q)
            self.FQ_Out[i].append(outEvt)
        else:
            pass

    def setTOutEvent(self, m, outEvt):
        assert isinstance(outEvt, OutEvent), "[setOutEvent] mauvais type d'event"
        if m in self.mu:
            i = self.Q.index(m)
            self.FT_Out[i].append(outEvt)
        else:
            pass

    def next(self, symbol) :
        ok = super().next(symbol)
        t = self.mem[:1]
        return ok

    def run(self, word) :
        super().run(word)

        
#==================================================
#==================================================
#==================================================

if __name__ == '__main__':
    print('main de FSA.py')
    fsa = FSD()
    fsa.loadJFLAP4File('ex.csv')
    fsa.run(['a','c'])






