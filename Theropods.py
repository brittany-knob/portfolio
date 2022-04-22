import matplotlib.pyplot as plt
from numpy import *
from matplotlib import *
from scipy import linalg

theropods = loadtxt('thero.csv', delimiter=',')
print(theropods)

log_data = log(theropods)/log(10)  # use log base 10

b = log_data[:, 1:2]
A = hstack([ones((24, 1)), log_data[:, 0:1]])

x = linalg.solve( A.T @ A, A.T @ b )
k, m = float(x[0]), float(x[1]) 
print((k, m))


(x_alt, residues, a_rank, svd_vals) = linalg.lstsq(A, b)
print((float(x_alt[0]), float(x_alt[1])))


z = 10**linspace(0, 1.75, 10)

plt.loglog(theropods[:, 0], theropods[:, 1], 'o', z, 10**k*z**m,'r-')
plt.title('Theropods', fontsize=18)
plt.xlabel('Body Length (m)', fontsize=18)
plt.ylabel('Body Mass (kg)', fontsize=18)
Equation = "$M_t = %.3f  L^{%.3f}$"%(10**k, m)
plt.text(11, 1.7, Equation, fontsize=14)

plt.show()
