# Exploding kittens

def greedy_select_cards(cards, total_risk):
    selected_cards = []
    for ratio, name, risk, benefit in cards:
        selected_cards.append(name)
        if risk < total_risk:
            total_risk -= risk
        else:
            return selected_cards
    return selected_cards


def main():
    card_amount, total_risk = map(int, input().strip().split())
    cards = [("ratio", "name", "risk", "benefit")] * card_amount
    for card in range(card_amount):
        name, risk, benefit = input().strip().split()
        risk, benefit = map(int, (risk, benefit))
        ratio = benefit / risk
        cards[card] = ratio, name, risk, benefit

    cards.sort(reverse=True)
    selected_cards = greedy_select_cards(cards, total_risk)
    card_names = ""
    for name in selected_cards:
        card_names += name + " "
    print(card_names)


if __name__ == '__main__':
    main()
