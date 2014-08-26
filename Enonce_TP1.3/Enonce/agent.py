# -*- coding: utf-8 -*-
#
# Implementation of an agent
#
# Author: Michel Gagnon
# Date:  14/02/2014
from search import *
import sys



class Agent:
    def __init__(self, graph, pos, weight = 10, maxLoad = 5, k = 1):
        self.graph = graph
        self.position = pos
        self.weight = weight
        self.maxLoad = maxLoad
        self.load = set()
        self.loadWeight = 0
        self.distance = 0
        self.k = k
        self.plan = []

    def take(self, package):
        "Add one package to its load, if maximum weight is not reached"
        self.load.add(package)
        self.loadWeight += package.weight
        if self.loadWeight > self.maxLoad:
            print "LOAD=", self.loadWeight, "WEIGHT=", self.maxLoad
            raise RuntimeError


    def getLoad(self):
        return self.load

    def empty(self):
        return len(self.load) == 0

    def find(self, condition):
        "Find the packages that respect the condition"
        return filter(condition,self.load)

    def move(self, newPosition):
        "Move to the new position "
        self.distance += self.cost(('move',newPosition))
        self.position = newPosition
 
    def drop(self,packageId):
        "Drop the package whose destination is this position"
        
        package = self.find(lambda p: p.id == packageId)[0]
        self.load.remove(package)
        self.loadWeight -= package.weight

    def chooseAction(self, environment):
        if environment.allDelivered():
            return ('wait',None)

        isGenerateNewPlan = False
        if self.plan:
            packagePlanList = list()
            for action in self.plan:
                if action[0] == "take":
                    packagePlanList.append(action[1])
            results = map(lambda x: x.id not in packagePlanList, environment.packages)
            # Si l'agent détecte que l'environnement à changé par rapport à son plan
            if map(lambda x: x.id not in packagePlanList, environment.packages).__contains__(True):
                isGenerateNewPlan = True
        
        # Même si l'environnement a changé, si l'agent transporte des paquets on attend qu'ils soient livrés avant de replannifier
        if (not self.plan) or (isGenerateNewPlan is True and len(self.load) is 0):
            self.plan = Search(environment).startSearch()
        return self.plan.pop()    


    def updateModel(self,action,environment):
        pass

    def cost(self,(action,arg)):
        if action == 'move':
            return self.costMove(self.position,arg)
        else:
            return 0


    def costMove(self,source,dest):
        distance = self.graph.shortestPathLength(source,dest)
        return distance 

        
    
