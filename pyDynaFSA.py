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

    def next(self, symbol) :
        if (self.currentState, symbol) in self._mu :
            lt = self._mu[(self.currentState, symbol)]
            self.time += 1
            (s,a,c) = lt[0]
            self.mem.append( (self.time, s, a, c) )
            self.currentState = c
            ok = True
        else :
            ok = False
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
    fsa.load(['a','b', 'c'], [1, 2, 3, 4, 5], [1], [4], [ (1,'a',3), (2,'b',3), (3,'c',4), (3,'a',5) ] )
    fsa.run(['a','c'])






