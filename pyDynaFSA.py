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
        self.F_Out = [list() for i in range(self.nbt)]

    def next(self, symbol) :
        ok = super().next(symbol)
        return ok

    def run(self, word) :
        word.reverse()
        self.word = word
        ok = True
        while ( not self.end() ) and ok :
            if len(self.word)>0:
                symbol = self.word.pop()
                ok = self.next(symbol)
            else : 
                ok = False
        if self.end() : print('Réussite')
        else : print('Echec')
        
#==================================================
#==================================================
#==================================================

if __name__ == '__main__':
    print('main de FSA.py')
    fsa = FSD()
    fsa.loadJFLAP4File('ex.csv')
    fsa.run(['a','c'])






