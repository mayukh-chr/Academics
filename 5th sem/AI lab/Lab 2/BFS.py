graph = {
    '5':['3', '7'],
    '3':['2', '4'],
    '7':['8'],
    '2':[],
    '4':['8'],
    '8':[]
}


visited = []
queue = []

def bfs(visited, graph, root):
    visited.append(root)
    queue.append(root)

    while(queue):
        node = queue.pop(0)
        print(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.append(neighbor)

print("BFS tym: ")
bfs(visited, graph, '5')



    
