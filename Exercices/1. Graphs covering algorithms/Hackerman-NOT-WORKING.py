# Hackerman

# NOT WORKING

def get_lowest_node(g, node):
    pass


def deep_first_search(g):
    # We set the initial node to visit the conex component
    visited = set()
    iteration = 0
    stack = [0]

    while stack:
        iteration += 1
        node = stack.pop()
        visited.add(node)
        g["discovery"][node] = iteration
        g["lowest"][node] = get_lowest_node(g, node)

        # Visit adjacent nodes:
        for i in range(len(g["adj"][node])):
            if g["adj"][node][i] not in visited:
                stack.append(g["adj"][node][i])


def main():
    # We read the graph data:
    nodes, edges = map(int, input().strip().split())

    # We initialize the graph:
    graph = {
        "weight": [0] * nodes,
        "adj": [[] for _ in range(nodes)],
        "discovery": [0] * nodes,
        "lowest": [0] * nodes
    }

    # We add the weights to the nodes:
    for node in range(nodes):
        graph["weight"][node] = input().strip()

    # We add the edges to the graph:
    for edge in range(edges):
        a, b = map(int, input().strip().split())
        graph["adj"][a].append(b)
        graph["adj"][b].append(a)

    print(graph)


if __name__ == '__main__':
    main()
