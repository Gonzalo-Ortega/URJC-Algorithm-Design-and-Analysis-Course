# Reina de corazones
# Minimum distance between two nodes passing through selected nodes.

# DOES NOT WORK

from collections import deque


def select_min_distance(distances, visited_nodes, node_types, required_type):
    min_distance = float('inf')
    best_node = None

    for node in range(len(distances)):
        if node not in visited_nodes and node_types[node] == required_type and distances[node] < min_distance:
            min_distance = distances[node]
            best_node = node

    return best_node


def dijkstra(graph, node_types, type_requirements, current_node):
    required_type = type_requirements.popleft()

    visited_nodes = set()
    distances = [float('inf')] * len(graph)

    if node_types[current_node] == required_type:
        distances[current_node] = 0
    parents = [-1] * len(graph)

    for _ in range(len(graph) - 1):
        # Update distances vector and visited nodes set
        visited_nodes.add(current_node)
        required_type = type_requirements.popleft()

        for end, cost in graph[current_node]:
            if distances[current_node] + cost < distances[end] and node_types[end] == required_type:
                distances[end] = distances[current_node] + cost
                parents[end] = current_node

        # Get next node
        current_node = select_min_distance(distances, visited_nodes, node_types, required_type)
        if len(type_requirements) == 0:
            return distances, parents

    return distances, parents


def main():
    node_amount, edge_amount, iterations = map(int, input().strip().split())
    graph = [[] for _ in range(node_amount)]
    for _ in range(edge_amount):
        start, end, cost = map(int, input().strip().split())
        graph[start].append((end, cost))
        graph[end].append((start, cost))

    node_types = []
    for _ in range(node_amount):
        node, node_type = input().strip().split()
        node_types.append(node_type)

    for _ in range(iterations):
        start_node, end_node, requirement = input().strip().split()
        start_node, end_node = map(int, (start_node, end_node))
        type_requirements = deque()
        for node_type in requirement:
            type_requirements.append(node_type)

        distances, parents = dijkstra(graph, node_types, type_requirements, start_node)

        if distances[end_node] == float("inf"):
            print("No se puede llegar")
        else:
            solution = deque()
            while end_node != start_node:
                solution.appendleft(end_node)
                end_node = parents[end_node]
            solution.appendleft(end_node)
            while solution:
                print(solution.popleft(), end=" ")
            print()


if __name__ == '__main__':
    main()
