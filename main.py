print("Welcome to Joshua's Soccer Shop!")

def user_name_age():
    name = input("What is your name? ")
    age = int(input(f"Hello, {name}, how old are you? "))
    if age < 14:
        print("You're pretty young to be shopping here...")
    elif 14<= age <18:
        print("I guess you're here to blow your hard earned money away...")  
    elif age>=18:
        print("Have fun shopping!")
    else:
        print("Please retry and enter a valid age.")          
user_name_age() 


#def user_request():
# print("HOLD")
#user_request()
#def menu():
 #   choice = input("Select the number that you have questions pertaining to: ")
