def calculate_discounted_price(burgers, sides, drinks):
    total_original_price = sum(burgers) + sum(sides) + sum(drinks)
    max_sets = min(len(burgers), len(sides), len(drinks))

    burgers.sort(reverse=True)
    sides.sort(reverse=True)
    drinks.sort(reverse=True)

    discounted_price = 0

    for i in range(max_sets):
        set_price = burgers[i] + sides[i] + drinks[i]
        discounted_price += set_price * 0.9
    discounted_price += sum(burgers[max_sets:])
    discounted_price += sum(sides[max_sets:])
    discounted_price += sum(drinks[max_sets:])

    return total_original_price, int(discounted_price)

if __name__ == "__main__":
    b, c, d = map(int, input().split())
    burgers = list(map(int, input().split()))
    sides = list(map(int, input().split()))
    drinks = list(map(int, input().split()))
    total_original_price, discounted_price = calculate_discounted_price(burgers, sides, drinks)

    print(total_original_price)
    print(discounted_price)