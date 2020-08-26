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
	def __init__(self):
		self.A = None # set() of String or integers
		self.Q = None # set() of States
		self.I = None
		self.F = None # set()
		self._mu = dict()
		self.mu = None
		self.currentState = None
		self.isDeterministic = False
		self.time = 0
		self.mem = None
		self.word = None

	def load(self,A,Q, I, F, mu):
		self.A = A # set() of String or integers
		self.Q = Q # set() of States
		assert reduce(lambda x,y: x and y, [i in Q for i in I]) , 'Initial state is not a state'
		self.I = I
		assert reduce(lambda x,y: x and y, [f in Q for f in F]), 'Final states are not states'
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
		self.isDeterministic = det and (len(self.I)==1)
		self.init()

	def test(self) :
		pass

	def loadJFLAP4File(self, f) :
		if existFile(f) :
			self.A = list()
			self.Q = list()
			self.I = list()
			self.F = list()
			self.mu = list()
			self._mu = dict()
			det = True
			with open(f, newline='') as csvfile:
				fsa = csv.DictReader(csvfile, delimiter=';')
				for row in fsa:
					typeNode = row['type']
					if typeNode == 'state' :
						q = int(row['id'])
						initial = row['v1'] == 'true'
						final = row['v2'] == 'true'
						self.Q.append(q)
						if initial : self.I.append(q)
						if final : self.F.append(q)
					elif typeNode == 'transition' :
						s = int(row['v1'])
						c = int(row['v3'])
						a = row['v2']
						self.mu.append( ( s, a, c ) )
						if a not in self.A : self.A.append( a )
						if (s,a) in self._mu: 
							self._mu[(s, a)].append(t)
							det = False
						else: self._mu[(s, a)] = [ (s,a,c) ]
						if a is None: det = False
			self.isDeterministic = det and (len(self.I)==1)
			self.init()
			print('File loaded')
			return True
		else :
			print('File ',f,' doesn''t exist')
			return False

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
	def __init__(self):
		FSA.__init__(self)

	def load(self,A,Q, I, F, mu):
		super().load(A,Q, I, F, mu)
		assert self.isDeterministic, "FSA is not a determinic one !"

	def toMinimal(self): #TODO
		pass

	def toDeterministic(self, fsa): #TODO
		pass

	def next(self, symbol = None) :
		if symbol is None :
			symbol = self.word.pop()
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

	def setWord(self,word) :
		self.word = word.copy()
		self.word.reverse()

	def run(self, word) :
		self.setWord(word)
		ok = True
		while ( not self.end() ) and ok :
			if len(self.word)>0:
				ok = self.next()
			else : 
				ok = False
		if self.end() : print(word,' ok')
		else : print(word,' ko')
		
#==================================================
#==================================================
#==================================================

if __name__ == '__main__':
	print('main de FSA.py')
	fsa = FSD()
	fsa.load(['a','b', 'c'], [1, 2, 3, 4, 5], [1], [4], [ (1,'a',3), (2,'b',3), (3,'c',4), (3,'a',5) ] )
	fsa.run(['a','c'])

	# fsd = FSD()
	# fsd.loadJFLAP4File('ex.csv')
