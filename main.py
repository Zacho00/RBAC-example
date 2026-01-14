#Log-in
def Role(username, password):
    if password == "password":
        if username == "user1":
            print('Welcome, Customer!')
        elif username == "user2":
            print('Welcome, Admin!')
        else:
            print("Username or Password invalid")
    else:
        print("Username or Password invalid")

#Access determined by Role(RBAC)
def Actions(username):
    while True:
        if username == "user1" or username == "user2":
            print("Please select what you would like to do")
            print("-Options-")
            print("View Menu")
            print("View Stock")
            print("-----------")
            choice = input("")
            if username == "user1" and choice == "View Menu":
                print("Cheese Burger $4.99")
                print("French Fries $1.50")
                break
            elif username == "user2" and choice == "View Stock":
                print("Beef Patties - 50")
                print("Cheese Slices - 70")
                print("Potatoes - 40")
                break
            else:
                print("You are not authorized for that action.")
        else:
            break

username = input("Please enter your username: ")
password = input("Please enter your password: ")

Role(username, password)
Actions(username)