#-*- coding:Utf-8 *-
from graph import *

class Environment:
    def __init__(self, graph, agent):
        self.graph = graph
        self.agent = agent
 
        # Initially, desks do not contain any package
        self.desks = {}
        for d in graph.specialNodes:
            self.desks[d] = []

        self.actionCounter = 0
        self.options  = {
            'take': self.actionTake,
            'drop': self.actionDrop,
            'move': self.actionMove,
        }

    def addPackage(self, deskName, package):
        "Add a package at one desk"
        self.desks[deskName].append(package)

    def removePackage(self, deskName, package):
        self.desks[deskName].remove(package)

    def getDeskState(self, deskName):
        "Return the list of packages found at one desk"
        if self.graph.specialNodes.__contains__(deskName) is not True:
            return list()
        
        return self.desks[deskName]

    def getEnvironmnentState(self):
        "Return the collection of packages for all desks in the office"
        return dict([(desk, self.getDeskState(desk)) for desk in self.desks])

    def allDelivered(self):
        "Return True if all packages have been delivered"
        if len(self.agent.load) is not 0:
            return False
        for desk in self.desks:
            for package in self.desks[desk]:
                if package.destination is not desk:
                    return False
        return True

    def percept(self, agent):
        "Return the list of package at current agent position"
        return self.getDeskState(agent.position)

    def executeAction(self, agent, action, arg):
        "Agent executes the action. World state is changed to reflect this action."
        self.options[action](agent,arg)

    def step(self):
        "Run the environment for one time step. "
        if not self.allDelivered():
            (action, arg) = self.agent.chooseAction(self.percept(self.agent))
            self.actionCounter += 1
            self._showAction(action, arg)
            self.executeAction(self.agent, action, arg)
            self.agent.updateModel(action, self.percept(self.agent))

    def run(self, steps=1000):
        "Run the Environment for given number of time steps."
        while steps > 0:
            if self.allDelivered(): return
            self.step()
            steps -= 1

    def _showAction(self,action,arg):
        print self.actionCounter, ':',
 
        if action in ['take','drop']:
            print action, arg.id
        else:
            print action, arg
        
    def actionTake(self, agent, arg):
        agent.take(arg)
        self.removePackage(agent.position,arg)

    def actionDrop(self, agent, arg):
        addedPackages =  agent.find(lambda x:(False,True)[x.destination == agent.position])
        agent.drop(lambda x:(False,True)[x.destination == agent.position])
        for package in addedPackages:
            self.addPackage(agent.position,package)

    def actionMove(self, agent, arg):
        agent.move(arg)