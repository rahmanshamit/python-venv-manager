import os
import subprocess
import sys
import json

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

# Saves user input virtual envirnment paths to local json file
def save_paths_to_json():
    paths = []
    print("Enter local drive paths. When you're done, type 'y' and press Enter.")
    
    while True:
        # Ask the user for a path
        path = input("Enter path (or 'y' to finish): ")
        
        if path.lower() == 'y':  # Check if user wants to finish input
            break
        
        # Optionally, validate if the path exists on the system
        if path != "":
            if os.path.exists(path) and path not in paths:
                paths.append(path)
            else:
                print(f"Warning: Path does not exist or already added: {path}")
        else:
            print(f"Warning: Cannot add empty path")
        
    # Save the paths to paths.json
    with open('paths.json', 'w') as json_file:
        json.dump(paths, json_file, indent=4)
    print("Paths saved to 'paths.json'.")

def get_drive_paths():
    if os.path.exists('paths.json'):
        with open('paths.json', 'r') as json_file:
            paths = json.load(json_file)
            print("Loaded paths from 'paths.json':")
            return paths

# STARTS FROM HERE
# If no paths json file, get paths from Json
if not os.path.exists('paths.json'):
    save_paths_to_json()

# Get venv paths from user
venv_dirs = get_drive_paths()

# If no paths were provided
if not venv_dirs:
    print("No paths were entered.")
else:
    for base_dir in venv_dirs:
        check_venv_versions(os.path.join(base_dir))