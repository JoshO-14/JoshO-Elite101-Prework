"""
Greet the user and ask for their information
"""
def greetings():
    print("Welcome to Joshua's Thrift Shop!") #greeting
    name = input("\nWhat is your name? ") #collecting user's name
    age = int(input(f"\nHello {name}, How old are you? "))#collecting user's age

    if age >= 18:#checking if user is old enough to shop
        print("\nYou are welcome to shop with us, and choose wisely!")
    elif age <= 17: 
        print("\nYou're pretty young to be shopping here, but take care!")
    else:
        print("Invalid age, please try again.")

def chat():#function to chat with user
        print("\nSelect from the list of help options below:\n")
        print(
            "1. Purchase items - to buy items\n"
            "2. Return an item - to return an item\n"
            "3. Exchange an item - to exchange an item\n"
            "4. View cart - to view your cart\n"
            "5. Checkout - checkout your items\n"
            "6. Exit - to exit\n"
        )
        return input("What would you like to do? Input the number of the option: ")#collecting user's choice

"""
Display items in stock
"""


def shop():#function to display items in stock
    print("\n Here are the items we have in stock:")
    print("1. Shoes - $50")
    print("2. Clothes - $30")
    print("3. Jewelry - $100")
    print("4. Hats - $20")
    print("5. Exit")

cart = []#empty list to store user's choice

"""
Ask user to make a purchase
"""

def user_purchase():
    while True:
        shop()
        choice = input("What would you like to buy? List the number of the item: ")#collecting user's choice
        
        if choice == "1":
            print("\nYou have chosen Shoes, that will be $50.")
            cart.append("1 pair of Shoes: 50")
        elif choice == "2":
            print("\nYou have chosen Clothes, that will be $30.")
            cart.append("1 set of Clothes: 30")
        elif choice == "3":
            print("\nYou have chosen Jewelry, that will be $100.")
            cart.append("1 piece of Jewelry: 100")
        elif choice == "4":
            print("\nYou have chosen Hats, that will be $20.")
            cart.append("1 Hat: 20")
        elif choice == "5":
            print("\nOh well, thank you for shopping with us!") 
            break
        else:
            print("\nInvalid choice, please try again.")   
        
        print(f"Here is your cart: {cart}")
        
        #Ask user if they would like to add more items to cart
        add_more = input("Would you like to add more items to your cart? (y/n) ")
        if add_more.lower() != "y":
            break


def checkout():#function to calculate total cost
    total_cost = 0
    for item in cart:
        total_cost += int(item.split(":")[1])
    print(f"Your total cost is ${total_cost}.")
    print("Thank you for shopping with us!")

def return_item():#function to return item
    user_return = input("Would you like to return an item? (y/n) ")
    if user_return.lower() == "y":
        print(f"Here is your cart: {cart}")
        item_return = input("Which item would you like to return? List the number of the item: ")
        for item in cart:
            if item_return in item:
                cart.remove(item)
                print(f"{item} has been removed from your cart.")
                print(f"Here is your updated cart: {cart}")
            else:
                print("Invalid item, please try again.")
    elif user_return.lower() == "n":
        print(f"Here is your cart: {cart}")
    else:
        print("Invalid input, please try again.")

def exchange_item():#function to exchange item
    user_exchange = input("Would you like to exchange an item? (y/n) ")
    if user_exchange.lower() == "y":
        print(f"Here is your cart: {cart}")
        item_exchange = input("Which item would you like to exchange? List the number of the item: ")
        for item in cart:
            if item_exchange in item:
                cart.remove(item)
                print(f"{item} has been removed from your cart.")
                user_purchase()
            else:
                print("Invalid item, please try again.")
    elif user_exchange.lower() == "n":
        print(f"Here is your cart: {cart}")
    else:
        print("Invalid input, please try again.")
#calling the function to return item     

def selection():
    while True:
        choice = chat()
        if choice == "1":
            user_purchase()
        elif choice == "2":
            return_item()    
        elif choice == "3":
            exchange_item()
        elif choice == "4":
            print(f"Here is your cart: {cart}")
        elif choice == "5":
            checkout()
            break
        elif choice == "6":
            print("Okay, thank you for shopping with us!")
            break
        else:
            print("Invalid input, please try again.")

if __name__ == "__main__":
    greetings()
    selection()


