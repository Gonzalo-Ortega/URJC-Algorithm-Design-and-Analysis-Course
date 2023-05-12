# Breath-first search
# Iterates over all nodes in a graph.

from collections import deque


# Functions
def breath_first_search_aux(g, visited, node):
    queue = deque()
    print("Visiting node: " + str(node))
    visited[node] = True
    queue.append(node)
    while queue:
        aux = queue.popleft()
        for adj in g[aux]:
            if not visited[adj]:
                visited[adj] = True
                print("Visiting node: " + str(adj))
                queue.append(adj)


def breath_first_search(g):
    n = len(g)
    visited = [False] * n
    for node in range(1, n):
        if not visited[node]:
            breath_first_search_aux(g, visited, node)


def main():
    graph = [
        [],
        [2, 4, 8],
        [1, 3, 4],
        [2, 4, 5],
        [1, 2, 3, 7],
        [3, 6],
        [5, 7],
        [4, 5, 9],
        [1, 9],
        [7, 8]
    ]

    breath_first_search(graph)


if __name__ == '__main__':
    main()
