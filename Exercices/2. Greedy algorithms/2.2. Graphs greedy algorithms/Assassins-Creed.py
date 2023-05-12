# Assassin's Creed
# Shortest path between nodes evading baned nodes

def select_min_distance(distances, visited_nodes, baned_nodes):
    min_distance = float('inf')
    best_node = None

    for node in range(len(distances)):
        if distances[node] < min_distance and node not in baned_nodes and node not in visited_nodes:
            min_distance = distances[node]
            best_node = node

    return best_node


def dijkstra(current_node, end_node, graph, baned_nodes):
    # Initialize the visited nodes set
    visited_nodes = set()

    # Initialize the distances vector
    distances = [float('inf')] * len(graph)
    distances[current_node] = 0

    for _ in range(len(graph)):
        # Check if finished
        if current_node == end_node or current_node is None:
            return distances[end_node]

        # Update distances vector and visited nodes set
        visited_nodes.add(current_node)
        for end, cost in graph[current_node]:
            if distances[current_node] + cost < distances[end] and end not in baned_nodes:
                distances[end] = distances[current_node] + cost

        current_node = select_min_distance(distances, visited_nodes, baned_nodes)

    # Return answer
    return distances[end_node]


def main():
    node_amount, edge_amount = map(int, input().strip().split())

    graph = [[] for _ in range(node_amount)]
    for node in range(edge_amount):
        start, end, cost = map(int, input().strip().split())
        graph[start].append((end, cost))
        graph[end].append((start, cost))

    baned_nodes_amount = int(input().strip())
    baned_nodes = set(map(int, input().split()))
    start_node, end_node = map(int, input().strip().split())

    distance = dijkstra(start_node, end_node, graph, baned_nodes)
    if distance < float('inf'):
        print(distance)
    else:
        print('IMPOSIBLE')


if __name__ == '__main__':
    main()

