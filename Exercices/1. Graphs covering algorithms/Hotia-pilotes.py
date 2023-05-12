# Hotia pilotes
# Count conex components using a deep-first search.

def deep_first_search_aux(g, visited, node):
    # We set the initial node to visit the conex component
    stack = [node]

    while stack:
        node = stack.pop()
        visited.add(node)

        # Visit adjacent nodes:
        for i in range(len(g[node])):
            if g[node][i] not in visited:
                stack.append(g[node][i])


def number_of_conex_components(g):
    visited = set()
    conex_components = 0
    for node in range(0, len(g)):
        if node not in visited:
            conex_components += 1
            deep_first_search_aux(g, visited, node)
    return conex_components


def main():
    # Read two numbers
    # n = Number of nodes | m = Number of edges
    n, m = map(int, input().strip().split())

    # Graph with n nodes:
    graph = [[] for _ in range(n)]

    # We add the m edges to the graph:
    for joint_nodes in range(m):
        a, b = map(int, input().strip().split())
        graph[a].append(b)
        graph[b].append(a)

    print(number_of_conex_components(graph))


if __name__ == '__main__':
    main()
