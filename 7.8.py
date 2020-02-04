# solution for problem 7.8 from https://github.com/gadepall/school/blob/master/ncert/optimization/gvv_ncert_opt.pdf
import pulp as p

profit = p.LpProblem("profit_maximising_problem", p.LpMaximize)

x = p.LpVariable("x", lowBound=0)
y = p.LpVariable("y", lowBound=0)

profit += 10500 * x + 9000 * y
profit += x + y == 50
profit += 20 * x + 10 * y <= 800

print(profit)
status = profit.solve()
print(p.LpStatus[status])
print("Number of hectares in which x is grown:",p.value(x))
print("Number of hectares in which y is grown:",p.value(y))
print("Maximum Profit:",p.value(profit.objective))
