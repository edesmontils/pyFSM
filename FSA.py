#!/usr/bin/env python3.7
# coding: utf8

import random
import os
import csv
from functools import reduce

#==================================================
#============ Tools ===============================
#==================================================

def existFile(f):
	return os.path.isfile(f)

def existDir(d):
	return os.path.exists(d)

def choixAleatoire(l) :
	if len(f) == 0 :
		return None
	elif len(l) == 1 :
		return l[0]
	else :
		return random.choice(l)

#==================================================
#==================================================

class FSA(object):
	def __init__(self,A,Q, I, F, mu):
		self.A = A # set() of String or integers
		self.Q = Q # set() of States
		assert reduce(lambda x,y: x and y, [i in Q for i in I]) , 'Initial state is not a state'
		self.I = I
		assert reduce(lambda x,y: x and y, [f in Q for f in F]), 'Final states are not a states'
		self.F = F # set()
		self._mu = dict()
		det = True
		for t in mu :
			(s,a,c) = t
			assert ((a in self.A) or (a is None)) and s in self.Q and c in self.Q, "Transition error"
			if (s,a) in self._mu: 
				self._mu[(s, a)].append(t)
				det = False
			else: self._mu[(s, a)] = [t]
			if a is None: det = False
		self.mu = mu
		self.currentState = None
		self.isDeterministic = det and (len(self.I)==1)
		self.time = 0
		self.mem = None
		self.word = None
		self.init()

	def init(self) :
		self.time = 0
		self.currentState = self.I[0]
		self.mem = list()
		self.mem.append( (self.time, None, None, self.currentState) )
		self.word=[]

	def run(self, word):
		pass

	def end(self,word = None):
		if word is None : word = self.word
		return (len(word) == 0) and (self.currentState in self.F)

	def isDeterministic(self):
		return self.isDeterministic


class FSD(FSA):
	"""docstring for FSD"""
	def __init__(self, A,Q, I, F, mu):
		FSA.__init__(self,A,Q, I, F, mu)
		assert self.isDeterministic, "Automate non déterministe !"

	def toMinimal(self): #TODO
		pass

	def toDeterministic(self, fsa): #TODO
		pass

	def next(self, symbol) :
		ok = True
		if (self.currentState, symbol) in self._mu :
			lt = self._mu[(self.currentState, symbol)]
			self.time += 1
			(s,a,c) = lt[0]
			self.mem.append( (self.time, s, a, c) )
			self.currentState = c
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
		if ok and self.end() : print('Réussite')
		else : print('Echec')
		
#==================================================
#==================================================
#==================================================

if __name__ == '__main__':
	print('main de FSA.py')
	fsa = FSD(['a','b', 'c'], [1, 2, 3, 4, 5], [1], [4], [ (1,'a',3), (2,'b',3), (3,'c',4), (3,'a',5) ] )
	fsa.run(['a','c'])

