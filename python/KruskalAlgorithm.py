import numpy as np

def findp(parent, i):
    if parent[i]!=i:
        parent[i]=findp(parent, parent[i])
    return parent[i]

def unionsets(parent, rank, x, y):
    if rank[x] < rank[y]:
        parent[x] = y
    elif rank[y] < rank[x]:
        parent[x] = x
    else:
        parent[y]=x
        rank[x] += 1

edges = np.loadtxt('Files//edgelist.txt', delimiter=',', dtype=int)
Vset = set()
for i in range(edges.shape[0]):
    for j in range(edges.shape[1]):
        if j > 0:
            Vset.add(edges[i][j])
print(Vset)
assert(len(Vset)==1+max(Vset)-min(Vset))
V = len(Vset)

i = 0
e = 0
result = []
ranks = [0] * V
parents = list(range(V))

sEdges = sorted(edges.tolist(), key=lambda item: item[0])
print(sEdges)
print(ranks)
print(parents)

while e < V-1:
    w,u,v = sEdges[i]
    i += 1
    x = findp(parents,u)
    y = findp(parents,v)

    if x != y:
        e +=1
        result.append([w,u,v])
        unionsets(parents,ranks,x,y)

mst_cost = 0
print('This is the MST:')
for w,u,v in result:
    mst_cost += w
    print('Arc({},{})={}'.format(u,v,w))
print('MST cost: {}'.format(mst_cost))