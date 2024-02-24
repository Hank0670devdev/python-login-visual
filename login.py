import getpass
import os
import subprocess

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

def view_files():
    """View files in the OS directory."""
    files = os.listdir('.')
    print("Files in the OS directory:")
    for file in files:
        print(file)

def open_file(filename):
    """Open a specific file."""
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            print(f"Contents of '{filename}':")
            print(file.read())
    else:
        print(f"Error: File '{filename}' does not exist.")

def list_processes():
    """List running processes."""
    print("Running processes:")
    for proc in psutil.process_iter():
        try:
            # Fetch process details
            pinfo = proc.as_dict(attrs=['pid', 'name'])
            print(pinfo)
        except psutil.NoSuchProcess:
            pass

def execute_process(command):
    """Execute a specific process."""
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError:
        print(f"Error: Failed to execute command '{command}'")

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
                while True:
                    print("\n<1> View Files")
                    print("<2> Open File")
                    print("<3> List Processes")
                    print("<4> Execute Process")
                    print("<5> Logout")
                    choice = input(">>> ")
                    if choice == "1":
                        view_files()
                    elif choice == "2":
                        filename = input("Enter the name of the file to open: ")
                        open_file(filename)
                    elif choice == "3":
                        list_processes()
                    elif choice == "4":
                        command = input("Enter the command to execute: ")
                        execute_process(command)
                    elif choice == "5":
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice. Please choose again.")
                break
            else:
                print("Invalid username or password.")
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
