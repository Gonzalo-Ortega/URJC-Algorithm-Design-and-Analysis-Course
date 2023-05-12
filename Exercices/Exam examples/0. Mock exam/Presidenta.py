# Presidenta
# Min recovery tree using Krustal and saving used edges.

def update_conex_components(conex_components, new_id, old_id):
    for component in range(len(conex_components)):
        if conex_components[component] == old_id:
            conex_components[component] = new_id


def kruskal(nodes, edges):
    total_cost = 0
    conex_components = list(range(len(nodes)))
    conex_components_amount = len(conex_components)
    solution_edges = []

    edge = 0
    while conex_components_amount > 1 and edge < len(edges):
        cost, start, end = edges[edge]
        if conex_components[nodes[start]] != conex_components[nodes[end]]:
            total_cost += cost

            solution_edges.append((start, end) if start < end else (end, start))

            conex_components_amount -= 1
            update_conex_components(conex_components, conex_components[nodes[start]], conex_components[nodes[end]])
        edge += 1

    return total_cost, solution_edges


def main():
    node_amount, edge_amount = map(int, input().strip().split())
    edges = []
    nodes = dict()
    for _ in range(edge_amount):
        start, end, cost = input().strip().split()
        if start not in nodes:
            nodes[start] = len(nodes)
        if end not in nodes:
            nodes[end] = len(nodes)
        edges.append((int(cost), start, end))
        edges.append((int(cost), end, start))
    edges.sort()

    total_cost, solution_edges = kruskal(nodes, edges)

    print(total_cost)
    solution_edges.sort()
    for start, end in solution_edges:
        print(start + " - " + end)


if __name__ == "__main__":
    main()
