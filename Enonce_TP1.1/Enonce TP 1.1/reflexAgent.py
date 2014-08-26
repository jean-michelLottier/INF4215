from agent import *

class ReflexAgent(Agent):
    def __init__(self, graph, pos):
        Agent.__init__(self, graph, pos, weight = 10, maxLoad = 5, k = 1)
        self.options = {
        	'A':'E',
        	'E':'F',
        	'F':'B',
        	'B':'A',
        }

    def chooseAction(self, packageList):
    	print 'TEST1:',len(packageList) 
    	packageToDrop = self.isAgentHasPackagesWhichDestEqualPos(self.load)
    	if len(packageList) is 0:
    		if packageToDrop is not None:
    			return ('drop',packageToDrop)
    		else:
    			newPosition = self.findBestDestination(self.load)
    			return ('move',newPosition)
    	else:
    		print 'TEST3: packageList is not None'
    		package = self.isExistPackagePosAndAgentPosDif(packageList)
    		if package is not None and (package.weight + self.loadWeight) < self.maxLoad:
    			return ('take',package)
    		elif packageToDrop is not None:
    			return ('drop',packageToDrop)
    		else:
    			newPosition = self.findBestDestination(self.load)
    			return ('move',newPosition)

    def isExistPackagePosAndAgentPosDif(self,packageList):
    	result = filter(lambda x:(False,True)[x.destination is not self.position],packageList)
    	if len(result) is not 0:
    		return reduce((lambda x,y: x if x.weight < y.weight else y),result)
    	return None

    def findNextDestination(self):
    	print 'agent position:',self.position, ' next position:',self.options[self.position]
    	return self.options[self.position]

    def updateModel(self, action, packageList):
    	pass

    def findBestDestination(self, agentPackageList):
        if len(agentPackageList) is 0:
            print 'TEST2: agentPackageList is 0'
            return self.findNextDestination()

        destList = {}
        for agentPackage in agentPackageList:
            if destList.__contains__(agentPackage.destination):
                destList[agentPackage.destination] += 1
            else:
                destList[agentPackage.destination] = 1
        print 'show destList:',destList
        '''bestDestList = {nbrPaquets:destination}'''
        bestDestList = [(0,'A')]
        for x in destList:
            if destList[x] > bestDestList[0][0]:
                bestDestList = list()
                bestDestList.append((destList[x],x))
            elif destList[x] is bestDestList[0][0]:
                bestDestList.append((destList[x],x))
        print 'show bestDestList:',bestDestList
        if len(bestDestList) is 1:
            return bestDestList[0][1]
        else:
            destination = (1000,'A')
            for x in bestDestList:
                pathLength = self.graph.shortestPathLength(self.position,x[1])
                if pathLength <= destination[0]:
                    destination = (pathLength,x[1])
            return destination[1]