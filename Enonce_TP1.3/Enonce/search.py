# -*- coding: utf-8 -*-
#
# Implementation of A* algorithm
#
# Author: Michel Gagnon
# Date:  31/01/2014

#from node import *
import sys
import math
import subprocess
from itertools import *


class Search(object):
    """ This is an implementation of the A* search """
    def __init__(self, environment):
        self.environment = environment



    ####################
    # Public functions
    ####################

    def startSearch(self):
        """ This function does the search and returns a plan """
        self._createProblemFile()
        self.result = subprocess.Popen('../Metric-FF-v2.1/./ff -o domain.pddl -f problem.pddl > result.txt',shell=True)
        self.result.wait()
        print "*************************************************************************"
        return self._extractPlan()


    ####################
    # Private functions
    ####################


    def _createProblemFile(self):
        self.problemFile = open('problem.pddl','w')
        self.problemFile.write("""
(define (problem prob1)
   (:domain store)
""")

        # Object list
        self.problemFile.write("   (:objects")
        for d in self.environment.graph.nodes:
            self.problemFile.write(" " + d)
        for p in self.environment.packages:
            self.problemFile.write(" " + p.id)
        self.problemFile.write(")\n")

        self.problemFile.write("   (:init \n")

        self.problemFile.write("      (agent {})\n".format("myAgent"))
        self.problemFile.write("      (agentAt {} {})\n".format("myAgent",self.environment.agent.position))
        self.problemFile.write("      (= (agentLoadWeight {}) {})\n".format("myAgent",self.environment.agent.loadWeight))
        self.problemFile.write("      (= (agentMaxLoad {}) {})\n".format("myAgent",self.environment.agent.maxLoad))
        self.problemFile.write("      (= (cost) {})\n".format(0))

        # Package list
        for  p in self.environment.packages:
            self.problemFile.write("      (package {})\n".format(p.id))
            self.problemFile.write("      (packageAt {} {})\n".format(p.id,p.origin))
            self.problemFile.write("      (= (packageWeight {}) {})\n".format(p.id,p.weight))
            self.problemFile.write("      (packageDest {} {})\n".format(p.id,p.destination))
            #self.problemFile.write("      (not (in {} {}))\n".format(p.id,"myAgent"))
            #self.problemFile.write("      (not (delivered {}))\n".format(p.id))
			
         # Connected node
        for n1 in self.environment.graph.nodes:
            self.problemFile.write("      (node {})\n".format(n1))
            for n2 in self.environment.graph.nodes:
                if n1 is n2: continue
                if self.environment.graph.connected(n1,n2) is True:
                    self.problemFile.write("      (connected {} {})\n".format(n1,n2))
                    self.problemFile.write("      (= (distance {} {}) {})\n".format(n1,n2,self.environment.graph.shortestPathLength(n1,n2)))

        self.problemFile.write("   )\n")
        # Vous devez compléter ici...
        
        self.problemFile.write("""
   (:goal (forall (?x) (imply (package ?x) (delivered ?x))))
   (:metric minimize (cost)))
""") 
        self.problemFile.flush()                             

    def _extractPlan(self):
        result = open('result.txt')
        lines = result.readlines()
        lines = [l for l in dropwhile(lambda s: not s.startswith('ff: found legal plan'),lines)]
        lines = lines[1:]
        lines = [l for l in takewhile(lambda s: not s.startswith('plan cost'),lines)]

        plan = []
        for line in [l.split() for l in lines]:
            x = line[-3]
            if x == "take" or x == "drop":
                y = line[-2]
            else:
                y = line[-1]

            plan.append((x,y))

        plan.reverse()
        
        return plan                


