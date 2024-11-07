import numpy as np
import json

def conv(val):
    try:
        return float(val)
    except:
        pass
    return np.Infinity

def serialize(m):
    n = m.shape[0]
    myheaders = list(range(n))
    mycells = []
    mycells.append(myheaders)
    for ii in range(n):
        mycells.append(list(m.T[ii]))
    myObj = {
        "kind":{ "plotly": True },
        "data": [{
            "header": {
                "values": myheaders
            },
            "cells": {
                "values": mycells
            },
            "type": "table",
        }],
        "layout": {},
    }
    # myObj = {
    #     "kind":{ "plotly": True },
    #     "data": [{
    #         "header": {
    #             "values": ["H1", "H2", "H3"]
    #         },
    #         "cells": {
    #             "values": [
    #                 ["A", "B", "C"],
    #                 [341319, 281489, 294786],
    #                 [4488916, 3918072, 3892124]
    #             ]
    #         },
    #         "type": "table"
    #     }],
    #     "layout": {}
    # }
    return myObj

adjmat = np.loadtxt('Files//adjmat01.txt', delimiter=',', converters=conv)
assert adjmat.shape[0]==adjmat.shape[1] 

serialized = serialize(adjmat)

print(adjmat)
V = adjmat.shape[0]

for k in range(V):
    for i in range(V):
        for j in range(V):
            adjmat[i][j] = min(adjmat[i][j], adjmat[i][k] + adjmat[k][j])
            serialized = serialize(adjmat)

print(adjmat)