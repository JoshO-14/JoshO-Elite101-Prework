import random 

print("Welcome to Joshua's Clothing Store!")

def user_name_age(): #collect user information
    name = input("What is your name? ")#ask for user name
    age = int(input(f"Hello, {name}, how old are you? "))#ask for user age
    if age < 14: #set dialogues for each age
        print("You're pretty young to be shopping here...")
    elif 14<= age <18:
        print("I guess you're here to blow your new paycheck away...")  
    elif age>=18:
        print("Have fun shopping!")
    else:
        print("Please retry and enter a valid age.")          
user_name_age() #call to action

def options(): #menu for help
    print("\n **Joshua's Thrift Shop Clothing Store Menu**")
    print("1. Return Item")
    print("2. Exchange Item")
    print("3. View Stock/Inventory")
    print("4. Exit \n")
    options = int(input("Select a number from 1-4: "))
    if options == 1:
        print("NF")
    elif options == 2:
        print("NF")   
    elif options == 3:
        inventory()   
    elif options == 4:
        print("Goodbye...")    
    else:
        exit

def inventory():
    inventory = [
 {'prod_Id': 4327, 'type': 'Shirt', 'price': 70.0, 'stock': 20, 'brand': 'Ralph Lauren'},
 {'prod_Id': 3915, 'type': 'Sweater', 'price': 90.0, 'stock': 32, 'brand': 'Champion'},
 {'prod_Id': 2119, 'type': 'Jeans', 'price': 34.0, 'stock': 19, 'brand': 'Levis'},
 {'prod_Id': 1194, 'type': 'Shoes', 'price': 20.0, 'stock': 5, 'brand': 'Timberland'},  
 {'prod_Id': 1300, 'type': 'Hoodies', 'price': 30.0, 'stock': 3, 'brand': 'Nike'},
 {'prod_Id': 1118, 'type': 'Hats', 'price': 15.0, 'stock': 10, 'brand': 'New Era'}, 
 {'prod_Id': 1664, 'type': 'Jewleries', 'price': 7.0, 'stock': 5, 'brand': 'Cartier'},
] 
class Product:
    def __init__(self, type, price, stock, brand):
        self.prod_id = random.randint(1000,5000)
        self.type = type
        self.price = price
        self.stock = stock
        self.brand = brand
    def features(self):
        ft = {'prod_id': self.prod_id, 'type': self.type, 'price': self.price, 'stock': self.stock, 'brand': self.brand}
        return ft



def user_request():
    answer = input("\n Hey there, do you need any additional help? (Y/N) ")
    if answer == "Y" or answer == "y":
        options()
    elif answer == "N" or answer == "n":
        print("Alrighty, continue shopping!")    
    else:
        exit   
user_request()



