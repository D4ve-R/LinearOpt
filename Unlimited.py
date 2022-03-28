# g1: y = x + 1
# g2: y = x/2 - 1/2
# x >= 0, y >= 0
# Schnittpunkt berechnen: 
# x = - 3
# x liegt außerhalb des Definitionsbereich
# Die Geraden haben keinen Schnittpunkt im 1. Quadrant (Definitionsbereich)

from pulp import *
import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(-4, 4, 8)
fig, ax = plt.subplots()

# coordinate system style
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.plot(x, x + 1, color='blue')
ax.plot(x, x/2 - 1/2, color='green')
ax.plot(x, -2*x/3, color='red')
ax.grid()

plt.suptitle('Unlimited')
plt.show()

prob = LpProblem('Unlimited', LpMaximize)
x1 = LpVariable('x', 0)
y = LpVariable('y', 0)
prob.setObjective(2 * x1 - 3 * y)
prob += - x1 + y <= 1
prob += x1 - 2 * y <= 1
prob.solve()

print("Status: ", LpStatus[prob.status], "\n")
if(prob.status):
    print(20*"#")
    print("x: ", value(x1))
    print("y: ", value(y))
    print(20*"-")
    print("Objective value: ", pulp.value(prob.objective))
    print(20*"#")


