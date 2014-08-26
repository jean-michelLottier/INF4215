from environment import *
from agent import *
from package import *


#            A
#          |  |
#          | 2|
#          |  |
#     -----    ------------
#    B  3   C   3  D    4  E
#     ------------    -----
#                 |  |
#                 | 4|
#                 |  |
#                   F


gr1 = Graph(['A','B','C','D','E','F'],
            [('A','C',2),('B','C',3),('C','D',3),('D','E',4),('D','F',4)],
            ['A','B','E','F'])

#agent = ReflexAgent(gr1,'B')
agent = Agent(gr1,'B')
environment = Environment(gr1,agent) 

environment.addPackage('F',Package('A', 1, '4566'))
environment.addPackage('F',Package('A', 1, '4567'))
environment.addPackage('F',Package('A', 5, '4568'))
environment.addPackage('F',Package('A', 2, '4569'))
environment.addPackage('F',Package('A', 1, '4570'))
environment.addPackage('F',Package('A', 4, '4571'))
environment.addPackage('F',Package('A', 5, '4572'))
environment.addPackage('F',Package('B', 2, '4573'))
environment.addPackage('F',Package('B', 2, '2102'))
environment.addPackage('F',Package('B', 2, '2103'))
environment.addPackage('F',Package('B', 2, '2104'))
environment.addPackage('F',Package('B', 2, '2105'))
environment.addPackage('F',Package('B', 2, '2106'))
environment.addPackage('F',Package('B', 2, '2107'))
environment.addPackage('F',Package('B', 2, '2108'))
environment.addPackage('F',Package('B', 2, '2109'))
environment.addPackage('F',Package('B', 2, '2110'))
environment.addPackage('F',Package('B', 2, '2111'))
environment.addPackage('F',Package('E', 2, '2112'))
environment.addPackage('F',Package('E', 2, '2113'))
environment.addPackage('F',Package('E', 2, '2114'))
environment.addPackage('F',Package('E', 2, '2115'))
environment.addPackage('F',Package('E', 2, '2116'))
environment.addPackage('F',Package('E', 1, '6700'))
environment.addPackage('F',Package('E', 2, '6701'))
environment.addPackage('F',Package('E', 1, '6702'))
environment.addPackage('F',Package('E', 1, '6703'))
environment.addPackage('F',Package('A', 1, '6704'))
environment.addPackage('F',Package('A', 2, '6705'))
'''environment.addPackage('F',Package('A', 1, '6706'))
environment.addPackage('F',Package('A', 1, '6707'))
environment.addPackage('F',Package('A', 1, '6708'))
environment.addPackage('F',Package('A', 2, '6709'))
environment.addPackage('F',Package('E', 1, '6710'))
environment.addPackage('F',Package('E', 1, '6711'))
environment.addPackage('F',Package('E', 1, '6712'))
environment.addPackage('F',Package('E', 2, '6713'))
environment.addPackage('F',Package('E', 1, '6714'))
environment.addPackage('F',Package('E', 1, '6715'))
environment.addPackage('F',Package('E', 1, '1165'))
environment.addPackage('F',Package('E', 2, '1166'))
environment.addPackage('F',Package('A', 1, '1167'))
environment.addPackage('F',Package('A', 1, '1166'))
environment.addPackage('F',Package('A', 2, '1167'))
environment.addPackage('F',Package('A', 1, '1168'))
environment.addPackage('F',Package('B', 1, '1169'))
environment.addPackage('F',Package('B', 2, '1170'))
environment.addPackage('F',Package('B', 1, '1171'))
environment.addPackage('F',Package('B', 1, '1172'))
environment.addPackage('F',Package('B', 2, '1173'))
environment.addPackage('F',Package('B', 1, '1174'))
environment.addPackage('F',Package('B', 1, '1175'))
environment.addPackage('F',Package('B', 2, '1176'))
environment.addPackage('F',Package('B', 1, '1177'))
environment.addPackage('F',Package('A', 1, '1178'))
environment.addPackage('F',Package('A', 2, '1179'))
environment.addPackage('F',Package('A', 1, '1180'))
environment.addPackage('F',Package('A', 1, '1181'))
environment.addPackage('F',Package('A', 2, '1182'))
environment.addPackage('F',Package('A', 1, '1183'))
environment.addPackage('F',Package('E', 1, '1184'))
environment.addPackage('F',Package('E', 2, '1185'))
environment.addPackage('F',Package('E', 1, '1186'))
environment.addPackage('F',Package('E', 1, '1187'))
environment.addPackage('F',Package('B', 2, '1188'))
environment.addPackage('F',Package('B', 1, '1189'))
'''
environment.run()




