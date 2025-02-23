class Graph:

    def __init__(self):
        self.graph = {}
    def addEdge(self,u,v):
    if u in self.graph:
        self.graph[u].append(v)
    else:
        self.graph[u]=[v]
    def isCyclicUtil(self,v, visited, recStack):
        visited[v]=True
        recStack[v]=True
        for neighbour in self.graph[v]:
            if not visited[neighbour]:
                if self.isCyclicUtil(neighbour, visited, recStack):
                    return True
            elif recStack[neighbour]:
                return True
        recStack[v]=False
        return False

    def isCyclic(self):
        visited = [False]*(len(self.graph))
        recStack = [False]*(len(self.graph))
        for node in range(len(self.graph)):
            if not visited[node]:
                if self.isCyclicUtil(node, visited, recStack):
                    return True
        return False


# Create a graph and check for cycle
g = Graph()

g.addEdge(0, 1)

g.addEdge(0, 2)

g.addEdge(1, 2)

g.addEdge(2, 0)

g.addEdge(2, 3)

g.addEdge(3, 3)

if g.isCyclic():
    print("Graph contains cycle")
else:
    print("Graph does not contain cycle")
