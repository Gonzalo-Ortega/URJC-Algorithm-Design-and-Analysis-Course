# Discord
# Graph coloring increasing color amount until success.

def is_feasible(graph, case, node, color):
    for adj in graph[node]:
        if adj < node:
            if color == case[adj]:
                return False
    return True


def coloring_count(graph, solution, node, color_amount):
    if node == len(graph):
        success = True
    else:
        success = False
        color = 1
        while not success and color <= color_amount:
            if is_feasible(graph, solution, node, color):
                solution[node] = color
                case, success = coloring_count(graph, solution, node + 1, color_amount)
            if not success:
                solution[node] = 0
            color += 1
    return solution, success


def main():
    node_amount, edge_amount = map(int, input().strip().split())
    graph = [[] for _ in range(edge_amount)]
    for _ in range(edge_amount):
        a, b = map(int, input().strip().split())
        graph[a].append(b)
        graph[b].append(a)

    solution = [0] * len(graph)
    start_node = 0
    color_amount = 1
    success = False

    while not success:
        color_amount += 1
        solution, success = coloring_count(graph, solution, start_node, color_amount)

    print(color_amount)


if __name__ == "__main__":
    main()
