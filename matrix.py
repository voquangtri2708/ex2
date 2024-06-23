A = [[1,2,3],
     [4,5,6]]
B = [[2,3],
     [4,5],
     [6,7]]

import numpy as np
A = np.array(A)
B = np.array(B)

C = A @ B
print(C)