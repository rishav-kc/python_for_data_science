inventory = {
    "Widget": 10,
    "Gadget": 5,
    "Sensor": 0,
    "Cable": 15
}

orders = [
    ["Widget", 3],
    ["Sensor", 2],
    ["Gadget", 7],
    ["Cable", 5],
    ["Phone", 2]
]

unfulfilled = []
fully_fulfilled = 0

for order in orders:
    item = order[0]
    requested = order[1]

    stock = inventory.get(item)

    if stock is None:
        print("Item not found:", item)
        unfulfilled.append([item, requested])

    elif stock == 0:
        print("Out of stock:", item)
        unfulfilled.append([item, requested])

    elif stock >= requested:
        inventory[item] = stock - requested
        fully_fulfilled = fully_fulfilled + 1
        print("Order fully fulfilled:", item)

    else:
        remaining = requested - stock
        inventory[item] = 0
        unfulfilled.append([item, remaining])

        print("Order partially fulfilled:", item)
        print("Unfulfilled quantity:", remaining)


print()
print("Final inventory:", inventory)
print("Fully fulfilled orders:", fully_fulfilled)
print("Unfulfilled orders:", unfulfilled)