# solution for problem 7.8 from https://github.com/gadepall/school/blob/master/ncert/optimization/gvv_ncert_opt.pdf
from cvxpy import *
import numpy as np

A = np.array(( [1, 1], [20, 10 ])).T
b = np.array([ 50, 800 ]).reshape((2,-1))
c = np.array([ 10500, 9000 ])

x = Variable((2,1))

f = c @ x
obj = Maximize(f)

constraints = [A.T @ x <= b]


Problem(obj, constraints).solve()

print("Number of hectares of land with X crop",x.value[0])
print("Number of hectares of land with Y crop",x.value[1])
print("Maximum profit =",f.value)
