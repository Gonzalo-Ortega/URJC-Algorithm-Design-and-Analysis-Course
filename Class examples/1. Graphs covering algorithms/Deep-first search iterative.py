# Deep-first search (iterative)
# Iterates over all nodes in a graph.

def deep_first_search_aux(g, visited, node):
    # We set the initial node to visit the conex component
    stack = [node]

    while stack:
        node = stack.pop()
        visited.add(node)
        print("Visiting node: " + str(node))

        # Visit adjacent nodes:
        for i in range(len(g[node])):
            if g[node][i] not in visited:
                stack.append(g[node][i])


def deep_first_search(g):
    visited = set()
    for node in range(0, len(g)):
        if node not in visited:
            deep_first_search_aux(g, visited, node)


def main():
    graph = [
        [1, 2],
        [0, 3, 4],
        [0, 5],
        [1],
        [1],
        [2],
    ]

    deep_first_search(graph)


if __name__ == '__main__':
    main()
