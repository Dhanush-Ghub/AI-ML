def depth_first_search(graph, vertex, visited_set):
    visited_set.add(vertex)
    print(vertex, end=" ")

    for neighbor in graph[vertex]:
        if neighbor not in visited_set:
            depth_first_search(graph, neighbor, visited_set)

num_vertices = int(input("Enter the number of vertices: "))
num_edges = int(input("Enter the number of edges: "))

graph = {}
for i in range(num_vertices):
    graph[i] = []

for _ in range(num_edges):
    u, v = map(int, input("Enter an edge (u v): ").split())
    graph[u].append(v)
    graph[v].append(u)

start_vertex = int(input("Enter the start vertex: "))
visited_set = set()

print("DFS traversal:")
depth_first_search(graph, start_vertex, visited_set)

