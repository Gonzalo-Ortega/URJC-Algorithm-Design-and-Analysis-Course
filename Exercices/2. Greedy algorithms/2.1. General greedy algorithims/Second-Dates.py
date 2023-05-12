# Second Dates
import sys


def get_best_competitor(candidates):
    lowest_age = sys.maxsize
    for age, name in candidates:
        if age < lowest_age:
            lowest_age = age
            best_candidate = age, name
    return best_candidate


def greedy_group_by_ages(competitors, young_group_size):
    # We initialize the groups and the candidates:
    young_group, old_group = [], []
    candidates = set()
    for candidate in competitors:
        candidates.add(candidate)
    picked_candidates = 0

    # Greedy loop to add the required young candidates:
    while picked_candidates < young_group_size and candidates:
        best_competitor = get_best_competitor(candidates)
        young_group.append(best_competitor)
        candidates.remove(best_competitor)
        picked_candidates += 1

    # We add the rest of the candidates to the old group:
    for candidate in candidates:
        old_group.append(candidate)

    # We sort the groups by age:
    young_group.sort()
    old_group.sort()

    return young_group, old_group


def get_age_difference(young_group, old_group):
    old_total = 0
    for age, name in old_group:
        old_total += age

    young_total = 0
    for age, name in young_group:
        young_total += age

    return old_total - young_total


def main():
    competitor_number, group_size = map(int, input().strip().split())

    competitors = [("age", "name")] * competitor_number

    for competitor in range(competitor_number):
        name, age = input().strip().split()
        competitors[competitor] = (int(age), name)

    # We compare which of the two possible combinations is best
    young_group_a, old_group_a = greedy_group_by_ages(competitors, group_size)
    young_group_b, old_group_b = greedy_group_by_ages(competitors, competitor_number - group_size)

    if get_age_difference(young_group_a, old_group_a) > get_age_difference(young_group_b, old_group_b):
        young_group, old_group = young_group_a, old_group_a
    else:
        young_group, old_group = young_group_b, old_group_b

    # We get and print the names of each group:
    young_names = ""
    for age, name in young_group:
        young_names += name + " "

    old_names = ""
    for age, name in old_group:
        old_names += name + " "

    print(young_names)
    print(old_names)


main()
