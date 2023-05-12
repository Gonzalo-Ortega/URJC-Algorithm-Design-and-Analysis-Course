# La fiesta de Arquímedes.
# Get the nodes from each conex component using a breath-first search.

def conex_component(graph, visited, node):
    stack = [node]
    conex_members = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            conex_members.append(node)

        for i in range(len(graph[node])):
            if graph[node][i] not in visited:
                stack.append(graph[node][i])

    conex_members.sort()
    return conex_members


def conex_components_members(graph):
    visited = set()
    for node in range(len(graph)):
        if node not in visited:
            print(*conex_component(graph, visited, node))


def main():
    nodes, edges = map(int, input().strip().split())

    g = [[] for _ in range(nodes)]

    for edge in range(edges):
        a, b = map(int, input().strip().split())
        g[a].append(b)
        g[b].append(a)

    conex_components_members(g)


if __name__ == '__main__':
    main()
