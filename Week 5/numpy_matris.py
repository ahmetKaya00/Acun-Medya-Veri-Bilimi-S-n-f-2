import numpy as np

matris = np.random.randint(0,10,(2,3))
print("Matsin:\n",matris)

transpoz = matris.T
print("Transpoz:\n",transpoz)

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
carpim = np.dot(A,B)
print("Carpim:\n",carpim)

ters = np.linalg.inv(A)
print("Tersi:\n",ters)
