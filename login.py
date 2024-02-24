import getpass
import click  # Importing click for CLI commands

# Define your OS commands as Click commands
@click.group()
def os_cli():
    pass

@os_cli.command()
def files():
    """View files in the OS."""
    click.echo("Listing files in the OS:")
    # Add code here to list files in the OS directory

@os_cli.command()
def open_file():
    """Open a file."""
    filename = click.prompt("Enter the name of the file to open")
    # Add code here to open the specified file

@os_cli.command()
def processes():
    """View running processes."""
    click.echo("Listing running processes:")
    # Add code here to list running processes

@os_cli.command()
def execute_process():
    """Execute a process."""
    process_name = click.prompt("Enter the name of the process to execute")
    # Add code here to execute the specified process

@os_cli.command()
def logout():
    """Logout of the OS."""
    click.echo("Logging out...")
    # Add code here to logout

# Authenticate function remains the same

def sign_up():
    username = input("Enter a new username: ")
    password = getpass.getpass("Enter a new password: ")
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
                os_cli()  # Launch the OS CLI after successful login
                break  # Exit the loop after logout
            else:
                print("Invalid username or password.")
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
