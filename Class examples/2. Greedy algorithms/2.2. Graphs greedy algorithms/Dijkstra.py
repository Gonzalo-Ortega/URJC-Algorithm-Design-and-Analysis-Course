# Dijkstra
# Calculates the shortest path from one node to each other.
# Does not work if there are negative weights.
# If all weight are 1, a breath-first search is better.
# A good exercise could be counting the edges that form a path.

def select_min_distance(distances, visited):
    min_distance = float('inf')
    best_item = None

    for i in range(1, len(distances)):
        if not visited[i] and distances[i] < min_distance:
            min_distance = distances[i]
            best_item = i

    return best_item


def greedy_dijkstra(origin, g):
    n = len(g)

    visited = [False] * n
    visited[origin] = True

    # We initialize the distances list:
    distances = [float('inf')] * n
    distances[origin] = 0
    for start, end, weight in g[origin]:
        distances[end] = weight

    # Greedy loop:
    # while not is_sol() and candidates:
    for _ in range(2, n):
        next_node = select_min_distance(distances, visited)
        visited[next_node] = True
        for start, end, weight in g[next_node]:
            distances[end] = min(distances[end], distances[start] + weight)

    return distances


def main():
    graph = [
        [],
        [(1, 2, 5), (1, 4, 5)],
        [(2, 5, 1)],
        [],
        [(4, 2, 1), (4, 3, 11), (4, 5, 6)],
        [(5, 3, 1)]
    ]

    node = 1

    print(greedy_dijkstra(node, graph))


if __name__ == '__main__':
    main()
