# Knapsack
# Maximize value of items placed in a knapsack with weight limits.

# Only guarantees the best solution if objects can be divided.
# Can be optimized sorting the data.

# "La mejor improvisación es aquella que se ha preparado previamente"

def get_best_item(candidates, data):
    best_item = -1
    best_ratio = -1
    for candidate in candidates:
        ratio = data['profit'][candidate]/data['weight'][candidate]
        if ratio > best_ratio:
            best_ratio = ratio
            best_item = candidate
    return best_item


def is_feasible(best_item, free_weight, data):
    return free_weight - data['weight'][best_item] >= 0


def greedy_knapsack(data):
    # We initialize the candidates and the solution:
    candidates = set()
    items = len(data['profit'])
    solution = [0] * items
    for item in range(items):
        candidates.add(item)

    free_weight = data['max_weight']
    is_solution = False

    # Greedy loop:
    while not is_solution and candidates:
        best_item = get_best_item(candidates, data)
        candidates.remove(best_item)
        if is_feasible(best_item, free_weight, data):
            solution[best_item] = 1.0
            free_weight -= data['weight'][best_item]
        else:
            ratio = free_weight/data['weight'][best_item]
            solution[best_item] = ratio
            is_solution = True
    return solution


def main():
    data = {
        'profit': [20, 30, 66, 40, 60],
        'weight': [10, 20, 30, 40, 50],
        'max_weight': 100
    }
    print(greedy_knapsack(data))


# Run program:
main()
