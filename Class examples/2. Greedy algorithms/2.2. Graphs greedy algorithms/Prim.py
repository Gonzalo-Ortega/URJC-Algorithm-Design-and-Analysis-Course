# Prim (Greedy algorithm to find a graph minimal recovery tree)
from random import randint


def select_min(visited, candidates):
    vertex = None
    weight = float('inf')
    for i in range(1, len(candidates)):
        if not visited[i] and candidates[i] < weight:
            vertex = i
            weight = candidates[i]
    return vertex, weight


def greedy_prim(g):
    n = len(g)
    candidates = [float('inf')] * n
    initial = randint(1, n - 1)
    for start, end, weight in g[initial]:
        candidates[end] = weight
    solution = 0
    visited = [False] * n
    visited[initial] = True

    # Greedy loop:
    for i in range(2, n):
        next_vertex, cost = select_min(visited, candidates)
        visited[next_vertex] = True
        solution += cost
        for start, end, weight in g[next_vertex]:
            if not visited[end]:
                candidates[end] = min(weight, candidates[end])
    return solution


def main():
    graph = [
        [],
        [(1, 3, 1), (1, 4, 2), (1, 7, 6)],  # Adjacent nodes to node 1.
        [(2, 5, 2), (2, 6, 4), (2, 7, 7)],
        [(3, 1, 1), (3, 4, 3), (3, 7, 5)],
        [(4, 1, 2), (4, 3, 3), (4, 5, 1), (4, 6, 9)],
        [(5, 2, 2), (5, 4, 1), (5, 7, 8)],
        [(6, 2, 4), (6, 4, 9)],
        [(7, 1, 6), (7, 2, 7), (7, 3, 5), (7, 5, 8)]
    ]

    print(greedy_prim(graph))


if __name__ == '__main__':
    main()
