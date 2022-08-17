from collections import deque

def bfs(graph, start, value):
    if not start in graph:
        return None
        
    visited = set(start)
    queue = deque(start)

    while not len(queue) == 0:
        node = queue.pop()
        for n in graph[node]:
            if n == value:
                return n
            if n not in visited:
                queue.append(n)
                visited.add(n)
    return None


