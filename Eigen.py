import numpy as np

A=np.array([[2,1,0],[1,2,1],[0,1,2]])
X=np.ones(3)

for i in range(4):
    Y= A@X #X=X0
    m=np.max(np.abs(Y))
    Y= Y/m #left Y is X1
    X=Y
    print(m,Y)
