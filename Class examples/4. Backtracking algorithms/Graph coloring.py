# Graph Coloring
# Find a suitable coloring for a given graph.


def is_solution(node, graph):
    return node == len(graph)


def is_feasible(graph, case, node, color):
    for adj in graph[node]:
        if adj < node:
            if color == case[adj]:
                return False
    return True


def backtracking_coloring(graph, case, node, max_colors):
    if is_solution(node, graph):
        success = True
    else:
        success = False
        color = 1
        while color <= max_colors:
            if is_feasible(graph, case, node, color):
                case[node] = color
                case, success = backtracking_coloring(graph, case, node + 1, max_colors)
                if not success:
                    case[node] = 0
            color += 1
    return case, success


def main():
    graph = [
        [1, 2, 3],
        [0],
        [0, 3],
        [0, 2]
    ]
    initial_node = 0
    max_colors = 4
    initial_case = [0] * len(graph)
    solution, success = backtracking_coloring(graph, initial_case, initial_node, max_colors)

    print(solution if success else "No solution")


if __name__ == "__main__":
    main()
