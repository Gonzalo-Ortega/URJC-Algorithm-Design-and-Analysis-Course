# Casting Tentador
# Deep-first search used to check if a graph is strongly connected.

def is_strongly_connected(graph):
    for initial_node in range(len(graph)):
        stack = [initial_node]
        visited = set()

        while stack:
            node = stack.pop()
            visited.add(node)
            for i in range(len(graph[node])):
                if graph[node][i] not in visited:
                    stack.append(graph[node][i])

        if len(visited) < len(graph):
            return False

    return True


def main():
    nodes, arrows = map(int, input().strip().split())

    g = [[] for _ in range(nodes)]

    for edge in range(arrows):
        a, b = map(int, input().strip().split())
        g[a].append(b)

    if is_strongly_connected(g):
        print("CASTING COMPLETO")
    else:
        print("HAY QUE REPETIR")


if __name__ == '__main__':
    main()
