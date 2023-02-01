com = int(input())
n = int(input())
graph = {i:[] for i in range(1,com+1)}
res = 0

def dfs(graph, start):
    need_visited, visited = list(), list() 
    need_visited.append(start)

    while need_visited:
        node = need_visited.pop()
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
    return visited

visited = [1]
def dfs2(graph, start):
    for i in graph[start]:
        if i not in visited:
            visited.append(i)
            dfs2(graph, i)
    return visited

for i in range(n):
    x, y = map(int, input().split(" "))
    graph[x].append(y)
    graph[y].append(x)
print(len(dfs2(graph, 1))-1)



