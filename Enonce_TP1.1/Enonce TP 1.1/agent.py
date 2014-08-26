#-*- coding:Utf-8 *-
class Agent:
    def __init__(self, graph, pos, weight = 10, maxLoad = 5, k = 1):
        self.graph = graph
        '''Position de l\'agent dans le graph''' 
        self.position = pos       
        '''Poids de l\'agent'''
        self.weight = weight      
        '''Poids max que l\'agent peut accepter'''
        self.maxLoad = maxLoad    
        '''Paquets que transporte l\'agent'''
        self.load = []            
        '''Poids du chargement'''
        self.loadWeight = 0       
        '''Energie depensé pour transporter le chargement'''
        self.wastedEnergy = 0     
        self.k = k

    def take(self, package):
        "Add one package to its load, if maximum weight is not reached"
        self.load.append(package)
        self.loadWeight += package.weight
        if self.loadWeight > self.maxLoad:
            raise RuntimeError


    def drop(self,condition):
        "Remove from load the packages that respect the condition"
        removedPackages =  self.find(condition)   
        self.load = filter(lambda x: not condition(x), self.load)  
        for p in removedPackages:
            self.loadWeight -= p.weight

    def getLoad(self):
        return self.load

    def find(self, condition):
        "Find the packages that respect the condition"
        return filter(condition,self.load)

    def move(self, newPosition):
        distance = self.graph.shortestPathLength(self.position, newPosition)
        self.position = newPosition
        self.wastedEnergy += self.k * distance * (self.loadWeight + self.weight) 

    def chooseAction(self, packageList):
        abstract

    def updateModel(self, action, packageList):
        abstract

    def isAgentHasPackagesWhichDestEqualPos(self,agentPackageList):
        if len(agentPackageList) is 0:
            return None
        for agentPackage in agentPackageList:
                if agentPackage.destination is self.position:
                    return agentPackage
        return None