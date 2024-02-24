import getpass
import time

def authenticate(username, password):
    with open('credentials.txt', 'r') as file:
        for line in file:
            stored_username, stored_password = line.strip().split(',')
            if username == stored_username and password == stored_password:
                return True
    return False

def sign_up():
    username = input("Enter a new username: ")
    password = getpass.getpass("Enter a new password: ")
    with open('credentials.txt', 'a') as file:
        file.write(f"{username},{password}\n")
    print("Sign up successful!")

def generate_os_link(username, password):
    # Replace 'github_pages_site_link' with the actual link to your GitHub Pages site
    github_pages_site_link = 'https://Hank0670devdev.github.io/'
    os_link = f"{github_pages_site_link}usr?={username}&pass?={password}"
    return os_link

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
                os_link = generate_os_link(username, password)
                print("Here is the link to the OS:")
                print(os_link)
                break
            else:
                print("Invalid username or password.")
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
    time.sleep(50000)
