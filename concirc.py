
import numpy as np
import matplotlib.pyplot as plt
import subprocess
from coeffs import *


n =  np.array([3,-4]) 
c = 26
P = np.array([3,-5]) 

x = P[0]*np.ones(8)
y = P[1]*np.ones(8)
rmin =0.1
r = np.arange(8)*rmin*6


phi = np.linspace(0.0,2*np.pi,100)
na=np.newaxis


x_line = x[na,:]+r[na,:]*np.sin(phi[:,na])
y_line = y[na,:]+r[na,:]*np.cos(phi[:,na])
ax=plt.plot(x_line,y_line,'-')

k = np.array([-5,20])

x_AB=line_norm_eq(n,c,k)

bx=plt.plot(x_AB[0,:],x_AB[1,:],label="$3*x_1-4*x_2-26=0$")
plt.axis('equal')
plt.grid()
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.legend([ax[1], bx[0]],['$(x_1-3)^2+(x_2+5)^2=0.36$','$3x_1-4x_2-26=0$'], loc='best')
plt.show()










