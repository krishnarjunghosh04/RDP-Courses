# Assignment 8: Shopping Cart Total Write a program that simulates a shopping cart.
# Prompt the user to enter the prices of items they want to buy.
# After they're done, calculate and print the total cost of all the items in the cart.
def shopping_cart():
    print("""Welcome to RDP Shopping
Please scan your item to proceed""")
    total = 0.0
    print("Enter the prices of the items. Type 'done' when finished.\n")
    while True:
        price = input("Enter the price of the item: ")
        if price.lower() == 'done':
            break
        try:
            price = float(price)
            if price <= 0:
                print("Price cannot be less than 0.Try again.")
                continue
            total += price
        except ValueError:
            print("Invalid input. Please enter a number or done.")
    print("The total is", total)
shopping_cart()
