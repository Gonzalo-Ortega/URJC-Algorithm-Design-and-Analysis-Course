# Deep-first search (recursive)
# Iterates over all nodes in a graph.

def deep_first_search_recursive(v, visited, g):
    print("Visiting node: " + str(v))
    visited.add(v)
    for node in g[v]:
        if node not in visited:
            deep_first_search_recursive(node, visited, g)


def deep_first_search(g):
    visited = set()
    for node in range(0, len(g)):
        if node not in visited:
            deep_first_search_recursive(node, visited, g)


def main():
    graph = [
        [1, 2],
        [0, 2, 3],
        [0, 1, 3],
        [1, 2, 4],
        [3]
    ]

    graph_v2 = [
        [],
        [2, 3],
        [1, 3, 4],
        [1, 2, 4],
        [2, 3, 5],
        [4]
    ]

    deep_first_search(graph)


if __name__ == '__main__':
    main()
