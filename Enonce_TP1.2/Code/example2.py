from environment import *
from agent import *
from package import *


# ------------------------------------------------------------
# A     2     B      3       C       4        D    2    E
# ----------------------------------------------------------

gr1 = Graph(['A','B','C','D','E'],
            [('A','B',2),('B','C',3),('C','D',4),('D','E',2)],
            ['A','B', 'C', 'D','E'])

agent = Agent(gr1,'A')
environment = Environment(gr1,agent) 

environment.addPackage('A',Package('D', 1, '4566'))
environment.addPackage('A',Package('E', 1, '4567'))
environment.addPackage('A',Package('B', 5, '4568'))
environment.addPackage('A',Package('B', 2, '4569'))
environment.addPackage('A',Package('E', 1, '4570'))
environment.addPackage('A',Package('E', 4, '4571'))
environment.addPackage('A',Package('C', 5, '4572'))
environment.addPackage('A',Package('B', 2, '4573'))
environment.addPackage('B',Package('E', 2, '2102'))
environment.addPackage('B',Package('A', 2, '2103'))
environment.addPackage('B',Package('A', 2, '2104'))
environment.addPackage('B',Package('E', 2, '2105'))
environment.addPackage('B',Package('A', 2, '2106'))
environment.addPackage('B',Package('A', 2, '2107'))
environment.addPackage('B',Package('C', 2, '2108'))
environment.addPackage('B',Package('A', 2, '2109'))
environment.addPackage('B',Package('A', 2, '2110'))
environment.addPackage('B',Package('E', 2, '2111'))
environment.addPackage('B',Package('A', 2, '2112'))
environment.addPackage('B',Package('A', 2, '2113'))
'''environment.addPackage('B',Package('D', 2, '2114'))
environment.addPackage('B',Package('A', 2, '2115'))
environment.addPackage('B',Package('A', 2, '2116'))
environment.addPackage('E',Package('B', 1, '6700'))
environment.addPackage('E',Package('B', 2, '6701'))
environment.addPackage('E',Package('B', 1, '6702'))
environment.addPackage('E',Package('A', 1, '6703'))
environment.addPackage('E',Package('A', 1, '6704'))
environment.addPackage('E',Package('B', 2, '6705'))
environment.addPackage('E',Package('C', 1, '6706'))
environment.addPackage('E',Package('A', 1, '6707'))
environment.addPackage('E',Package('B', 1, '6708'))
environment.addPackage('E',Package('B', 2, '6709'))
environment.addPackage('E',Package('B', 1, '6710'))
environment.addPackage('E',Package('A', 1, '6711'))
environment.addPackage('E',Package('D', 1, '6712'))
environment.addPackage('E',Package('B', 2, '6713'))
environment.addPackage('E',Package('A', 1, '6714'))
environment.addPackage('E',Package('A', 1, '6715'))
environment.addPackage('C',Package('A', 1, '1165'))
environment.addPackage('C',Package('B', 2, '1166'))
environment.addPackage('C',Package('E', 1, '1167'))
environment.addPackage('C',Package('A', 1, '1166'))
environment.addPackage('C',Package('B', 2, '1162'))
environment.addPackage('C',Package('E', 1, '1168'))
environment.addPackage('C',Package('A', 1, '1169'))
environment.addPackage('C',Package('B', 2, '1170'))
environment.addPackage('C',Package('E', 1, '1171'))
environment.addPackage('C',Package('A', 1, '1172'))
environment.addPackage('C',Package('B', 2, '1173'))
environment.addPackage('C',Package('E', 1, '1174'))
environment.addPackage('C',Package('A', 1, '1175'))
environment.addPackage('C',Package('B', 2, '1176'))
environment.addPackage('C',Package('E', 1, '1177'))
environment.addPackage('C',Package('A', 1, '1178'))
environment.addPackage('C',Package('B', 2, '1179'))
environment.addPackage('C',Package('E', 1, '1180'))
environment.addPackage('C',Package('A', 1, '1181'))
environment.addPackage('C',Package('B', 2, '1182'))
environment.addPackage('C',Package('E', 1, '1183'))
environment.addPackage('C',Package('A', 1, '1184'))
environment.addPackage('C',Package('B', 2, '1185'))
environment.addPackage('C',Package('E', 1, '1186'))
environment.addPackage('C',Package('A', 1, '1187'))
environment.addPackage('C',Package('B', 2, '1188'))
environment.addPackage('C',Package('E', 1, '1189'))
environment.addPackage('D',Package('A', 1, '8172'))
environment.addPackage('D',Package('B', 2, '2312'))
environment.addPackage('D',Package('E', 1, '7655'))
environment.addPackage('D',Package('A', 1, '8888'))
environment.addPackage('D',Package('B', 2, '7777'))
environment.addPackage('D',Package('E', 1, '1124'))
'''
environment.run()




