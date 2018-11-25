import numpy as np

_array = np.arange(9).reshape(3, 3) 
print("\n",_array," -  np.arrang(15).reshape(3,3)")

# https://het.as.utexas.edu/HET/Software/Numpy/reference/generated/numpy.linalg.norm.html
_array = np.linalg.norm(_array)
print("\n",_array," -  np.linalg.norm(_array)")


multiDimensArray = np.random.randn(3, 3)# + 1j*np.random.randn(3, 3)
print("\n before linalg.svd: ", multiDimensArray,"\n") 
U, s, V = np.linalg.svd(multiDimensArray, full_matrices=True)
print("U:",U,"\n V:", V,"\n s:", s)

def extractRt(E):
  W = np.mat([[0,-1,0],[1,0,0],[0,0,1]],dtype=float)
  U,d,Vt = np.linalg.svd(E)
  assert np.linalg.det(U) > 0
  if np.linalg.det(Vt) < 0:
    Vt *= -1.0
  R = np.dot(np.dot(U, W), Vt)
  if np.sum(R.diagonal()) < 0:
    R = np.dot(np.dot(U, W.T), Vt)
  t = U[:, 2]
  ret = np.eye(4)
  ret[:3, :3] = R
  ret[:3, 3] = t
  return ret


a2 = np.arange(6) # 1d array
print(a2)

b2 = np.arange(12).reshape(4, 3) # 2d array
print("\n 2d arr: \n", b2)

c = np.arange(24).reshape(2,3,4)
print("\n 3d arr: : \n", c) # 3d array

extractRt(multiDimensArray)
