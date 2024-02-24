import getpass

def authenticate(username, password):
    with open('credentials.txt', 'r') as file:
        for line in file:
            stored_username, stored_password = line.strip().split(',')
            if username == stored_username and password == stored_password:
                return True
    return False

def main():
    username = input("username? ")
    print('Logging in with: <'+username+'>')
    password = getpass.getpass("password: ")
    
    if authenticate(username, password):
        print("Login successful!")
    else:
        print("Invalid username or password.")
        main()
if __name__ == "__main__":
    main()
