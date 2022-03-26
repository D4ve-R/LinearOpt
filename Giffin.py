from pulp import *
import matplotlib.pyplot as plt
import numpy as np

prob = LpProblem("giffin", LpMinimize)
x_B = LpVariable("x_B", 0)
x_Z = LpVariable("x_Z", 0)

timeBoat = 2
timeTrain = 1
priceBoat = 5
priceTrain = 10
maxMoney = 300
minDist = 40

prob.setObjective(timeBoat * x_B + timeTrain * x_Z)
prob += priceBoat * x_B + priceTrain * x_Z <= maxMoney
prob += x_B + x_Z >= minDist

prob.solve()

print("Status: ", LpStatus[prob.status], "\n")
if(prob.status):
    print(20*"#")
    print("Boot km x: ", value(x_B))
    print("Zug km x: ", value(x_Z))
    print(20*"-")
    print("Objective value: ", pulp.value(prob.objective))
    print(20*"#")

x= np.linspace(0,50)
fig, axs = plt.subplots(2)
fig.suptitle('Giffin Paradox')
axs[0].plot(x, -x + minDist, color='green')
axs[0].plot(x, -(priceBoat/priceTrain)*x+(maxMoney/priceTrain), color='blue')
axs[0].grid()
axs[1].plot(x, -x + minDist, color='green')
axs[1].plot(x, -((priceBoat+1)/priceTrain)*x+(maxMoney/priceTrain), color='blue')
axs[1].grid()
plt.show()
