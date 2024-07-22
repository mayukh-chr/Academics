graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

def dfs_search(graph, start, target, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    if start == target:
        print("\nTarget node found!")
        return True
    for next in graph[start]:
        if next not in visited:
            if dfs_search(graph, next, target, visited):
                return True
    return False

target_node = 'E'
if not dfs_search(graph, 'A', target_node):
    print("\nTarget node not found.")
