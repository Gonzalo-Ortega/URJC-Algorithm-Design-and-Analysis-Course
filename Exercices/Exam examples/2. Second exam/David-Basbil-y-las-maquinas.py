# David Basbil y las maquinas - Gonzalo Ortega

def update_components(conex_components, old_index, new_index):
    for index in range(len(conex_components)):
        if conex_components[index] == old_index:
            conex_components[index] = new_index
    return conex_components


def kruskal(edges, node_amount):
    total_cost = 0
    conex_components = list(range(node_amount))
    conex_components_amount = node_amount
    nodes = {
        'cost': [0] * node_amount,
        'adj': [[] for _ in range(node_amount)]
    }

    edge = 0
    while conex_components_amount > 1:
        cost, start, end = edges[edge]
        if conex_components[start] != conex_components[end]:
            total_cost += cost
            nodes['cost'][start] += cost
            nodes['cost'][end] += cost
            nodes['adj'][start].append(end)
            nodes['adj'][end].append(start)
            conex_components = update_components(conex_components, conex_components[start], conex_components[end])
            conex_components_amount -= 1
        edge += 1

    return total_cost, nodes


def main():
    node_amount, edge_amount = map(int, input().strip().split())
    edges = []
    for _ in range(edge_amount):
        start, end, cost = map(int, input().strip().split())
        edges.append((cost, start, end))
    edges.sort()

    total_cost, nodes = kruskal(edges, node_amount)
    print(total_cost)

    iterations = int(input().strip())
    nodes_iterated = set()
    for _ in range(iterations):
        node = int(input().strip())
        if node not in nodes_iterated:
            nodes['adj'][node].sort()
            nodes_iterated.add(node)
        print(str(nodes['cost'][node]), end=': ')
        print(*nodes['adj'][node])


if __name__ == '__main__':
    main()
