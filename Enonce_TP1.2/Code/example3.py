from environment import *
from agent import *
from package import *

#
#                                                                                       Z
#                                                                                     |   |
#                                                                                     | 2 |
#                                                                                     |   |
#                                              ---------------------------------------    |
#                                             V       5        W     2     X     3      Y |
#                                              --------------      ------     --------    |
#                                                           /    /        \   \       |   |
#                                                          /    /          \ 3 \      | 4 |
#                                                         /    /            \   \     |   |
#                                                        /  4 /              \   -----    |
#                                                       /    /               | AB  2   AA |
#                              ------------------------     /               /   ----------
#                             O    1   N       2       L   /               / 2 /
#                      Q       ------     -----------     /               /   /
#                    |   |           |   |           |   |                 AC
#                    | 1 |           | 1 |           | 1 |
#                    |   |           |   |           |   |
#     ---------------     -----------     -----------     ---------
#    S   1   R    2    P      2        M        3      K     1   J |
#     -----     -----     -----------     ---------------------    |
#          |   |     |   |           |   |                     |   |
#          |   |     |   |           |   |                     | 3 |
#          |   |     |   |           | 5 |                     |   |
#          |   |     |   |           |   |                     |    -------
#          | 2 |     | 6 |           |   |                     | T     2   U
#          |   |     |   |            AD                       |    -------
#          |   |     |   |                                     |   |
#          |   |     |   |                                     | 3 |
#     -----     -----     -------------------------------------    |
#    A  2    B  2      D                      8                  I |                  
#     -----     -----         -------------------------------------
#          |   |     |   |\   \
#          | 3 |     | 4 | \ 5 \
#          |   |     |   |  \   \
#            C         E     \   ------
#                            | F    4   H
#                            |    -----
#                            | 3 |
#                            |   |
#                              G

gr1 = Graph(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','AA','AB','AC','AD'],
            [('A','B',2),('B','C',3),('B','R',2),('B','D',2),('D','E',4),('D','F',5),
             ('D','P',6),('D','I',8),('F','G',3),('F','H',4),('I','T',3),('T','U',2),
             ('T','J',3),('J','K',1),('K','L',1),('K','M',3),('M','N',1),('N','O',1),
             ('M','P',2),('P','Q',1),('P','R',2),('R','S',1),('L','W',4),('V','W',5),
             ('W','X',2),('X','Y',3),('X','AB',3),('Y','Z',2),('Y','AA',4),('AA','AB',2),
             ('AB','AC',2),('M','AD',5)],
            ['A','C','E','H','I','U','L','O','Q','S','V','Z','AC','AD'])

agent = Agent(gr1, 'AD')
environment = Environment(gr1, agent)

environment.addPackage('A', Package('E', 2, '1000'))
environment.addPackage('A', Package('E', 2, '1001'))
environment.addPackage('H', Package('C', 3, '1002'))
environment.addPackage('E', Package('H', 3, '1003'))
environment.addPackage('C', Package('H', 2, '1004'))
environment.addPackage('U', Package('I', 2, '1005'))
environment.addPackage('L', Package('U', 3, '1006'))
environment.addPackage('Q', Package('U', 3, '1007'))
environment.addPackage('A', Package('U', 2, '1008'))
environment.addPackage('A', Package('L', 2, '1009'))

environment.addPackage('V', Package('AC', 2, '1010'))
environment.addPackage('V', Package('Q', 2, '1011'))
environment.addPackage('Z', Package('O', 2, '1012'))
environment.addPackage('AC', Package('C', 2, '1013'))
environment.addPackage('AC', Package('O', 2, '1014'))
environment.addPackage('AC', Package('O', 2, '1015'))
environment.addPackage('AD', Package('L', 2, '1016'))
environment.addPackage('AD', Package('V', 2, '1017'))
environment.addPackage('AD', Package('A', 2, '1018'))

environment.addPackage('E', Package('AC', 2, '1019'))
environment.addPackage('E', Package('Q', 2, '1020'))
environment.addPackage('E', Package('O', 2, '1021'))
environment.addPackage('H', Package('C', 2, '1022'))
environment.addPackage('H', Package('A', 2, '1023'))
environment.addPackage('S', Package('U', 2, '1024'))
environment.addPackage('Z', Package('C', 2, '1025'))
environment.addPackage('L', Package('E', 2, '1026'))
environment.addPackage('O', Package('A', 2, '1027'))

environment.run()