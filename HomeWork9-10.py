graph1 = {
    'A' : ['B','C'],
    'B' : ['A','D'],
    'C' : ['A'],
    'D' : ['B'],
}
visited = []
def dfs(graph,node):
    global visited
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph,n)
dfs(graph1,'A')
print("DFS:")
print(visited)

graph = {'A' : ['B','C'],
        'B' : ['A','D'],
        'C' : ['A'],
        'D' : ['B'],
         }
from queue import deque
def bfs(graph, start):
    visited, queue = [], deque([start])
    while queue:
        vertex = queue.pop()
        if vertex not in visited:
            visited.append(vertex)
            queue.extendleft(set(graph[vertex]) - set(visited))
    return visited
print("BFS:")
print(bfs(graph, 'A'))
class graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
# Check for the visisted and unvisited nodes
def dfs(graph, start, visited = None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

gdict = {
    "a" : set(["b","c"]),
    "b" : set(["a", "d"]),
    "c" : set(["a", "d"]),
    "d" : set(["e"]),
    "e" : set(["a"])
}
dfs(gdict, 'a')