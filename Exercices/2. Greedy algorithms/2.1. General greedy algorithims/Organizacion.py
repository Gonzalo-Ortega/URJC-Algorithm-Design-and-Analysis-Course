# Organizacion

def topological_sort(graph, incoming_edges):
    solution = []
    initial_nodes = []
    for node in range(len(graph)):
        if incoming_edges[node] == 0:
            initial_nodes.append(node)

    while initial_nodes:
        initial_nodes.sort()
        origin = initial_nodes.pop(0)
        solution.append(origin)
        for node in graph[origin]:
            incoming_edges[node] -= 1
            if incoming_edges[node] == 0:
                initial_nodes.append(node)

    return solution


def main():
    task_amount, dependencies_amount = map(int, input().strip().split())
    graph = [[] for _ in range(task_amount)]
    incoming_edges = [0] * task_amount

    for order in range(dependencies_amount):
        a, b = map(int, input().strip().split())
        graph[a].append(b)
        incoming_edges[b] += 1

    for task in topological_sort(graph, incoming_edges):
        print(str(task), end=" ")


if __name__ == '__main__':
    main()
