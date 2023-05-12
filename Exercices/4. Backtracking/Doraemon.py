# Doraemon
# Knapsack problem picking just one copy, without dividing items, and total global restrictions.

import copy
from math import inf


def is_solution(solution, items):
    min_weight = inf
    for item in range(items['amount']):
        if not items['picked'][item] and items['weight'][item] < min_weight:
            min_weight = items['weight'][item]

    return solution['total_weight'] + min_weight > items['max_weight'] and solution['id_sum'] % 5 != 0


def is_feasible(solution, item, items):
    return solution['total_weight'] + items['weight'][item] <= items['max_weight']


def knapsack(solution, best_solution, items, current_item):
    if is_solution(solution, items):
        if solution['total_value'] > best_solution['total_value']:
            best_solution = copy.deepcopy(solution)
    else:
        for item in range(current_item, items['amount']):
            if is_feasible(solution, item, items):
                solution['total_weight'] += items['weight'][item]
                solution['total_value'] += items['value'][item]
                solution['id_sum'] += items['id'][item]
                items['picked'][item] = True

                best_solution = knapsack(solution, best_solution, items, item + 1)

                solution['total_weight'] -= items['weight'][item]
                solution['total_value'] -= items['value'][item]
                solution['id_sum'] -= items['id'][item]
                items['picked'][item] = False

    return best_solution


def main():
    item_amount, max_weight = map(int, input().strip().split())
    items = {
        'id': [],
        'value': [],
        'weight': [],
        'picked': [False] * item_amount,
        'amount': item_amount,
        'max_weight': max_weight
    }
    for _ in range(item_amount):
        item_id, value, weigh = map(int, input().strip().split())
        items['id'].append(item_id)
        items['value'].append(value)
        items['weight'].append(weigh)

    solution = {
        'total_weight': 0,
        'total_value': 0,
        'id_sum': 0
    }

    best_solution = copy.deepcopy(solution)

    current_item = 0

    solution = knapsack(solution, best_solution, items, current_item)
    print(solution['total_value'])


if __name__ == "__main__":
    main()
