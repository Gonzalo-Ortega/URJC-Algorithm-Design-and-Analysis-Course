# Que se enciendan las luces

def greedy_selection(partners, time):
    seduced_names = []
    benefit = 0
    for ratio, name, quality, required_time in partners:
        if required_time < time:
            seduced_names.append(name)
            benefit += quality
            time -= required_time
        else:
            seduced_names.append(name)
            benefit += ratio * time
            return seduced_names, benefit
    return seduced_names, benefit


def main():
    competitors_amount = int(input().strip())

    # We read and format the data needed for each participant:
    for competitor in range(competitors_amount):
        preferred_quality = input().strip()
        max_time = int(input().strip())
        partners_amount = int(input().strip())

        partners = [("ratio", "name", "quality", "required_time")] * partners_amount

        # We select the preferred quality and fill the required data for each partner:
        for partner in range(partners_amount):
            name, beauty, intelligence, kindness, required_time = input().strip().split()

            quality = 0
            if preferred_quality == "beauty":
                quality = int(beauty)
            elif preferred_quality == "intelligence":
                quality = int(intelligence)
            elif preferred_quality == "kindness":
                quality = int(kindness)

            required_time = int(required_time)
            ratio = quality/required_time
            partners[partner] = (ratio, name, quality, required_time)

        partners.sort(reverse=True)
        # We get the solution and format the output:
        seduced, benefit = greedy_selection(partners, max_time)

        seduced_names = ""
        for name in seduced:
            seduced_names += name + " "

        print(seduced_names)
        print("{:.2f}".format(benefit))


# Run program:
main()
