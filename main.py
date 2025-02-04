"""
Greet the user and ask for their information
"""

print("Welcome to Joshua's Thrift Shop!") #greeting
name = input("\nWhat is your name? ") #collecting user's name
age = int(input(f"\nHello {name}, How old are you? "))#collecting user's age
if age >= 18:#checking if user is old enough to shop
    print("\nYou are welcome to shop with us, and choose wisely!")
elif age <= 17: 
    print("\nYou're pretty young to be shopping here, but take care!")
else:
    print("Invalid age, please try again.")

"""
Display items in stock and ask user to choose
"""


def shop():#function to display items in stock
    print("\n Here are the items we have in stock:")
    print("1. Shoes - $50")
    print("2. Clothes - $30")
    print("3. Jewelry - $100")
    print("4. Hats - $20")
    print("5. Exit")
cart = []#empty list to store user's choice
shop()#calling the function to display items in stock

def user_purchase():
    global choice 
    choice = str(input("What would you like to buy? List the number of the item: "))#collecting user's choice
    if choice == "1":
        print("You have chosen Shoes, that will be $50.")
        cart.append("1 pair of Shoes: 50")
    elif choice == "2":
        print("You have chosen Clothes, that will be $30.")
        cart.append("1 set of Clothes: 30")
    elif choice == "3":
        print("You have chosen Jewelry, that will be $100.")
        cart.append("1 piece of Jewelry: 100")
    elif choice == "4":
        print("You have chosen Hats, that will be $20.")
        cart.append("1 Hat: 20")
    elif choice == "5":
        print("Oh well, thank you for shopping with us!") 
    else:
        print("Invalid choice, please try again.")   
    user_purchase()#calling the function to display items in stock

    print(f"Here is your cart: {cart}")#displaying user's choice

def add_to_cart():#function to add more items to cart
    user_add_more = input("Would you like to add more items to your cart? (yes/no) ")
    if user_add_more.lower == "yes":
        user_purchase()
    elif user_add_more.lower == "no":
        print(f"Here is your cart: {cart}")
    else:
        print("Invalid input, please try again.")        
    add_to_cart()#calling the function to add more items to cart

def checkout():#function to calculate total cost
    total_cost = 0
    for item in cart:
        total_cost += int(item.split(":")[1])
    print(f"Your total cost is ${total_cost}.")
    print("Thank you for shopping with us!")

def return_item():#function to return item
    user_return = input("Would you like to return an item? (yes/no) ")
    if user_return.lower == "yes":
        print(f"Here is your cart: {cart}")
        item_return = input("Which item would you like to return? List the number of the item: ")
        for item in cart:
            if item_return in item:
                cart.remove(item)
                print(f"{item} has been removed from your cart.")
                print(f"Here is your updated cart: {cart}")
            else:
                print("Invalid item, please try again.")
    elif user_return.lower == "no":
        print(f"Here is your cart: {cart}")
    else:
        print("Invalid input, please try again.")
    return_item()#calling the function to return item     

def exchange_item():#function to exchange item
    user_exchange = input("Would you like to exchange an item? (yes/no) ")
    if user_exchange.lower == "yes":
        print(f"Here is your cart: {cart}")
        item_exchange = input("Which item would you like to exchange? List the number of the item: ")
        for item in cart:
            if item_exchange in item:
                cart.remove(item)
                print(f"{item} has been removed from your cart.")
                user_purchase()
            else:
                print("Invalid item, please try again.")
    elif user_exchange.lower == "no":
        print(f"Here is your cart: {cart}")
    else:
        print("Invalid input, please try again.")
    exchange_item()#calling the function to exchange item


def main():
    user_purchase()
    add_to_cart()
    checkout()
    return_item()
    exchange_item()
