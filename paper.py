# solution for problem 7.8 from https://github.com/gadepall/school/blob/master/ncert/optimization/gvv_ncert_opt.pdf
import pulp as p

Z_max = p.LpProblem("profit_maximising_problem", p.LpMaximize)

days=list(range(30))
# x = p.LpVariable("x", lowBound=0)
# y = p.LpVariable("y", lowBound=0)


# profit += 10500 * x + 9000 * y
# profit += x + y == 50
# profit += 20 * x + 10 * y <= 800

# print(profit)
# status = profit.solve()
# print(p.LpStatus[status])
# print("Number of hectares in which x is grown:",p.value(x))
# print("Number of hectares in which y is grown:",p.value(y))
# print("Maximum Profit:",p.value(profit.objective))
# for i in range(30):
# 	Y[i]=p.LpVariable("Y[i]", lowBound=0,upperBound=13800
Y = p.LpVariable.dicts("y",days ,lowBound=0,upBound=13800,cat='Integer')
S = p.LpVariable.dicts("S",days ,lowBound=0,cat='Integer')
J = p.LpVariable.dicts("J",days ,lowBound=0,upBound=12,cat='Integer')
R = p.LpVariable.dicts("R",days ,lowBound=0,upBound=300,cat='Integer')
T = p.LpVariable.dicts("T",days ,lowBound=0,cat='Integer')

Z_max += 1000 * 222 *sum( S) + 25 * 270 * sum(J)


Z_max += Y[1] ==12000 + 1000 * (20 +40) *(S[1] -T[1])
for i in range(1,30):
	Z_max += R[i] ==25 * J[i]
	Z_max += R[i] ==25 * J[i]
	Z_max += S[i] + R[i] ==3000
	Z_max += S[1] ==3000
	if(i>=2 and i<7):
		Z_max = Y[i]=Y[i-1] + 1000 * (20+40)*(S[i]-T[i])
		Z_max += S[i] ==3000
	elif(i>6):
		Z_max = Y[i]=Y[i-1] + 1000 * (20+40)*(S[i]-S[i-6])
		Z_max = S[i-6] = 1000 * (20 + 40)  * T[i]

status = Z_max.solve()
print(p.LpStatus[status])




