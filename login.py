from os_module import OS  # Importing the OS class from the os_module module

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
                os_instance = OS()  # Creating an instance of the OS class
                while True:
                    print("\n<1> View Files")
                    print("<2> Open File")
                    print("<3> List Processes")
                    print("<4> Execute Process")
                    print("<5> Logout")
                    choice = input(">>> ")
                    if choice == "1":
                        os_instance.view_files()
                    elif choice == "2":
                        filename = input("Enter the name of the file to open: ")
                        os_instance.open_file(filename)
                    elif choice == "3":
                        os_instance.list_processes()
                    elif choice == "4":
                        command = input("Enter the command to execute: ")
                        os_instance.execute_process(command)
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
