# max x + y
# s.t. ax + by <= 1
#       x, y   >= 0
#
# infeasible: a,b < 0
# unlimited: a < 0, b > 0
# one solution: a,b > 0 && (a != b) 
# multiple solutions: a = b && a,b > 0

import sys
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np
from pulp import * 

def target(x):
    return -x

# a,b = -1
def infeasible(x):
    return -x - 1

# a = -1, b = 1
def unlimited(x):
    return x + 1

# a = 1, b = 2
def oneSol(x):
    return -x/2 + 1/2

# a,b = 1
def multSol(x):
    return -x + 1

x = np.array([-2, -1, 0, 1, 2])

fig, axs = plt.subplots(2,2)
fig.suptitle('Parameterized Lp')

for i in range(2):
    for j in range(2):
        axs[i][j].plot(x, target(x), color='red')
        axs[i][j].spines['bottom'].set_position('zero')
        axs[i][j].spines['left'].set_position('zero')
        axs[i][j].spines['top'].set_visible(False)
        axs[i][j].spines['right'].set_visible(False)
        axs[i][j].grid()

axs[0][0].plot(x, infeasible(x), color='violet')
axs[0][0].set_title('Infeasible')
verts = [(0,0), (2,0),(2,2),(0,2)]
axs[0][0].add_patch(Polygon(verts, color='pink'))
verts = [(-2,1), (2,-3),(-2,-3)]
axs[0][0].add_patch(Polygon(verts, color='pink'))

axs[0][1].plot(x, unlimited(x), color='yellow')
axs[0][1].set_title('Unlimited')
verts = [(0,0), (2,0),(2,3),(0,1)]
axs[0][1].add_patch(Polygon(verts, color='pink'))

axs[1][0].plot(x, oneSol(x), color='green')
axs[1][0].set_title('One solution')
verts = [(0,0), (1,0),(0,1/2)]
axs[1][0].add_patch(Polygon(verts, color='pink'))

axs[1][1].plot(x, multSol(x), color='blue')
axs[1][1].set_title('Multiple solutions')
verts = [(0,0), (1,0),(0,1)]
axs[1][1].add_patch(Polygon(verts, color='pink'))

plt.show()

if len(sys.argv) > 1:
    prob = LpProblem('para', LpMaximize)
    x = LpVariable('x', 0)
    y = LpVariable('y', 0)
    prob.setObjective(x+y)
    if sys.argv[1] == 'mult':
        prob += x + y <= 1
        prob.solve()
    if sys.argv[1] == 'unbounded':
        prob += -x + y <= 1
        prob.solve()
    if sys.argv[1] == 'infeasible':
        prob += -x - y <= 1
        prob.solve()
    if sys.argv[1] == 'one':
        prob += x + 2 * y <= 1
        prob.solve()

    print(LpStatus[prob.status], '\n')
    if(prob.status):
        print("objective value: ", value(prob.objective))
        print(f"x: {value(x)}")
        print(f"y: {value(y)}")
