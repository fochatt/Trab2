 
def check_in_list(list, element):
    try:
        return list.index(element)
    except:
        return False

def createAdjMatrix(V, G):
    adjMatrix = []

    for i in range(V):
        adjMatrix.append([])
        for j in range(V):
            adjMatrix[i].append(0)

    for i in range(len(G)):
        adjMatrix[G[i][0]][G[i][1]] = G[i][2]
        adjMatrix[G[i][1]][G[i][0]] = G[i][2]

    return adjMatrix


def prim(V, G):
    adjMatrix = createAdjMatrix(V, G)
    vertex = 0
    MST = []
    edges = []
    visited = []
    minEdge = [None, None, float('inf')]

    while(len(MST) != V-1):
        visited.append(vertex)

        for r in range(V):
            if adjMatrix[vertex][r] != 0:
                edges.append([vertex, r, adjMatrix[vertex][r]])

        for e in range(len(edges)):
            if edges[e][2] < minEdge[2] and check_in_list(visited, edges[e][1]) == False:
                minEdge = edges[e]

        # edges.splice(edges.indexOf(minEdge), 1)
        edges.pop(edges.index(minEdge))
        MST.append(minEdge)
        vertex = minEdge[1]
        minEdge = [None, None, float('inf')]

    peso_total = 0
    for i in MST:
        peso_total += i[2]
    return MST, peso_total


a=0
b=1
c=2
d=3
e=4
f=5
graph = [
    [a,b,2],
    [a,c,3],
    [b,d,3],
    [b,c,5],
    [b,e,4],
    [c,e,4],
    [d,e,2],
    [d,f,3],
    [e,f,5]
]
geradora_minima, custo = prim(6, graph)
print('AGM: {}\ncusto: {}'.format(geradora_minima,custo))