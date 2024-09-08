import os
import subprocess
import sys

# Define the base directories where your virtual environments are located
venv_dirs = [
    # local drive placeholders for testing during development process
    # TODO: Take base directories from user
    'D:/Code/python_venv_checker/venv1/myvenv1', 
    'D:/Code/python_venv_checker/venv2/myvenv2'
]

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


for base_dir in venv_dirs:
    print("BASE DIR IS: {}".format(base_dir))
    check_venv_versions(os.path.join(base_dir))