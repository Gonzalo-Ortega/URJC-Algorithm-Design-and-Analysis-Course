# Schedule
# Optimize obtained profit delivering tasks that expire over time.

def get_best_item(data, candidates):
    best_item = -1
    best_profit = -1
    for candidate in candidates:
        profit = data['profit'][candidate]
        if profit > best_profit:
            best_profit = profit
            best_item = candidate
    return best_item


def greedy_schedule(data):
    # We initialize the candidates and the solution:
    candidates = set()
    n = len(data['profit'])

    for i in range(n):
        candidates.add(i)

    schedule = [-1] * n
    last_date = max(data['deadline'])
    time = 0

    # Greedy loop:
    while time <= last_date and candidates:
        best_item = get_best_item(data, candidates)
        candidates.remove(best_item)
        execution_time = data['deadline'][best_item]
        found = False
        while execution_time >= 0 and not found:
            if schedule[execution_time] == -1:
                schedule[execution_time] = best_item
                found = True
            execution_time -= 1
        time += 1

    return schedule


def main():
    data = {
        'profit': [50, 10, 15, 30],
        'deadline': [2, 1, 2, 1]
    }
    print(greedy_schedule(data))


if __name__ == '__main__':
    main()
