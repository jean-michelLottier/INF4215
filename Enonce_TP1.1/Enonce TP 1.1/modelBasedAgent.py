#-*- coding:Utf-8 *-

from agent import *
from store import *
from random import random
from random import sample
from copy import copy

class ModelBasedAgent(Agent):
	def __init__(self, graph, pos):
		Agent.__init__(self, graph, pos, weight = 10, maxLoad = 5, k = 1)
		self.dataBases = []

	def chooseAction(self,packageList):
		'''si le comptoir n\'a pas de paquets'''
		'''print '----- method chooseAction -----'
		'''
		packageList = filter(lambda x: x.destination is not self.position, packageList)

		'''print '| packageList:'
		for package in packageList:
			package.show()
		print '------------------------------'
		'''
		
		if len(packageList) is 0:
			return self.case_1_PackageListEmpty()
		else:
			return self.case_2_PackageListNotEmpty(packageList,False,self.position)

	def case_1_PackageListEmpty(self):
		'''print '----- method case_1_PackageListEmpty -----'
		'''
		packageToDrop = self.isAgentHasPackagesWhichDestEqualPos(self.load)
		'''print '| packageToDrop:'
		if packageToDrop is not None: 
			packageToDrop.show() 
		else:
			print 'None'
		print '------------------------------'
		'''

		'''si l\'agent a des paquets à déposer pour le comptoir donné'''
		if packageToDrop is not None:
			return ('drop',packageToDrop)
		else:
			'''Si la BDD de l\'agent n\'est pas vide'''
			if len(self.dataBases) is not 0:
				return self.case_3_DataBasesNotEmpty()
			elif len(self.load) is not 0:
				newPosition = self.findBestDestination(self.load)
				return ('move',newPosition)
			else:
				return self.findBestDestinationByOnlyAgentPosition()

	def case_2_PackageListNotEmpty(self,packageList,isSimulation,simulationPos):
		'''print '----- method case_2_PackageListNotEmpty -----'
		print '| isSimulation:',isSimulation
		print '| simulationPos:',simulationPos
		print '| packageList:'
		for package in packageList:
			package.show()
		print '------------------------------'
		'''

		'''si l\'agent ne transporte pas de paquets'''
		if len(self.load) is 0:
			return self.case_2_1_LoadAgentEmpty(packageList,isSimulation,simulationPos)
		else:
			return self.case_2_2_LoadAgentNotEmpty(packageList,isSimulation,simulationPos)

	def case_2_1_LoadAgentEmpty(self,packageList,isSimulation,simulationPos):
		'''print '----- case_2_1_LoadAgentEmpty -----'
		print '| isSimulation:',isSimulation'''
		stores = self.storingPackagesByDestination(packageList)
		if isSimulation:
			pos = simulationPos
		else:
			pos = self.position
		'''print '| pos:',pos'''
		
		bestStore = None
		for store in stores:
			'''store.show()'''
			if store.name is pos:
				continue
			if bestStore is None \
			or store.getPackageNumber() > bestStore.getPackageNumber() \
			or (store.getPackageNumber() == bestStore.getPackageNumber() and store.totalLoadWeight < bestStore.totalLoadWeight) \
			or (store.getPackageNumber() == bestStore.getPackageNumber() and store.totalLoadWeight == bestStore.totalLoadWeight and self.graph.shortestPathLength(pos,store.name) < self.graph.shortestPathLength(pos,bestStore.name)):
				bestStore = store

		package = reduce(lambda x,y:x if x.weight < y.weight else y,bestStore.packages)

		'''print '------------------------------'
		'''
		return ('take',package)

	def case_2_2_LoadAgentNotEmpty(self,packageList,isSimulation,simulationPos):
		'''print '----- case_2_2_LoadAgentNotEmpty -----'
		print '| isSimulation:',isSimulation'''
		if isSimulation:
			pos = simulationPos
		else:
			pos = self.position
		'''print '| pos:',pos'''
			
		packageToDrop = self.isAgentHasPackagesWhichDestEqualPos(self.load)
		'''print '| packageToDrop:'
		if packageToDrop is not None: 
			packageToDrop.show() 
		else:
			print 'None'
		'''
		if packageToDrop is not None:
			return ('drop',packageToDrop)

		stores = self.storingPackagesByDestination(self.load)
		
		active = True
		while active:
			storeWithMaxPackagesIntoAgent = reduce(lambda x,y: x if x.getPackageNumber() > y.getPackageNumber() else y, stores)
			'''print '| storeWithMaxPackagesIntoAgent:',storeWithMaxPackagesIntoAgent.show()
			print '------------------------------'
			'''
			'''1: trouver un paquet dont la dest est la meme que storeWithMaxPackagesIntoAgent'''
			package1 = None
			package2 = None
			for currentPackage in packageList:
				if currentPackage.destination is pos:
					continue
				if currentPackage.destination is storeWithMaxPackagesIntoAgent.name and (package1 is None or currentPackage.weight < package1.weight):
					package1 = currentPackage
				if package2 is None or currentPackage.weight < package2.weight:
					package2 = currentPackage
			'''2: verifier si ajout de ce paquet ne va pas depasser le poids autorisé'''
			if package1 is not None and (package1.weight + self.loadWeight) < self.maxLoad:
				return ('take',package1)
			
			if len(stores) > 1:
				stores.remove(storeWithMaxPackagesIntoAgent)
			else:
				active = False

		'''3: si le paquet ne convient pas alors trouver le paquet dans packageList dont le poids est le plus petit possible'''
		'''4: verifier si ajout de ce paquet ne va pas depasser le poids autorisé'''
		if package2 is not None and (package2.weight + self.loadWeight) < self.maxLoad:
			return ('take',package2)
		'''5: si le paquet ne convient pas alors faire un move'''
		if isSimulation is True:
			return None
		elif len(self.dataBases) is not 0:
			return self.case_3_DataBasesNotEmpty()
		else: 
			newPosition = self.findBestDestination(self.load)
			return ('move',newPosition)


	def case_3_DataBasesNotEmpty(self):
		print '----- case_3_DataBasesNotEmpty -----'
		
		weightProbability = (self.loadWeight / self.maxLoad)
		takeProbability = 1 - weightProbability
		dropProbability = weightProbability

		for store in self.dataBases:
			'''print '| store:',store.show()'''
			if store.name is self.position:
				continue
			nbDrop = 0
			nbTake = 0
			copyAgent = copy(self)
			copyStore = copy(store)
			isSimulationNotDone = True

			while isSimulationNotDone:
				result = copyAgent.case_2_PackageListNotEmpty(copyStore.packages,True,copyStore.name)
				if result is None:
					print '| case 3 - result is None'
					isSimulationNotDone = False
				elif result[0] is 'drop':
					print '| case 3 - result is drop'
					nbDrop += 1
					copyAgent.load.remove(result[1])
					copyAgent.loadWeight -= result[1].weight
				else:
					print '| case 3 - result is take'
					nbTake += 1
					copyAgent.take(result[1])
					copyStore.removePackage(result[1])
			
			store.actionsWeight = nbDrop*dropProbability + nbTake*takeProbability
			print '| case 3 - store:',store.name,' actionsWeight:',store.actionsWeight

		bestStore = reduce(lambda x,y: x if x.actionsWeight > y.actionsWeight else y, self.dataBases)
		newPosition = bestStore.name
		if bestStore.name is self.position or bestStore.actionsWeight is 0:
			newPosition = self.findBestDestination(self.load)

		for store in self.dataBases:
			store.actionsWeight = 0

		print '------------- END case 3 ---------------'
		return ('move',newPosition)


	def storingPackagesByDestination(self, packageList):
		stores = []
		
		for package in packageList:
			result = filter(lambda x: x.name is package.destination,stores)
			if len(result) is not 0:
				result[0].addPackage(package)
				result[0].totalLoadWeight += package.weight
			else:
				newStore = Store(package.destination,[package],package.weight)
				stores.append(newStore)

		return stores

	def updateModel(self, action, packageList):
		print '----- updateModel -----'
		print '| action:',action
		if action is 'move' or action is 'drop':
			return

		tmp = filter(lambda x: (False,True)[x.name is self.position],self.dataBases)
		packageList = filter(lambda x: x.destination is not self.position, packageList)
		'''print '| packageList (without package -> destination = position):'
		for package in packageList:
			package.show()
		'''
		
		if len(packageList) is 0 and len(tmp) is not 0:
			print '| remove (plus de paquet a traiter):',tmp[0].show()
			self.dataBases.remove(tmp[0])
			print '------------------------------'
			return

		if len(packageList) is 0 and len(tmp) is 0:
			print '| remove NOTHING (packageList = None & tmp = None)'
			print '------------------------------'
			return
		
		if len(tmp) == 0:
			totalPackagesWeight = sum(package.weight  for package in packageList)
			store = Store(self.position,packageList,totalPackagesWeight)
			print '| add a store into BDD:',store.show()
			self.dataBases.append(store)
		else:
			'''print '| tmp[0] (avant reduction de la liste de paquets):',tmp[0].show()'''
			copyTmp = copy(tmp[0])
			for package in copyTmp.packages:
				if packageList.__contains__(package) is False:
					tmp[0].removePackage(package)
					tmp[0].totalLoadWeight -= package.weight
				else:
					print 'paquet {} supprimé de packageList'.format(package.id)
					packageList.remove(package)
			for package in packageList:
				if tmp[0].packages.__contains__(package): continue
				print 'paquet {} ajouté de packageList à tmp[0]'.format(package.id)
				tmp[0].addPackage(package)
				tmp[0].totalLoadWeight += package.weight

			print '| remove packageList into store:',tmp[0].show()
		print '------------------------------'

	def findBestDestinationByOnlyAgentPosition(self):
		bestDestination = ''
		pathLength = -1

		for destination in self.graph.specialNodes:
			if destination is self.position:
				continue

			tmpVal = self.graph.shortestPathLength(self.position,destination)
			if pathLength is -1 or tmpVal < pathLength:
				bestDestination = destination
				pathLength = tmpVal

		isBestDestNotCorrect = True
		while isBestDestNotCorrect:
			if random() < 0.2:
				bestDestination = sample(self.graph.specialNodes,1)
			if bestDestination is not self.position:
				isBestDestNotCorrect = False

		return ('move',bestDestination[0])

	def findBestDestination(self, agentPackageList):
	    if len(agentPackageList) is 0:
	        result = self.findBestDestinationByOnlyAgentPosition()
	        return result[1]

	    destList = {}
	    for agentPackage in agentPackageList:
	        if destList.__contains__(agentPackage.destination):
	            destList[agentPackage.destination] += 1
	        else:
	            destList[agentPackage.destination] = 1

	    bestDestList = [(0,'A')]
	    for x in destList:
	        if destList[x] > bestDestList[0][0]:
	            bestDestList = list()
	            bestDestList.append((destList[x],x))
	        elif destList[x] is bestDestList[0][0]:
	            bestDestList.append((destList[x],x))

	    if len(bestDestList) is 1:
	        return bestDestList[0][1]
	    else:
	        destination = (100000,'A')
	        for x in bestDestList:
	            pathLength = self.graph.shortestPathLength(self.position,x[1])
	            if pathLength <= destination[0]:
	                destination = (pathLength,x[1])
	        return destination[1]
