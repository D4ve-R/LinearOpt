# min sum(x)
# s.t. 3x0 + 4x2 + x5 >= 100
#      x0 + x3 + x4 + x5 >= 125
#      3x1 + 2x3 + x4 + 2x5 >= 80 

from pulp import *
#maxLength = 105
rollLengths = [ 25, 30, 35]
demand = [100, 125, 80]
#310
#003
#400
#012
#021
#102
#030
patterns = [[3,0,4,0,0,1,0],
           [1,0,0,1,2,0,3],
           [0,3,0,2,1,2,0],
]
var = ['A','B','C', 'D', 'E', 'F', 'H']

prob = LpProblem("cuttingStock", LpMinimize)
lpVars = LpVariable.dicts('Patt_', var, 0,cat='Integer')

prob.setObjective(lpSum([lpVars[i] for i in var]))

for i in range(len(rollLengths)):
    prob += lpSum([lpVars[var[m]] * patterns[i][m] for m in range(len(var))]) >= demand[i]

prob.solve()
print("Status: ", LpStatus[prob.status], "\n")
if(prob.status):
    print(20*"#")
    for i in var:
        print(f"Patt_{i} : ", value(lpVars[i]))
    print(20*"-")
    print("Base rolls needed: ", pulp.value(prob.objective))
    print(20*"-")
    rolls = [0,0,0]
    for j in range(len(rolls)):
        for i in range(len(var)):
            rolls[j] += patterns[j][i] * value(lpVars[var[i]])
        print(rolls[j])
    print(20*"#")

