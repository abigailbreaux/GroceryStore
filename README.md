Final Project - GroceryStore
Abigail Breaux
5/12/2023
CSCI1620

The goal of this code is to implement a simple shopping cart application. It provides a menu-driven interface for users to add items to their cart, view the contents of the cart, remove items from the cart, and proceed to checkout. The code aims to provide a user-friendly shopping experience by allowing users to interactively manage their cart and obtain a total cost for the selected items. It serves as a foundation for building more complex e-commerce systems or as a learning exercise for understanding basic cart functionality. This project is an improved version of Lab 1 in CSCI1620. 

1. The code starts by declaring a global variable `cart` which will store the items added by the user.

2. The `add_item()` function prompts the user to select an item and quantity to add to the cart. Based on the user's input, the function determines the item name and price. If the item is already in the cart, the quantity is updated; otherwise, a new entry is added to the cart.

3. The `view_cart()` function displays the contents of the cart. If the cart is empty, it prints a corresponding message; otherwise, it iterates over the cart items and prints each item's name, quantity, and the total price.

4. The `remove_item()` function allows the user to remove an item from the cart. It displays the items in the cart along with their quantities and prices, and then prompts the user to select the item number to remove. The selected item is removed from the cart, and a confirmation message is displayed.

5. The `checkout()` function calculates and displays the total cost of the items in the cart. If the cart is empty, it prints a message indicating so. After displaying the total, a thank-you message is shown, and the program terminates.

6. The main code runs in an infinite loop, presenting a menu to the user. The user can select options to add an item, view the cart, proceed to checkout, or remove an item. Based on the user's selection, the corresponding function is called. If an invalid selection is made, an error message is displayed.

Overall, this code provides the functionality of a basic shopping cart system, allowing users to manage their cart, view the items, remove unwanted items, and complete their purchase.
