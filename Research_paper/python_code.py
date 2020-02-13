#this is not complete code. Some assumptions were modified to reduce no of variables

import pulp as p

Z_max = p.LpProblem("profit_maximising_problem", p.LpMaximize)

days=list(range(4))

# Y = p.LpVariable.dicts("y",days ,lowBound=0,upBound=13800,cat='Integer')
# S = p.LpVariable.dicts("S",days ,lowBound=0,cat='Integer')
# J = p.LpVariable.dicts("J",days ,lowBound=0,upBound=12,cat='Integer')
# R = p.LpVariable.dicts("R",days ,lowBound=0,upBound=300,cat='Integer')
# T = p.LpVariable.dicts("T",days ,lowBound=0,cat='Integer')

Y_1 = p.LpVariable("Y_1",lowBound=0,upBound=13800,cat='Integer')
Y_2 = p.LpVariable("Y_2",lowBound=0,upBound=13800,cat='Integer')
Y_3 = p.LpVariable("Y_3",lowBound=0,upBound=13800,cat='Integer')
Y_4 = p.LpVariable("Y_4",lowBound=0,upBound=13800,cat='Integer')

S_1 = p.LpVariable("S_1",lowBound=0,cat='Integer')
S_2 = p.LpVariable("S_2",lowBound=0,cat='Integer')
S_3 = p.LpVariable("S_3",lowBound=0,cat='Integer')
S_4 = p.LpVariable("S_4",lowBound=0,cat='Integer')

J_1 = p.LpVariable("J_1",lowBound=0,upBound=12,cat='Integer')
J_2 = p.LpVariable("J_2",lowBound=0,upBound=12,cat='Integer')
J_3 = p.LpVariable("J_3",lowBound=0,upBound=12,cat='Integer')
J_4 = p.LpVariable("J_4",lowBound=0,upBound=12,cat='Integer')

R_1 = p.LpVariable("R_1",lowBound=0,upBound=300,cat='Integer')
R_2 = p.LpVariable("R_2",lowBound=0,upBound=300,cat='Integer')
R_3 = p.LpVariable("R_3",lowBound=0,upBound=300,cat='Integer')
R_4 = p.LpVariable("R_4",lowBound=0,upBound=300,cat='Integer')

T_1 = p.LpVariable("T_1",lowBound=0,cat='Integer')
T_2 = p.LpVariable("T_2",lowBound=0,cat='Integer')
T_3 = p.LpVariable("T_3",lowBound=0,cat='Integer')
T_4 = p.LpVariable("T_4",lowBound=0,cat='Integer')

Z_max += 1000 * 222 *(S_1+S_2+S_3+S_4) + 25 * 270 * (J_1+J_2+J_3+J_4)


Z_max += Y_1 ==12000 + 1000 * (20 +40) *(S_1 -T_1)
# for i in range(1,4):
Z_max += R_1 ==25 * J_1
Z_max += S_1 + R_1 ==3000
Z_max += S_1 ==3000

Z_max += R_2 ==25 * J_2
Z_max += S_2 + R_2 ==3000
Z_max += S_2 ==3000
Z_max = Y_2 = Y_1 + 1000 * (20+40)*(S_2-T_2)
Z_max += S_2 ==3000

Z_max += R_3 ==25 * J_3
Z_max += S_3 + R_3 ==3000
Z_max += S_3 ==3000
Z_max = Y_3 = Y_2 + 1000 * (20+40)*(S_3-T_3)
Z_max += S_3 ==3000

Z_max += R_4 ==25 * J_4
Z_max += S_4 + R_4 ==3000
Z_max += S_4 ==3000
Z_max = Y_4=Y_3 + 1000 * (20+40)*(S_4-S_1)
Z_max = S_1 = 1000 * (20 + 40)  * T_4

status = Z_max.solve()
print(p.LpStatus[status])

