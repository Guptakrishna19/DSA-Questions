# Find the shortest path between two nodes in an unweighted graph using BFS.
# method 1:

from collections import deque

def bfs(graph, start, end):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        node, path = queue.popleft()
        visited.add(node)
        if node == end:
            return path
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    return None

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


# method 2:

from collections import deque

def bfs_shortest_path(graph, src, dest):
    # Initialize a queue with the starting path
    queue = deque([[src]])
    visited = set()

    while queue:
        # Get the first path from the queue
        path = queue.popleft()
        # Get the last node from the path
        node = path[-1]

        # If this node is the destination, return the path
        if node == dest:
            return path

        # If this node has not been visited
        if node not in visited:
            # Mark it as visited
            visited.add(node)

            # Enqueue all adjacent nodes by adding them to the current path
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    # If the destination node is not reachable, return an empty list
    return []

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

path = bfs_shortest_path(graph, 'A', 'F')
print(f"Path: {path}")






