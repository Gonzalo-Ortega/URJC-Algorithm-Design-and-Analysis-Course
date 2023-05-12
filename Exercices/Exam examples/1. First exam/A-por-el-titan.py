# A por el titan
# Min paths using Dijkstra over a series of nodes counting the total passing though each node.

def select_min_distance(distances, visited_nodes):
    min_distance = float("inf")
    best_node = None
    for node in range(len(distances)):
        if distances[node] < min_distance and node not in visited_nodes:
            min_distance = distances[node]
            best_node = node
    return best_node


def dijkstra(graph, current_node):
    visited_nodes = set()
    distances = [float('inf')] * len(graph)
    distances[current_node] = 0
    parents = [-1] * len(graph)

    for _ in range(len(graph) - 1):
        visited_nodes.add(current_node)

        # Update distances:
        for end, cost in graph[current_node]:
            if distances[current_node] + cost < distances[end]:
                distances[end] = distances[current_node] + cost
                parents[end] = current_node

        current_node = select_min_distance(distances, visited_nodes)

    return parents


def main():
    node_amount, edge_amount = map(int, input().strip().split())
    graph = [[] for _ in range(node_amount)]
    for _ in range(edge_amount):
        start, end, cost = map(int, input().strip().split())
        graph[start].append((end, cost))
        graph[end].append((start, cost))

    solution = [0] * node_amount
    iterations = int(input().strip())

    parents_vector = [-1] * node_amount
    for node in range(node_amount):
        parents_vector[node] = dijkstra(graph, node)

    for _ in range(iterations):
        start_node, end_node = map(int, input().strip().split())
        solution[end_node] += 1
        node = parents_vector[start_node][end_node]
        while node != -1:
            solution[node] += 1
            node = parents_vector[start_node][node]

    for node in solution:
        print(node, end=" ")


if __name__ == "__main__":
    main()
