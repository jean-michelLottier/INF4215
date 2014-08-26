# -*- coding: utf-8 -*-
import sys
import math
import copy
from random import random
from random import sample
from agent import *


class Node(object):
    def __init__(self, state, action = None, cost = 0, previous = None):
        self.state = state
        self.previous = previous
        self.g = cost
        self.h = self.estimateHeuristic()
        self.f = self.g + self.h
        self.action = action 

    ####################
    # Public methods
    ####################

    def expand(self):
        nextStates = list()
        # À Implémenter
        # Doit retourner une liste d'état successeurs
        # Pour chaque état, on doit fixer la valeur f(n) = g(n) + h(n)

        #Etape 1 : un etat successeur peut etre un take (de package de poids minimum)
        packagesList = self.getPackagesUnprocessed(self.state.agent.position)
        if packagesList is not None and len(packagesList) is not 0:
            packageLightest = reduce(lambda x,y:x if x.weight < y.weight else y,packagesList)
            if (self.state.agent.loadWeight + packageLightest.weight) <= self.state.agent.maxLoad:
                action = ('take',packageLightest)
                cost = self.g + self.state.agent.k*packageLightest.weight
                stateCopy = copy.deepcopy(self.state)
                stateCopy.executeAction(action)
                node = Node(stateCopy,action,cost,self)
                nextStates.append(node)

        #Etape 2 : un move est un état successeur courant
        positions = self.state.graph.specialNodes
        for position in positions:
            if position is self.state.agent.position:
                continue

            action =('moveAndDrop',position)
            d = self.state.graph.shortestPathLength(self.state.agent.position,position)
            cost = self.g + self.state.agent.k*d*(self.state.agent.weight + self.state.agent.loadWeight)
            stateCopy = copy.deepcopy(self.state)
            stateCopy.executeAction(action)
            node = Node(stateCopy,action,cost,self)
            nextStates.append(node)

        return nextStates

 
    def estimateHeuristic(self):
        # À Implémenter: Vous pouvez rajouter les paramètres 
        # nécessaire pour calculer l'heuristique.
        # L'heuristique est déterminée en fonction du nombre de paquets non traités : h = la somme des énergies dépensées pour prendre et acheminer ces paquets vers leur destination
        packagesUnprocessed = self.getPackagesByPosition()
        h = 0

        for position in packagesUnprocessed:
            if packagesUnprocessed[position] is None: continue
            for package in packagesUnprocessed[position]:
                d = self.state.graph.shortestPathLength(position,package.destination)
                h += self.state.agent.k*package.weight + self.state.agent.weight
                #h += self.state.agent.k*d*(self.state.agent.weight - 2 + package.weight)
                #h += d

        return h 


    def show(self):
        if self.previous is None:
            print 'agent PreviousPosition:None, CurrentPosition:{} --> g = {}, h = {}, f = {}, action: {}'.format(self.state.agent.position,self.g,self.h,self.f,self.action)
        else:
            print 'agent PreviousPosition:{}, CurrentPosition:{} --> g = {}, h = {}, f = {}, action: {}'.format(self.previous.state.agent.position,self.state.agent.position,self.g,self.h,self.f,self.action)
               
                

    ####################
    # Private methods
    ####################
    def getPackagesByPosition(self):
        specialNodes = self.state.graph.specialNodes
        packagesUnprocessed = dict()
        for specialNode in specialNodes:
            packagesUnprocessed[specialNode] = self.getPackagesUnprocessed(specialNode)

        if len(self.state.agent.load) is not 0:
            if packagesUnprocessed.get(self.state.agent.position) is None:
                packagesUnprocessed[self.state.agent.position] += self.state.agent.load
            else:
                packagesUnprocessed[self.state.agent.position] = packagesUnprocessed.get(self.state.agent.position) + list(self.state.agent.load)

        return packagesUnprocessed
                                    
    def getPackagesUnprocessed(self,position):
        return filter(lambda x: x.destination is not position,self.state.getDeskState(position)) 