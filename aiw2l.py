def iscycle(adj, vis, id):
    if vis[id] == 1:
        return True
    if vis[id] == 0:
        vis[id] = 1
        for edge in adj[id]:
            if iscycle(adj, vis, edge):
                return True
    vis[id] = 2
    return False

def canFinish(n, prerequisites):
    adj = [[] for _ in range(n)]
    for edge in prerequisites:
        adj[edge[1]].append(edge[0])
    vis = [0] * n
    
    for i in range(n):
        if iscycle(adj, vis, i):
            return False
    return True

# Example usage
tasks = 3
prerequisites = [[1, 0], [0, 2]]
print(canFinish(tasks, prerequisites)) 
