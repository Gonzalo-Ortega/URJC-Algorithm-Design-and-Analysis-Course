# Knapsack 01
# Knapsack problem where items can be piked various times but can't be divided.

import copy


def best(solution_1, solution_2):
    if solution_1['current_value'] > solution_2['current_value']:
        best_solution = copy.deepcopy(solution_1)
    else:
        best_solution = copy.deepcopy(solution_2)
    return best_solution


def is_solution(solution, data):
    return solution['accumulated_weight'] + min(data['weight']) > data['max_weight']


def is_feasible(solution, item, data):
    return solution['accumulated_weight'] + data['weight'][item] <= data['max_weight']


def assign(solution, item, data):
    solution['items'][item] += 1
    solution['current_value'] += data['value'][item]
    solution['accumulated_weight'] += data['weight'][item]
    return solution


def delete(solution, item, data):
    solution['items'][item] -= 1
    solution['current_value'] -= data['value'][item]
    solution['accumulated_weight'] -= data['weight'][item]
    return solution


def backtracking_knapsack(solution, best_solution, data, level):
    if is_solution(solution, data):
        best_solution = best(solution, best_solution)
    else:
        for item in range(level, data['size']):
            if is_feasible(solution, item, data):
                solution = assign(solution, item, data)
                best_solution = backtracking_knapsack(solution, best_solution, data, item)
                solution = delete(solution, item, data)
    return best_solution


def initialize_data():
    data = {
        'size': 4,
        'max_weight': 8,
        'weight': [2, 3, 4, 5],
        'value': [3, 5, 6, 10]
    }
    return data


def initialize_solution(data):
    solution = {
        'accumulated_weight': 0,
        'current_value': 0,
        'items': [0] * data['size']
    }
    return solution


def main():
    data = initialize_data()
    solution = initialize_solution(data)
    best_solution = initialize_solution(data)
    solution_level = 0
    best_solution = backtracking_knapsack(solution, best_solution, data, solution_level)
    print(best_solution)


if __name__ == "__main__":
    main()
