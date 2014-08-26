from environment import *
from agent import *
from package import *


# --------------------------------
# A  2  B        5       C    3   D                  
# ----     -------------    ------
#    |     |           |    |
#    |     |           |    |
#    |  6  |           | 6  |
#    |     |           |    |
#    |      -----------     |
#    |   E       7       F  |
#    ------------------------

gr1 = Graph(['A','B','C','D','E','F'],
            [('A','B',2),('B','C',5),('C','D',3),('B','E',6),('E','F',7),('C','F',6)],
            ['A','D','E','F'])

agent = Agent(gr1,'A')
environment = Environment(gr1,agent) 

environment.addPackage('A',Package('F', 1, '4566'))
#environment.addPackage('E',Package('E', 1, '4567'))
environment.addPackage('A',Package('D', 5, '4568'))
environment.addPackage('D',Package('E', 2, '4569'))
environment.addPackage('A',Package('E', 1, '4570'))
#environment.addPackage('E',Package('E', 4, '4571'))
environment.addPackage('F',Package('A', 5, '4572'))
environment.addPackage('F',Package('A', 2, '4573'))

environment.addPackage('E',Package('F', 1, '1111'))
environment.addPackage('E',Package('A', 1, '1112'))
environment.addPackage('E',Package('D', 5, '1113'))
environment.addPackage('E',Package('A', 2, '1114'))
environment.addPackage('E',Package('D', 1, '115'))
environment.addPackage('E',Package('D', 4, '1'))
environment.addPackage('E',Package('A', 5, '2'))
environment.addPackage('E',Package('F', 2, '3'))

environment.addPackage('F',Package('D', 1, '4'))
environment.addPackage('F',Package('E', 1, '5'))
environment.addPackage('F',Package('D', 5, '6'))
environment.addPackage('F',Package('E', 2, '7'))
environment.addPackage('F',Package('E', 1, '8'))
environment.addPackage('F',Package('D', 4, '9'))
environment.addPackage('F',Package('A', 5, '10'))
environment.addPackage('F',Package('A', 2, '11'))

environment.addPackage('D',Package('F', 1, '13'))
environment.addPackage('D',Package('E', 1, '14'))
#environment.addPackage('D',Package('D', 5, '12'))
environment.addPackage('D',Package('F', 2, '15'))
environment.addPackage('D',Package('A', 1, '16'))
environment.addPackage('D',Package('E', 4, '17'))
environment.addPackage('D',Package('A', 5, '19'))
environment.addPackage('D',Package('F', 2, '22'))

environment.run()




