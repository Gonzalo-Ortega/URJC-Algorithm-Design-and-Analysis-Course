# Baile-TikTok
# Count nodes in given depht from a starting node, using a breath-first search.

from collections import deque


def get_reached_nodes(graph, level):
    visited = set()
    next_level_nodes = deque()
    visited.add(0)
    next_level_nodes.append(0)
    iteration = 1
    level_nodes = next_level_nodes
    while len(level_nodes) > 0 and iteration < level:
        iteration += 1
        next_level_nodes = deque()
        while level_nodes:
            aux = level_nodes.popleft()
            for adj in graph[aux]:
                if adj not in visited:
                    visited.add(adj)
                    next_level_nodes.append(adj)
        level_nodes = next_level_nodes
    return len(visited)


def main():
    dances_number = int(input().strip())
    levels = [0] * dances_number
    graphs = [[] for _ in range(dances_number)]

    for i in range(dances_number):
        level, nodes, edges = map(int, input().strip().split())
        levels[i] = level
        graphs[i] = [[] for _ in range(nodes)]

        for edge in range(edges):
            a, b = map(int, input().strip().split())
            graphs[i][a].append(b)
            graphs[i][b].append(a)

    for i in range(dances_number):
        print(get_reached_nodes(graphs[i], levels[i]))


if __name__ == '__main__':
    main()
