import os
import json
import subprocess

# Function to check if paths.json exists
def check_json_exists():
    return os.path.exists('paths.json')

# Saves user input virtual envirnment paths to local json file
def start_save_paths_to_json():
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

# Function to load paths from paths.json
def load_paths_from_json():
    if check_json_exists():
        with open('paths.json', 'r') as json_file:
            return json.load(json_file)
    return []

# Function to save paths to paths.json
def save_paths_to_json(paths):
    with open('paths.json', 'w') as json_file:
        json.dump(paths, json_file, indent=4)

# Function to display the paths as a numbered list
def display_paths(paths):
    print("\nList of Virtual Environment Paths:")
    for i, path in enumerate(paths):
        print(f"{i + 1}. {path}")

# Function to show Python version and installed libraries for a specific path
def show_python_info(path):
    python_executable = os.path.join(path, 'Scripts', 'python.exe' if os.name == 'nt' else 'bin/python')
    if os.path.exists(python_executable):
        # Get Python version
        subprocess.run([python_executable, "--version"])
        # Get installed libraries
        subprocess.run([python_executable, "-m", "pip", "list"])
    else:
        print(f"No Python executable found in {path}")

# Option 1: Show Python version and installed libraries for all paths
def show_info_for_all_paths(paths):
    for path in paths:
        print(f"\nDetails for {path}:")
        show_python_info(path)

# Option 2: Show Python version and installed libraries for a specific path
def show_info_for_specific_path(paths):
    display_paths(paths)
    choice = int(input("\nSelect the number of the path you want to check: ")) - 1
    if 0 <= choice < len(paths):
        show_python_info(paths[choice])
    else:
        print("Invalid choice!")

# Option 3: Add new paths
def add_new_path(paths):
    new_path = input("Enter the new virtual environment path: ")
    if os.path.exists(new_path):
        paths.append(new_path)
        save_paths_to_json(paths)
        print(f"Path {new_path} added successfully.")
    else:
        print(f"Path {new_path} does not exist.")

# Option 4: Delete a path
def delete_path(paths):
    display_paths(paths)
    choice = int(input("\nSelect the number of the path you want to delete: ")) - 1
    if 0 <= choice < len(paths):
        deleted_path = paths.pop(choice)
        save_paths_to_json(paths)
        print(f"Path {deleted_path} deleted successfully.")
    else:
        print("Invalid choice!")

# Option 5: Activate a virtual environment in a new terminal
def activate_virtual_environment(paths):
    display_paths(paths)
    choice = int(input("\nSelect the number of the path you want to activate: ")) - 1
    if 0 <= choice < len(paths):
        env_path = paths[choice]
        activate_script = os.path.join(env_path, 'Scripts', 'activate.bat' if os.name == 'nt' else 'bin/activate')
        if os.path.exists(activate_script):
            # Open a new terminal and activate the virtual environment
            if os.name == 'nt':
                subprocess.run(['start', 'cmd', '/K', activate_script], shell=True)
            else:
                subprocess.run(['gnome-terminal', '--', 'bash', '-c', f'source {activate_script}; exec bash'])
        else:
            print(f"No activation script found in {env_path}")
    else:
        print("Invalid choice!")

# Main menu function
def main_menu():
    # STARTS FROM HERE
    # If no paths json file, get paths from Json
    if not os.path.exists('paths.json'):
        start_save_paths_to_json()

    paths = load_paths_from_json()

    while True:
        display_paths(paths)
        print("\nOptions:")
        print("1. Show Python version and installed libraries for all paths")
        print("2. Show Python version and installed libraries for a specific path")
        print("3. Add new path")
        print("4. Delete a path")
        print("5. Activate a virtual environment")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ")

        if choice == "1":
            show_info_for_all_paths(paths)
        elif choice == "2":
            show_info_for_specific_path(paths)
        elif choice == "3":
            add_new_path(paths)
        elif choice == "4":
            delete_path(paths)
        elif choice == "5":
            activate_virtual_environment(paths)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main_menu()
