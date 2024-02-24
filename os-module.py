import os
import subprocess

class OS:
    def __init__(self):
        pass

    def view_files(self):
        """View files in the OS directory."""
        files = os.listdir('.')
        print("Files in the OS directory:")
        for file in files:
            print(file)

    def open_file(self, filename):
        """Open a specific file."""
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                print(f"Contents of '{filename}':")
                print(file.read())
        else:
            print(f"Error: File '{filename}' does not exist.")

    def list_processes(self):
        """List running processes."""
        print("Running processes:")
        for proc in psutil.process_iter():
            try:
                # Fetch process details
                pinfo = proc.as_dict(attrs=['pid', 'name'])
                print(pinfo)
            except psutil.NoSuchProcess:
                pass

    def execute_process(self, command):
        """Execute a specific process."""
        try:
            subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError:
            print(f"Error: Failed to execute command '{command}'")
