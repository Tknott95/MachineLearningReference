import numpy as np

_array = np.arange(9).reshape(3, 3) 
print("\n",_array," -  np.arrang(15).reshape(3,3)")

# https://het.as.utexas.edu/HET/Software/Numpy/reference/generated/numpy.linalg.norm.html
_array = np.linalg.norm(_array)
print("\n",_array," -  np.linalg.norm(_array)")


multiDimensArray = np.random.randn(9, 6) + 1j*np.random.randn(9, 6)
print("\n before linalg.svd: ", multiDimensArray,"\n") 
U, s, V = np.linalg.svd(multiDimensArray, full_matrices=True)
print("U:",U,"\n V:", V,"\n s:", s)
