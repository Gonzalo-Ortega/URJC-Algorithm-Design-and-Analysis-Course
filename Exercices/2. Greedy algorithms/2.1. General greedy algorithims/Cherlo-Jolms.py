# Cherlo Jolms
# Knapsack problem allowing the division of items.

def greedy_case_selection(cases, money):
    selected_cases = []
    total_earnings = 0
    for ratio, case, cost, earnings in cases:
        if money > cost:
            selected_cases.append(case)
            money -= cost
            total_earnings += earnings
        elif money < cost:
            selected_cases.append(case)
            total_earnings += money * ratio
            selected_cases.sort()
            return selected_cases, total_earnings

    return selected_cases, total_earnings


def main():
    case_amount, money = map(int, input().strip().split())
    cases = [("ratio", "number", "cost", "earnings")] * case_amount
    for case in range(case_amount):
        cost, earnings = map(int, input().strip().split())
        ratio = earnings / cost
        cases[case] = (ratio, case, cost, earnings)
    cases.sort(reverse=True)
    selected_cases, total_earnings = greedy_case_selection(cases, money)
    for case in selected_cases:
        print(str(case), end=" ")
    print("\n" + str(round(total_earnings)))


if __name__ == '__main__':
    main()
