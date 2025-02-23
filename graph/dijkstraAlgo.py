import sys
import heapq

def dijk(graph, src, dest):
    inf = sys.maxsize  # it holds the maximum value
    node_data = {node: {'cost': inf, 'pred': []} for node in graph}
    node_data[src]['cost'] = 0

    priority_queue = [(0, src)]
    visited = set()

    while priority_queue:
        current_cost, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == dest:
            break

        for neighbor, weight in graph[current_node].items():
            cost = current_cost + weight
            if cost < node_data[neighbor]['cost']:
                node_data[neighbor]['cost'] = cost
                node_data[neighbor]['pred'] = node_data[current_node]['pred'] + [current_node]
                heapq.heappush(priority_queue, (cost, neighbor))

    path = node_data[dest]['pred'] + [dest]
    return node_data[dest]['cost'], path

graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'A': 2, 'C': 1, 'D': 5},
    'C': {'A': 4, 'B': 1, 'D': 3},
    'D': {'B': 5, 'C': 3},
    'E': {'A': 5}
}

cost, path = dijk(graph, 'A', 'E')
print(f"Cost: {cost}, Path: {path}")