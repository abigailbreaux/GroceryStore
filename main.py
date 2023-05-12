# declare cart as a global variable
cart = {}

# add item to cart function
def add_item():
    print("----CART MENU----")
    print("1: Cookie - $1.50")
    print("2: Sandwich - $4.00")
    print("3: Water - $1.00")
    item = input("Item: ")
    quantity = int(input("Quantity: "))
    if item == "1":
        item_name = "Cookie"
        item_price = 1.50
    elif item == "2":
        item_name = "Sandwich"
        item_price = 4.00
    elif item == "3":
        item_name = "Water"
        item_price = 1.00
    else:
        print("Invalid input")
        return
    if item_name in cart:
        cart[item_name]["quantity"] += quantity
    else:
        cart[item_name] = {"quantity": quantity, "price": item_price}
    if quantity == 1:
        print("Added 1", item_name)
    else:
        print("Added", quantity, item_name + "s")

# view cart function
def view_cart():
    if not cart:
        print("Your cart is empty")
        return
    print("------------------")
    for item in cart:
        print(f"{item} ({cart[item]['quantity']}) - ${cart[item]['quantity']*cart[item]['price']:.2f}")
    print("------------------")

# remove item function
def remove_item():
    if not cart:
        print("Your cart is empty.")
        return

    print("------------------")
    for i, item in enumerate(cart.items()):
        item_name = item[0]
        item_quantity = item[1]['quantity']
        item_price = item[1]['price']
        if item_quantity == 1:
            print(f"{i+1}. {item_name} ({item_quantity}) - ${item_quantity*item_price:.2f}")
        else:
            print(f"{i+1}. {item_name}s ({item_quantity}) - ${item_quantity*item_price:.2f}")
    print("------------------")

    while True:
        try:
            selection = int(input("Enter the number of the item to remove: "))
            if selection < 1 or selection > len(cart):
                raise ValueError
            break
        except ValueError:
            print("Invalid selection. Please try again.")

    item_name = list(cart.keys())[selection - 1]
    removed_item = cart.pop(item_name)
    item_quantity = removed_item['quantity']
    if item_quantity == 1:
        print(f"Removed {item_quantity} {item_name}")
    else:
        print(f"Removed {item_quantity} {item_name}s")
    print("------------------")

    for i, item in enumerate(cart.items()):
        item_name = item[0]
        item_quantity = item[1]['quantity']
        item_price = item[1]['price']
        if item_quantity == 1:
            print(f"{item_name} ({item_quantity}) - ${item_quantity*item_price:.2f}")
        else:
            print(f"{item_name}s ({item_quantity}) - ${item_quantity*item_price:.2f}")
    print("------------------")



# checkout function
def checkout():
    if not cart:
        print("Your cart is empty")
        return
    total = 0
    print("------------------")
    for item in cart:
        item_total = cart[item]['quantity']*cart[item]['price']
        print(f"{item} ({cart[item]['quantity']}) - ${item_total:.2f}")
        total += item_total
    print("------------------")
    print(f"Total: ${total:.2f}")
    print("Thank you for shopping with us!")
    quit()

while True:
    print("----MAIN MENU----")
    print("1: Add item to cart")
    print("2: View cart")
    print("3: Checkout")
    print("4: Remove item")
    selection = input("Selection: ")
    if selection == "1":
        add_item()
    elif selection == "2":
        view_cart()
    elif selection == "3":
        checkout()
    elif selection == "4":
        remove_item()
    else:
        print("Invalid selection. Please try again.")
