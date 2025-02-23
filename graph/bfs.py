class Graph:
    def __init__(self):
        self.graph={}
    def addEdge(self,u,v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u]=[v]
    def bfs(self,s):
        visited=[False]*len(self.graph)
        queue=[]
        queue.append(s)
        visited[s]=True
        while queue:
            s=queue.pop(0) # remove from queue before adding edge to graph list and add to queue again later on
            print(s,end=" ")
            for i in self.graph[s]:
                if visited[i]==False:
                    queue.append(i)
                    visited[i]=True
    def dfs(self,s):
        visited=[False]*len(self.graph)
        stack=[s]
        visited[s]=True
        while stack:
            s=stack.pop()
            print(s,end=" ")
            for i in self.graph[s]:
                if visited[i]==False:
                    stack.append(i)
                    visited[i]=True
                    # for DFS, we need to add visited[i] = True after popping it from stack, otherwise it will be visited again when we visit its adjacent nodes


g=Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)

print("Following is Breadth First Traversal")
g.bfs(0)

print("\nFollowing is Depth First Traversal")
g.dfs(0)



#youtube tutorial code

import collections

def bfs(graph, start):
    visited = set() # list of visited nodes that should be visited
    queue = collections.deque([start]) #
    while queue:
        vertex = queue.popleft()
        visited.add(vertex) #
        for i in graph[vertex]:
            if i not in visited:
                queue.append(i)
    print(visited)

# def dfs(graph,start):
#     visited = set()
#     if start not in visited:
#         visited.add(start)
#         print(start, end=' ')
#         for neighbor in graph[start]:
#             dfs(graph, neighbor)


graph={0:[1,2,3], 1:[0,2],2:[0,1,4], 3:[0],4:[2]}
bfs(graph,0)

# print("\n")

# dfs(graph,0)
