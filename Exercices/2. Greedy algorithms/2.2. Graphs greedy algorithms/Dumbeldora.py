# Dumbeldora
# Minimum spanning tree counting individual adjacent selected node edges costs.

def update_components(conex_components, new_id, old_id):
    for component in range(len(conex_components)):
        if conex_components[component] == old_id:
            conex_components[component] = new_id


def kruskal(candidates, node_amount):
    total_cost = 0
    node_costs = [0] * node_amount

    conex_components = list(range(node_amount))
    number_of_components = len(conex_components)

    edge = 0
    while number_of_components > 1 and edge < len(candidates):
        cost, start, end = candidates[edge]
        if conex_components[start] != conex_components[end]:
            total_cost += cost
            node_costs[start] += cost
            node_costs[end] += cost
            number_of_components -= 1
            update_components(conex_components, conex_components[start], conex_components[end])
        edge += 1

    return total_cost, node_costs


def main():
    node_amount, edge_amount = map(int, input().strip().split())
    candidates = []
    for _ in range(edge_amount):
        start, end, cost = map(int, input().strip().split())
        candidates.append((cost, start, end))
    candidates.sort()
    total_cost, node_costs = kruskal(candidates, node_amount)

    print("Coste total: " + str(total_cost))
    node_id = 0
    for cost in node_costs:
        print("H" + str(node_id) + ": " + str(cost))
        node_id += 1


if __name__ == "__main__":
    main()
