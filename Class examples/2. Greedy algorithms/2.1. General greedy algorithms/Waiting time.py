# Waiting time
# Minimize the waiting time in a system that needs to deliver a fixed amount of tasks.

# Coins, does not guarantee the best solution.

import random
import sys


def get_best_task(task_times, candidates):
    best_task_time = sys.maxsize  # Initialize the best time to the maximum.
    for candidate in candidates:
        time = task_times[candidate]
        if time < best_task_time:
            best_task_time = time
            best_task = candidate
    return best_task


def greedy_waiting_time(task_times):
    # We initialize the candidates and the solution:
    candidates = set()
    solution = []
    for task in range(len(task_times)):
        candidates.add(task)

    # Greedy loop:
    while candidates:  # and not isSol(): This part is relevant if the sol does not require all candidates.
        best_task = get_best_task(task_times, candidates)
        solution.append(best_task)
        candidates.remove(best_task)

    return solution


def main():
    number_of_elements = 10
    task_times = []
    for i in range(number_of_elements):
        # Each task needs a random time between 44 and 140 to be completed.
        task_times.append(random.uniform(44, 140))

    print(task_times)
    print(greedy_waiting_time(task_times))


# Run program:
main()
