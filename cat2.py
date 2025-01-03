import json

def data(path="data.json"): 

    info=open(path,"r")
    Read=file.read()
    info.close()

    if Read=="":
        return[]
    
    return json.loads(Read)


def put_data(users):
    info= open(path, "w")  
    info.write(json.dumps(users, indent=4)) 
    info.close()


def check_files(file):
    try:
        c=open(file_name)
        c.close()
        return True
    except:
        return False
    

def register():
    print("Register a new user")     
    User_Name=input("Enter username: ")
    Email = input("Enter email: ")
    Pass = input("Enter password: ")

    users=data()

    for user in users:
        if user["Email"]==Email:
             print("This Email is already used")
             return
        
    new_user={"Username":Username, "Email":Email, "Password":Password}
    users.append(new_user)
    put_data(users)  # Save data
    print("User registered.")    



def login():
    print("Login to your account")
    Email = input("Enter email: ")
    Password = input("Enter password: ")

    users = data()  # Get current data

    for user in users:
        if user["email"] == Email and user["password"] == Password:
            print("Welcome again,",user["username"] )
            return

    print("Wrong email or password!")




def main():
    while True:
        print("Simple User System ")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please Try again.")







# import json

# # File to store user data
# DATA_FILE = "data.json"

# # Load data from the file
# def load_data():
#     if not file_exists(DATA_FILE):  # Check if file exists
#         return []  # If no file, return empty list

#     file = open(DATA_FILE, "r")  # Open the file in read mode
#     data = file.read()  # Read the file content
#     file.close()  # Close the file

#     if data == "":  # If file is empty
#         return []  # Return empty list

#     return json.loads(data)  # Convert JSON to Python object

# # Save data to the file
# def save_data(users):
#     file = open(DATA_FILE, "w")  # Open the file in write mode
#     file.write(json.dumps(users, indent=4))  # Write JSON to file
#     file.close()  # Close the file

# # Check if file exists
# def file_exists(filename):
#     try:
#         f = open(filename)
#         f.close()
#         return True
#     except:
#         return False

# # Register a new user
# def register_user():
#     print("\nRegister a new user")
#     username = input("Enter username: ")
#     email = input("Enter email: ")
#     password = input("Enter password: ")

#     users = load_data()  # Get current data

#     # Check if email already exists
#     for u in users:
#         if u["email"] == email:
#             print("Error: This email is already used!")
#             return

#     # Add user to list
#     new_user = {"username": username, "email": email, "password": password}
#     users.append(new_user)
#     save_data(users)  # Save data
#     print("User registered!")

# # Login user
# def login_user():
#     print("\nLogin to your account")
#     email = input("Enter email: ")
#     password = input("Enter password: ")

#     users = load_data()  # Get current data

#     # Check if email and password match
#     for u in users:
#         if u["email"] == email and u["password"] == password:
#             print("Welcome back,", u["username"] + "!")
#             return

#     print("Error: Wrong email or password!")

# # Main menu
# def main():
#     while True:
#         print("\n--- Simple User System ---")
#         print("1. Register")
#         print("2. Login")
#         print("3. Exit")

#         choice = input("Choose an option: ")

#         if choice == "1":
#             register_user()
#         elif choice == "2":
#             login_user()
#         elif choice == "3":
#             print("Goodbye!")
#             break
#         else:
#             print("Invalid option. Try again.")

# # Run the program
# main()
