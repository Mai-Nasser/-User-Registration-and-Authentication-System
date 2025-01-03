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
