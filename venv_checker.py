import os
import subprocess
import sys

# Base directories where virtual environments are located
venv_dirs = []

# Function to check Python version and libraries for a virtual environment
def check_venv_versions(venv_path):
    if sys.platform == 'win32':
        python_bin = os.path.join(venv_path, 'Scripts', 'python.exe')
        print("python_bin PATH FOUND: {}".format(python_bin))
    else:
        python_bin = os.path.join(venv_path, 'bin', 'python')

    if os.path.isfile(python_bin):
        try:
            # Check Python version
            version_output = subprocess.check_output([python_bin, '--version'], text=True)
            print(f"\nVirtual Environment: {venv_path}")
            print(f"Python Version: {version_output.strip()}")

            # Check installed libraries
            pip_list_output = subprocess.check_output([python_bin, '-m', 'pip', 'list'], text=True)
            print("Installed Libraries:")
            print(pip_list_output)
        except subprocess.CalledProcessError as e:
            print(f"Error checking virtual environment {venv_path}: {e}")
    else:
        print(f"No Python binary found in {venv_path}")


# Function to check versions of specific libraries input by user
def check_venv_library_versions(venv_path, libraries):
    return print("check versions of libraries installed in a venv")
    
# Function to activate a specific venv
def activate_venv(venv_path):
    return print("activate venv")

# Function to deactivate a specific venv
def deactivate_venv(venv_path):
    return print("deactivate venv")

# Function to delete a specific venv
def delete_venv(venv_path):
    return print("delete venv")

def get_drive_paths():
    paths = []
    print("Enter local venv paths (press Enter without input when done):")
    while True:
        # Ask the user to input a path
        path = input("Enter path: ")
        path.replace("\\", "/")

        # Check if the user pressed Enter without input
        if path == "":
            break
        
        # Optionally, you can validate if the path exists before adding it
        # Uncomment the following lines if you want to check for valid paths
        if os.path.exists(path) and path not in paths:
            paths.append(path)
        else:
            print(f"Path does not exist or already added: {path}")
    return paths

# If running tool for the first time and paths are empty
# TODO: Implement local storage or memory, so that a user only needs to this once during startup
if not venv_dirs:
    # Get venv paths from user
    venv_dirs = get_drive_paths()

# If no paths were provided
if not venv_dirs:
    print("No paths were entered.")

for base_dir in venv_dirs:
    print("BASE DIR IS: {}".format(base_dir))
    check_venv_versions(os.path.join(base_dir))