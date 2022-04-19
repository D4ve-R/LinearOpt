from pulp import * 
x = [1,2,3]
prob = LpProblem('test', LpMaximize)
x = LpVariable.dicts('x_', x, 0)
prob.setObjective(x[1] - x[2] + x[3])
prob += 2*x[1] - x[2] + 2*x[3] <= 4
prob += 2*x[1] - 3*x[2] + x[3] <= -5
prob += -1*x[1] + x[2] - 2*x[3] <= -1
prob.solve()

print("Status: ", LpStatus[prob.status], "\n")
if(prob.status):
    print(20*"#")
    print("obj val: ", value(prob.objective))
    print(20*"-")
    [print(f"x_{i}:", value(x[i])) for i in range(1,len(x)+1)]
    print(20*"#")
