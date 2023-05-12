# Mercato
# Greedy knapsack with several pickers of the same items.

import math


def pick_best_player(manager, players):
    best_player = None
    best_ratio = 0

    for name, price, qualities in players:
        ratio = int(qualities[manager]) / price
        if ratio > best_ratio:
            best_player = (name, price, qualities)
            best_ratio = ratio

    return best_player, best_ratio


def knapsack(managers, players):
    for manager in managers['id']:
        while managers['money'][manager] > 0 and len(players) > 0:
            best_player, ratio = pick_best_player(manager, players)
            players.remove(best_player)
            name, price, qualities = best_player

            if price < managers['money'][manager]:
                managers['money'][manager] -= price
                managers['earnings'][manager] += int(qualities[manager])
            else:
                managers['earnings'][manager] += ratio * managers['money'][manager]
                managers['money'][manager] = 0

            managers['players'][manager].append(name)

    return managers


def main():
    manager_amount, players_amount, max_money = map(int, input().strip().split())

    managers = {
        'id': [],
        'name': [],
        'money': [max_money] * manager_amount,
        'earnings': [0] * manager_amount,
        'players': [[] for _ in range(manager_amount)]
    }
    for manager_id in range(manager_amount):
        managers['id'].append(manager_id)
        managers['name'].append(input())

    players = []
    for _ in range(players_amount):
        qualities = list(input().strip().split())
        name = qualities.pop(0)
        price = int(qualities.pop(0))
        players.append((name, price, qualities))

    managers = knapsack(managers, players)

    for manager in managers['id']:
        print(managers['name'][manager] + ": " + str(math.ceil(managers['earnings'][manager])))
        managers['players'][manager].sort()
        for player in managers['players'][manager]:
            print(player)


if __name__ == "__main__":
    main()
