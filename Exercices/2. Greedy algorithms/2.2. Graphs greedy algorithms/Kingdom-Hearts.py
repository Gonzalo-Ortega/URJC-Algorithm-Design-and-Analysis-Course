# Kingdom Hearts
# Minimal recovery tree using Kruskal.

def update_components(conex_components, new_id, old_id):
    for component in range(len(conex_components)):
        if conex_components[component] == old_id:
            conex_components[component] = new_id


def kruskal(edges, node_amount):
    total_cost = 0

    conex_components = list(range(node_amount))
    number_of_components = len(conex_components)

    edge = 0
    while number_of_components > 1 and edge < len(edges):
        cost, start, end = edges[edge]
        if conex_components[start] != conex_components[end]:
            total_cost += cost
            number_of_components -= 1
            update_components(conex_components, conex_components[start], conex_components[end])
        edge += 1

    return total_cost


def main():
    node_amount, edge_amount = map(int, input().strip().split())
    edges = []
    for _ in range(edge_amount):
        start, end, cost = map(int, input().strip().split())
        edges.append((cost, start, end))
    edges.sort()
    print(kruskal(edges, node_amount))


if __name__ == "__main__":
    main()
