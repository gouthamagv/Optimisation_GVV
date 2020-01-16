import numpy as np

A = np.matrix('2 0 -3; 0 2 4; 3 -4 0')
b = np.matrix('6 ; -10 ; 26')
print (np.linalg.inv(A)*b)