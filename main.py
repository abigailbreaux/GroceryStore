import tkinter as tk

root = tk.Tk()
root.title("Shopping Cart")
root.geometry("400x300")

# declare cart as a global variable
cart = {}

# add item to cart function
def add_item(item_name, item_price):
    if item_name in cart:
        cart[item_name]["quantity"] += 1
    else:
        cart[item_name] = {"quantity": 1, "price": item_price}
    result_label.config(text=f"{item_name} selected")
    back_to_menu()

# view cart function
def view_cart():
    if not cart:
        result_label.config(text="Your cart is empty")
        return
    result_label.config(text="Items in your cart:\n")
    for item in cart:
        item_quantity = cart[item]["quantity"]
        item_price = cart[item]["price"]
        result_label.config(text=result_label.cget("text") + f"{item} ({item_quantity}) - ${item_quantity * item_price:.2f}\n")
    result_label.config(text=result_label.cget("text") + "------------------")

# checkout function
def checkout():
    if not cart:
        result_label.config(text="Your cart is empty")
        return
    total = 0
    for item in cart:
        item_quantity = cart[item]["quantity"]
        item_price = cart[item]["price"]
        item_total = item_quantity * item_price
        total += item_total
    result_label.config(text="------------------\n")
    for item in cart:
        item_quantity = cart[item]["quantity"]
        result_label.config(text=result_label.cget("text") + f"{item} ({item_quantity}) - ${item_quantity * cart[item]['price']:.2f}\n")
    result_label.config(text=result_label.cget("text") + "------------------\n")
    result_label.config(text=result_label.cget("text") + f"Total: ${total:.2f}\n")
    result_label.config(text=result_label.cget("text") + "Thank you for shopping with us!")

# Function to handle menu selections
# Function to handle menu selections
def menu_selection(selection):
    if selection == "add_item":
        menu_frame.pack_forget()
        cart_frame.pack()
    elif selection == "view_cart":
        view_cart()
    elif selection == "checkout":
        checkout()
        cart_frame.pack_forget()
        start_new_order_button.pack()
        add_item_button.pack_forget()
        view_cart_button.pack_forget()
        checkout_button.pack_forget()

# Cart frame
cart_frame = tk.Frame(root)

# Cart menu buttons
cookie_button = tk.Button(cart_frame, text="Cookie - $1.50", command=lambda: add_item("Cookie", 1.50), font=("Arial", 12))
cookie_button.pack(fill=tk.X, padx=10, pady=5)
sandwich_button = tk.Button(cart_frame, text="Sandwich - $4.00", command=lambda: add_item("Sandwich", 4.00), font=("Arial", 12))
sandwich_button.pack(fill=tk.X, padx=10, pady=5)
water_button = tk.Button(cart_frame, text="Water - $1.00", command=lambda: add_item("Water", 1.00), font=("Arial", 12))
water_button.pack(fill=tk.X, padx=10, pady=5)

# Back to menu button
def back_to_menu():
    cart_frame.pack_forget()
    menu_frame.pack()

back_button = tk.Button(cart_frame, text="Back to menu", command=back_to_menu, font=("Arial", 12))
back_button.pack(fill=tk.X, padx=10, pady=5)

# Start New Order button
def start_new_order():
    cart.clear()
    result_label.config(text="")
    start_new_order_button.pack_forget()
    menu_frame.pack()  # Add this line to repack the menu_frame

    # Add the following lines to repack the menu buttons
    add_item_button.pack()
    view_cart_button.pack()
    checkout_button.pack()

start_new_order_button = tk.Button(root, text="Start New Order", command=start_new_order, font=("Arial", 12))


# Main menu frame
menu_frame = tk.Frame(root)

# Menu buttons
add_item_button = tk.Button(menu_frame, text="Add item to cart", command=lambda: menu_selection("add_item"), font=("Arial", 12))
view_cart_button = tk.Button(menu_frame, text="View cart", command=lambda: menu_selection("view_cart"), font=("Arial", 12))
checkout_button = tk.Button(menu_frame, text="Checkout", command=lambda: menu_selection("checkout"), font=("Arial", 12))

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12))

# Pack buttons in menu frame
add_item_button.pack(fill=tk.X, padx=10, pady=5)
view_cart_button.pack(fill=tk.X, padx=10, pady=5)
checkout_button.pack(fill=tk.X, padx=10, pady=5)

# Pack menu frame
menu_frame.pack()

# Pack result label
result_label.pack()

# Run the tkinter event loop
root.mainloop()


