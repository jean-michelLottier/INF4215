# -*- coding: utf-8 -*-
from node import *
import sys
import math
import random


class Search(object):
	def __init__(self,initState,successTest):
		self.initNode = Node(initState)
		self.successTest = successTest

	def startSearch(self,k = 10):
		currentNode = self.initNode
		for t in xrange(sys.maxint):
			T = self.exp_schedule(t)
			if T <= 0.00000001 or self.successTest(currentNode.state):
				return self._extractPlan(currentNode)
			for i in range(k):
				#currentNode.show()
				nextNodes = currentNode.expand()
				isNextNodesNotEmpty = True
				while isNextNodesNotEmpty:
					next = random.choice(nextNodes)
					nextNodes.remove(next)
					delta_e = currentNode.h - next.h
					#print "h = {}, h' = {}, delta_e = {}, proba = {}".format(currentNode.h,next.h,delta_e,math.exp(delta_e/T))
					if self.successTest(currentNode.state):
						return self._extractPlan(currentNode)
					if delta_e > 0 or math.exp(delta_e/T) > 0.5:
						currentNode = next
						isNextNodesNotEmpty = False
					elif len(nextNodes) is 0:
						isNextNodesNotEmpty = False

	def exp_schedule(self,t,k=20,lam=0.005,limit=100):
		if t < limit:
			return k*math.exp(-lam*t)
		else:
			return 0
		#return lambda t:(k*math.exp(-lam*t)) if t < limit else 0

	def _extractPlan(self,node):
		currentNode = node
		plan = [currentNode.action]
		while currentNode.previous != None:
			currentNode.show()
			currentNode = currentNode.previous
			plan.append(currentNode.action)
		plan.pop()
		return plan