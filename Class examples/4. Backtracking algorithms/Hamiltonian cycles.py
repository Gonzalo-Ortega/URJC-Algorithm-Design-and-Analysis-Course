# Hamiltonian cycles
# Count the amount of hamiltonian cycles in a given graph

def is_solution(graph, case, node):
    return node == case[0] and len(case) == len(graph) + 1


def is_feasible(node, case, graph_len):
    return node not in case or (node == case[0] and len(case) == graph_len)


def backtracking_hamiltonian(graph, node, case, solution_amount):
    if is_solution(graph, case, node):
        solution_amount += 1
    else:
        for adj in graph[node]:
            if is_feasible(adj, case, len(graph)):
                case.append(adj)
                solution_amount = backtracking_hamiltonian(graph, adj, case, solution_amount)
                case.pop()
    return solution_amount


def main():
    node_amount = 5
    edges = [(0, 1), (0, 3), (1, 2), (1, 3), (1, 4), (2, 4), (3, 4)]
    graph = [[] for _ in range(node_amount)]
    for start, end in edges:
        graph[start].append(end)
        graph[end].append(start)

    initial_node = 0
    initial_case = [initial_node]
    solution_amount = backtracking_hamiltonian(graph, initial_node, initial_case, 0)
    print(solution_amount)


if __name__ == "__main__":
    main()
