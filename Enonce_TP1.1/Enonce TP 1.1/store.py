class Store:
	def __init__(self,name,packageList,totalLoadWeight):
		self.name = name
		self.packages = packageList
		self.totalLoadWeight = totalLoadWeight
		self.visitCpt = 0
		
		self.actionsWeight = 0

	def addPackage(self,package):
		self.packages.append(package)

	def addPackages(self,packageList):
		self.packages + packageList

	def removePackage(self,package):
		self.packages.remove(package)

	def removePackages(self,packageList):
		for package in packageList:
			self.removePackage(package)

	def containsPackage(self,package):
		return self.packages.__contains__(package)

	def getPackageNumber(self):
		return len(self.packages)

	def show(self):
		print '------ store :',self.name,'------'
		if len(self.packages) is 0:
			print '| package list: None'
		else:
			print '| package list:'
			for package in self.packages:
				package.show()
		print '| totalLoadWeight:',self.totalLoadWeight
		print '| actionsWeight:',self.actionsWeight
		print '------------------------------'