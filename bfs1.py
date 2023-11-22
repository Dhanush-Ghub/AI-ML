from collections import defaultdict, deque

def explore(graph, begin):
    reached = set()
    queue = deque([begin])
    reached.add(begin)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor_node in graph[node]:
            if neighbor_node not in reached:
                queue.append(neighbor_node)
                reached.add(neighbor_node)

num_points = int(input())
num_links = int(input())
graph_map = defaultdict(list)

for _ in range(num_links):
    x, y = map(int, input().split())
    graph_map[x].append(y)
    graph_map[y].append(x)

starting_point = int(input())
explore(graph_map, starting_point)

