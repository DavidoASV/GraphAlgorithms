import numpy as np

def conv(val):
    try:
        return float(val)
    except:
        pass
    return np.Infinity

adjmat = np.loadtxt('Files//adjmat01.txt', delimiter=',', converters=conv)
assert adjmat.shape[0]==adjmat.shape[1] 

print(adjmat)
V = adjmat.shape[0]

for k in range(V):
    for i in range(V):
        for j in range(V):
            adjmat[i][j] = min(adjmat[i][j], adjmat[i][k] + adjmat[k][j])

print(adjmat)