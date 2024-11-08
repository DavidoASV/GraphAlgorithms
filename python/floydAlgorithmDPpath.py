import numpy as np

def conv(val):
    try:
        return float(val)
    except:
        pass
    return np.Infinity

def printPath(a,b,myparents):
    if a!=b:
        printPath(a,myparents[a][b],myparents)
    print(b)


adjmat = np.loadtxt('Files//adjmat01.txt', delimiter=',', converters=conv)
assert adjmat.shape[0]==adjmat.shape[1] 

print(adjmat)
V = adjmat.shape[0]

parents = np.zeros(adjmat.shape,dtype=int)
for i in range(V):
    for j in range(V):
        parents[i][j]=i
print(parents)

for k in range(V):
    for i in range(V):
        for j in range(V):
            if adjmat[i][j] > adjmat[i][k] + adjmat[k][j]:
                adjmat[i][j] = adjmat[i][k] + adjmat[k][j]
                parents[i][j] = parents[k][j]
print(adjmat)
print(parents)

for i in range(V):
    for j in range(V):
        if i!=j and np.isfinite(adjmat[i][j]):
            print('path({},{}):'.format(i,j))
            printPath(i,j,parents)
            print('******\n')