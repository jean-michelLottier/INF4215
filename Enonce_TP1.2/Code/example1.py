from environment import *
from agent import *
from package import *


#            A
#          |  |
#          | 2|
#          |  |
#     -----    ------------
#    B  3   C   3  D    4  E
#     ---    -----    -----
#        |  |     |  |
#        | 5|     | 4|
#        |  |       F 
#        |  |   
#     ---    -----
#    G  3  H   4   I
#     ------------
#        

gr1 = Graph(['A','B','C','D','E','F','G','H','I'],
            [('A','C',2),('B','C',3),('C','D',3),('D','E',4),('D','F',4),('C','H',5),('G','H',3),('H','I',4)],
            ['A','B','E','F','G','I'])

agent = Agent(gr1,'A')
environment = Environment(gr1,agent) 
environment.addPackage('B',Package('F', 2, '2102'))
environment.addPackage('B',Package('A', 2, '5431'))
environment.addPackage('B',Package('A', 3, '1873'))
environment.addPackage('F',Package('B', 3, '2317'))
environment.addPackage('G',Package('E', 3, '2312'))
environment.addPackage('I',Package('G', 3, '2232'))

'''
gr1 = Graph(['A','B','C','D','E','F'],
            [('A','C',2),('B','C',3),('C','D',3),('D','E',4),('D','F',4)],
            ['A','B','E','F'])

agent = Agent(gr1,'A')
environment = Environment(gr1,agent) 
environment.addPackage('B',Package('A', 2, '5431'))
environment.addPackage('B',Package('A', 3, '1873'))
environment.addPackage('F',Package('B', 3, '2317'))
environment.addPackage('A',Package('E', 3, '2312'))
'''

environment.run()





