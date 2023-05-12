# Kruskal (Greedy algorithm to find a graph minimal recovery tree)
# In each iteration choose the sortest edge.

def sort_candidates(g):
    candidates = []
    for adjacent_list in g:
        for (start, end, weight) in adjacent_list:
            # Weight is moved to the first place to use the python sort function:
            candidates.append((weight, start, end))
    candidates.sort()
    return candidates


def update_components(components, new_id, old_id):
    for i in range(1, len(components)):
        if components[i] == old_id:
            components[i] = components[new_id]


def greedy_kruskal(g):
    # Candidates definition:
    candidates = sort_candidates(g)

    # Initialize solution:
    solution = 0
    components = list(range(len(g)))  # [0, 1, 2, ..., 7]
    number_of_components = len(components) - 1

    # Greedy loop:
    i = 0
    while number_of_components > 1 and i < len(candidates):  # Check if is solution and loop over all candidates
        # Get best item
        (weight, start, end) = candidates[i]
        if components[start] != components[end]:
            solution += weight
            number_of_components -= 1
            update_components(components, components[start], components[end])
        i += 1

    return solution


def main():
    graph = [
        [],
        [(1, 3, 1), (1, 4, 2), (1, 7, 6)],  # Adjacent nodes to node 1. (start, end, weight)
        [(2, 5, 2), (2, 6, 4), (2, 7, 7)],
        [(3, 1, 1), (3, 4, 3), (3, 7, 5)],
        [(4, 1, 2), (4, 3, 3), (4, 5, 1), (4, 6, 9)],
        [(5, 2, 2), (5, 4, 1), (5, 7, 8)],
        [(6, 2, 4), (6, 4, 9)],
        [(7, 1, 6), (7, 2, 7), (7, 3, 5), (7, 5, 8)]
    ]

    print(greedy_kruskal(graph))


if __name__ == "__main__":
    main()