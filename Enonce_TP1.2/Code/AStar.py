# -*- coding: utf-8 -*-
#
# Implementation of A* algorithm
#
# Author: Michel Gagnon
# Date:  31/01/2014

from node import *
import sys
import math


class Search(object):
    """ This is an implementation of the A* search """
    def __init__(self, initState, successTest):
        self.initNode = Node(initState)
        self.successTest = successTest
        self.visitedNodes = []
        self.openNodes = []


    ####################
    # Public functions
    ####################

    def startSearch(self):
        """ This function does the search and returns a plan """
        self.openNodes.append(self.initNode)
        while self.openNodes:
            currentNode = self.openNodes.pop()
            if filter(lambda n: n.state.isEqual(currentNode.state), self.visitedNodes):
                '''
                print "+++++++++++++++++++++ALERT+++++++++++++++++++++"
                currentNode.show()
                print "+++++++++++++++++++ALERT END+++++++++++++++++++"
                '''
                continue
            else:
                self.visitedNodes.append(currentNode)
                #currentNode.show()
                if self.successTest(currentNode.state):
                    print "TEST successful"
                    return self._extractPlan(currentNode)
                else:
                    # Expand current node and sort the open node list
                    self.openNodes += currentNode.expand()
                    self.openNodes.sort(cmp = lambda n1,n2: -1 if n1.f < n2.f else (1 if n1.f > n2.f else 0), 
                                        reverse = True)
                    '''
                    print "*********************START********************************"
                    for n in self.openNodes:
                        n.show()
                    print "**********************END*********************************"
                    '''
        print "TEST RETURN None"
        return None

    ####################
    # Private functions
    ####################


    def _extractPlan(self,node):
        print "------------------------------EXTRACT PLAN------------------------------"
        currentNode = node
        plan = [currentNode.action]
        while currentNode.previous != None:
            currentNode.show()
            currentNode = currentNode.previous
            plan.append(currentNode.action)

        plan.pop()
        return plan


