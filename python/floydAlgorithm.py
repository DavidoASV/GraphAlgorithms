import numpy as np

def conv(val):
    try:
        return float(val)
    except:
        pass
    return np.Infinity

adjmat0 = np.loadtxt('Files//adjmat01.txt', delimiter=',', converters=conv)
assert adjmat0.shape[0]==adjmat0.shape[1] 

print(adjmat0)
V = adjmat0.shape[0]

adjmat = np.zeros(shape=(V,V,V), dtype=float)

for k in range(V):
    for i in range(V):
        for j in range(V):
            if k==0:
                adjmat[k][i][j] = adjmat0[i][j]
            else:
                adjmat[k][i][j] = min(adjmat[k-1][i][j], adjmat[k-1][i][k] + adjmat[k-1][k][j])

print(adjmat[V-1][:][:])