# Prim's Algorithm in Python
from random import randrange
import time
INF = 9999999
# number of vertices in graph
N = 6
tic = time.perf_counter()
#creating graph by adjacency matrix method
G = [[0, 0, randrange(10), randrange(10), 0, 0],
     [randrange(10), 0, 0, 0, randrange(10), 0],
     [0, randrange(10), 0, 0, randrange(10), randrange(10)],
     [0, 0, 0, 0, randrange(10), 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0]]

selected_node = [0, 0, 0, 0, 0, 0]

no_edge = 0

selected_node[0] = True

# printing for edge and weight
print("Edge : Weight\n")
while (no_edge < N - 1):
    
    minimum = INF
    a = 0
    b = 0
    for m in range(N):
        if selected_node[m]:
            for n in range(N):
                if ((not selected_node[n]) and G[m][n]):  
                    # not in selected and there is an edge
                    if minimum > G[m][n]:
                        minimum = G[m][n]
                        a = m
                        b = n
    print(str(a) + "-" + str(b) + ":" + str(G[a][b]))
    selected_node[b] = True
    no_edge += 1

toc = time.perf_counter()
print(f"Code finished in {toc-tic:0.8f} seconds")