# Dora la repartidora
# Minimize waiting time.

def greedy_waiting_time(clients):
    total_waiting_time = 0
    clients.sort()
    remaining_deliveries = len(clients)
    for delivery_time in clients:
        total_waiting_time += delivery_time * remaining_deliveries
        remaining_deliveries -= 1
    return total_waiting_time


def main():
    client_amount = int(input().strip())
    clients = [0] * client_amount
    for delivery_time in range(client_amount):
        code, clients[delivery_time] = map(int, input().strip().split())
    print(greedy_waiting_time(clients))


if __name__ == '__main__':
    main()
