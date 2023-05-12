# Henry Pitter
from collections import deque


def breath_first_search(graph, start_node, end_node, wall_nodes):

    visited_nodes = set()
    visited_nodes.add(start_node)

    level_nodes = deque()
    level_nodes.append(start_node)

    iterations = 0

    while level_nodes:
        iterations += 1
        next_level_nodes = deque()
        while level_nodes:
            node = level_nodes.popleft()
            for adj in graph[node]:
                if iterations % 2 == 0 and adj in wall_nodes:
                    continue
                if adj not in visited_nodes:
                    if adj == end_node:
                        return iterations
                    next_level_nodes.append(adj)
                    visited_nodes.add(adj)
        level_nodes = next_level_nodes
    return iterations


def main():
    rows, columns = map(int, input().strip().split())
    graph = [[] for _ in range(rows * columns)]
    start_node = 0
    end_node = None
    wall_nodes = set()

    for i in range(rows):
        node_types = deque(map(int, input().strip().split()))
        for j in range(columns):
            node = i * columns + j

            # Evaluate node type
            node_type = node_types.popleft()
            if node_type == -1:
                wall_nodes.add(node)
            elif node_type == 2:
                end_node = node

            # Add adjacent nodes
            if j + 1 < columns:
                graph[node].append(node + 1)
            if j - 1 >= 0:
                graph[node].append(node - 1)
            if i + 1 < rows:
                graph[node].append(node + columns)
            if i - 1 >= 0:
                graph[node].append(node - columns)

    print(breath_first_search(graph, start_node, end_node, wall_nodes))


if __name__ == "__main__":
    main()
