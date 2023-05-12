# Brawl Stars
# Minimum path between two nodes checking max distances and saving path nodes.

def select_min_distance(distances, visited_nodes):
    min_distance = float('inf')
    best_node = None
    for node in range(1, len(distances)):
        if distances[node] < min_distance and node not in visited_nodes:
            min_distance = distances[node]
            best_node = node
    return best_node


def dijkstra(graph):
    visited_nodes = set()
    current_node = 1

    distances = [float('inf')] * (len(graph))
    distances[current_node] = 0
    parents = [-1] * len(graph)

    for _ in range(1, len(graph)):
        visited_nodes.add(current_node)
        for end, cost in graph[current_node]:
            if distances[current_node] + cost < distances[end]:
                distances[end] = distances[current_node] + cost
                parents[end] = current_node

        current_node = select_min_distance(distances, visited_nodes)

    return distances, parents


def main():
    node_amount, edge_amount = map(int, input().strip().split())
    graph = [[] for _ in range(node_amount + 1)]
    for _ in range(edge_amount):
        start, end, cost = map(int, input().strip().split())
        graph[start].append((end, cost))
        graph[end].append((start, cost))
    iterations, distance = map(int, input().strip().split())

    distances, parents = dijkstra(graph)
    for _ in range(iterations):
        node = int(input().strip())
        while node != 1:
            if distances[node] < distance:
                print(node, end=" ")
            node = parents[node]
        print()


if __name__ == '__main__':
    main()
