# Topological sort
# Orders a given set of objects following certain priorities.
# Uses a great amount of dictionaries to learn how to use them.

from collections import deque


def topological_sort_visit(data, k):
    # We mark the node as visited and advance the time:
    data["state"][k] = "VISITED"
    data["time"] += 1
    data["discover"][k] = data["time"]

    # We check the state of all son nodes:
    for adj in data["graph"][k]:
        if data["state"][adj] == "NOT VISITED":
            topological_sort_visit(data, adj)

    # If there are no more unvisited nodes after the current, we add it to the solution:
    data["state"][k] = "FINISH"
    data["time"] += 1
    data["end"][k] = data["time"]
    data["solution"].appendleft(k)


def topological_sort(g):
    # We make a dictionary with all the data we need to save:
    data = {
        "graph": g,
        "state": dict(),  # Saves whether the node is VISITED, NOT VISITED or FINISH.
        "discover": dict(),  # Saves the time when the node is first visited.
        "end": dict(),  # Saves the time when the node can be placed.
        "time": 0,  # Counts the current iteration.
        "solution": deque()
    }
    # We initialize the data dictionaries:
    for k in g.keys():
        data["state"][k] = "NOT VISITED"
        data["discover"][k] = 0
        data["end"][k] = 0

    # We loop over all the nodes:
    for k in g.keys():
        if data["state"][k] == "NOT VISITED":
            topological_sort_visit(data, k)

    return data["solution"]


def main():
    graph = {
        "socks": ["shoes"],
        "trouser": ["shoes", "belt"],
        "shirt": ["belt", "sweater"],
        "shoes": [],
        "belt": [],
        "sweater": []
    }

    print(topological_sort(graph))


if __name__ == '__main__':
    main()
