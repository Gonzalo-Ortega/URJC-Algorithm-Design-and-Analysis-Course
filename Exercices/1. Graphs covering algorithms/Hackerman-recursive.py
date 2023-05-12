# Hackerman (recursive).
# Working recursive version of the problem.

def search_circle(graph, visited, node, ignore):
    if node == ignore:
        return
    visited.add(node)
    for adj in graph[node]:
        if adj not in visited:
            search_circle(graph, visited, adj, ignore)


def cut_nodes_cost_sum(graph):
    visited = set()
    cost_sum = 0
    search_circle(graph, visited, 1, 0)

    if len(visited) < len(graph) - 1:
        cost_sum += costs[0]

    for edge in range(1, len(graph)):
        visited = set()
        search_circle(graph, visited, 0, edge)
        if len(visited) < len(graph) - 1:
            cost_sum += costs[edge]

    return cost_sum


def main():
    nodes, edges = map(int, input().strip().split())

    costs = [0] * nodes
    g = [set() for _ in range(nodes)]

    for node in range(nodes):
        costs[node] = int(input().strip())

    for edge in range(edges):
        a, b = map(int, input().strip().split())
        g[a].add(b)
        g[b].add(a)

    print(cut_nodes_cost_sum(g))


if __name__ == '__main__':
    main()
