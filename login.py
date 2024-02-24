import getpass

def authenticate(username, password):
    with open('credentials.txt', 'r') as file:
        for line in file:
            stored_username, stored_password = line.strip().split(',')
            if username == stored_username and password == stored_password:
                return True
    return False

def sign_up():
    username = input("username? ")
    password = getpass.getpass("password: ")
    with open('credentials.txt', 'a') as file:
        file.write(f"{username},{password}\n")
    print("Sign up successful!")

def main():
    while True:
        print("<1> Sign Up!")
        print("<2> Log In")
        choice = input(">>> ")
        if choice == "1":
            sign_up()
        elif choice == "2":
            username = input("username? ")
            print('Logging in with: <'+username+'>')
            password = getpass.getpass("password: ")
            if authenticate(username, password):
                print("Login successful!")
                break
            else:
                print("Invalid username or password.")
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
