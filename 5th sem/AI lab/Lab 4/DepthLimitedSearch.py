def depth_limited_dfs(graph, start, depth, limit):
    if depth == limit:
        return
    print(start)
    for neighbor in graph[start]:
        depth_limited_dfs(graph, neighbor, depth + 1, limit)

Graph = {
    0: [1, 2], 
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
}

depth_limited_dfs(graph=Graph, start=0, depth=0, limit=5)
