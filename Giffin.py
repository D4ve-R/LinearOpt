from pulp import *

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
