import heapq

def best_first_search(start, goal, heuristics, graph):
    queue    = [(heuristics[start], start, [start])]
    visited = set()

    while queue:
        _, current_node, current_path = heapq.heappop(queue)
        if current_node == goal:
            return current_path  # Path found
        visited.add(current_node)
        for neighbor, cost in graph.get(current_node, []):
            if neighbor not in visited:
                heapq.heappush(queue, (heuristics[neighbor], neighbor, current_path + [neighbor]))
    
    return None  # No path found

# Example heuristics dictionary and graph dictionary
heuristics = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2,
    'E': 0,
}

graph = {
    'A': [('B', 3), ('C', 2)],
    'B': [('D', 4)],
    'C': [('D', 1)],
    'D': [('E', 3)],
    'E': []
}

start_node = 'A'
goal_node = 'E'
path = best_first_search(start_node, goal_node, heuristics, graph)

if path:
    print("Path found:", " -> ".join(path))
else:
    print("Path not found.")