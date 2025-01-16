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

def user_request():
    answer = input("Do you need any additional help?(Y/N) ")
    if answer == "Y":
        menu()
    else:
        print("Alright, continue shopping.")   
user_request()

def menu():
    print("\n **Joshua's Soccer Shop Menu**")
    print("1. NF")
    print("2. NF")
    print("3. NF")
    print("4.Exit \n")
    options = int(input("Select a number from 1-4: "))
    options()
menu()    

def options():
    options = int(input("Select a number from 1-4: "))
    if options == 1:
        print("NF")
    elif options == 2:
        print("NF")   
    elif options == 3:
        print("NF")    
    elif options == 4:
        print("Goodbye...")    
    else:
        exit
options()            

