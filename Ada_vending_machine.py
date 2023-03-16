def Ada_vending_machine(inventory, choice, funds):

    print("Welcome to Ada's Vending Machine")
    print("Here are the available items:")


# Display items within the vending machines:
    print(inventory)

    # check if user made a valid choice
    valid_choice = False

    for i in range(len(inventory)):
        if choice == inventory[i]['item_number']:
            if inventory[i]['price'] <= funds:
                print(
                    f"Thank you for your purchase! your change is ${funds - inventory[i]['price']}")
                inventory[i]['quantity'] -= 1
                print(inventory)
            else:
                print(
                    f"That is not enough money to purchase {inventory[i]['name']}")
            valid_choice = True
            break

    # check choice is invalid:
    if valid_choice == False:
        print("That is an invalid choice")


inventory = [
    {
        'name': 'Ada Chips',
                'item_number': 'A1',  # key = value
                'price': 0.50,
                'quantity': 5

    },
    {
        'name': 'Ada Candy Bar',
                'item_number': 'A2',
                'price': 0.75,
                'quantity': 5
    },
    {
        'name': 'Ada Gum',
                'item_number': 'A3',
                'price': 0.25,
                'quantity': 5
    },
]
choice = 'A1'
funds = 1.00

Ada_vending_machine(inventory, choice, funds)
