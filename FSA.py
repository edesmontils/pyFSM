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
		self.trace = None
		self.time = 0
		self.mem = None
		self.init()

	def init(self) :
		self.trace = list()
		self.time = 0
		self.mem = list()
		self.currentState = self.I[0]
		self.mem.append( (0, None, None, self.currentState) )

	def run(self, word):
		pass
		# word.reverse()
		# ok = True
		# while not ( (len(word)==0) and self.end()  ) and ok :
		# 	if len(word)>0:
		# 		symbol = word.pop()
		# 	else symbol = None
		# 	if (self.currentState, symbol) in self._mu :
		# 		lt = self._mu[(self.currentState, symbol)]
		# 		self.time += 1
		# 		(s,a,c) = lt[0]
		# 		self.mem.append( (self.time, s, a, c) )
		# 		self.currentState = c
		# 		print(s,a,c)
		# 	else :
		# 		ok = False
		# 		word.append(symbol)
		# 		while (not ok) and (len(self.mem)>0) :
		# 			(d, symbol, a, c) = self.mem.pop()
		# 			if d>0 :
		# 				lt = self._mu( (symbol,a) )
		# 				i = lt.index[ (symbol,a,c) ]
		# 				if i < len(lt)-1 :
		# 					ok = True
		# 					self.time = d
		# 					(a, symbol, c) = lt[i+1]
		# 					self.mem.append( (self.time, symbol, a, c) )
		# 					self.currentState = c
		# 					print((a, symbol, c))
		# 				else :
		# 					word.append(symbol)
		# 			else:
		# 				i = self.I.index(c)
		# 				if i < len(self.I)-1 :
		# 					ok = True
		# 					self.time = 0
		# 					c = self.I[i+1]
		# 					self.mem.append( (self.time, None, None, c) )
		# 					self.currentState = c					
		# 		if not ok :
		# 			print('Echec')
		# 			c = None
		# 			break
		# if ok and (len(word)==0) : print('Réussite')
		# print('Fin')

	def end(self):
		return self.currentState in self.F

	def isDeterministic(self): #TODO
		return False


class FSD(FSA):
	"""docstring for FSD"""
	def __init__(self, A,Q, I, F, mu):
		FSA.__init__(self,A,Q, I, F, mu)
		#assert deterinistic

	def toMinimal(self): #TODO
		pass

	def toDeterministic(self, fsa): #TODO
		pass
		

	def run(self, word) :
		pass
		
#==================================================
#==================================================
#==================================================

if __name__ == '__main__':
	print('main de FSA.py')
	fsa = FSA(['a','b', 'c'], [1, 2, 3, 4, 5], [1], [5], [ (1,'a',3), (2,'b',3), (3,'c',4), (3,'c',5) ] )
	fsa.run(['a','c'])

