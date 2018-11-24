import numpy as np

_array = np.arange(9).reshape(3, 3) 
print("\n",_array," -  np.arrang(15).reshape(3,3)")

# https://het.as.utexas.edu/HET/Software/Numpy/reference/generated/numpy.linalg.norm.html
_array = np.linalg.norm(_array)
print("\n",_array," -  np.linalg.norm(_array)")
