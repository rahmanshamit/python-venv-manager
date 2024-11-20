# python-venv-manager
A Python tool to manage multiple virtual environments, including options to view Python versions, installed libraries, add or remove virtual environments, and activate them in a new terminal.

## Goal, Purpose and Why
Existing tools such as virtualenvwrapper, creates all virtual environments by default under the directory specified by the WORKON_HOME environment variable (usually ~/.virtualenvs).
To check the libraries and versions installed in each virtual environment, the developer also needs to either run 'pip list' individually, or
they have to individually check the site-packages folder.

The main purpose of this project is avoid individual manual checking, and to streamline and automate this process of managing multiple Python virtual environments.

I want to give the developer the freedom to create their venv folders wherever as they want, and rather than manually nagivate to each venv folder, 
only define the paths once during setup, and manage environments from the tool.

## Features
- **Add Virtual Environments**: Input paths to your virtual environments and save them to a `paths.json` file.
- **View Python Info**: View the Python version and installed libraries for all or specific virtual environments.
- **Activate Virtual Environments**: Open a new terminal and activate the selected virtual environment.
- **Manage Virtual Environments**: Add new paths, delete existing paths, or refresh the list.

## Getting Started
### 1. Run the Script
To use the tool, first run the Python script "python venv_manager.py". On the first run, you will be prompted to input the paths to your local virtual environments.

### 2. Input Virtual Environment Paths
The script will ask you to enter local drive paths for your virtual environments.

### 3. Main Menu Options
Once the paths are saved in the paths.json file, the tool will present a menu with several options:
1. Show Python version and installed libraries for all paths
2. Show Python version and installed libraries for a specific path
3. Add new path
4. Delete a path
5. Activate a virtual environment
6. Exit

### Requirements:
- Python 3.x
- Virtual environments (Paths should be valid)


## Python Virtual Environments - What and Why
A Python virtual environment is a self-contained directory that contains a specific version of Python and its libraries, independent of the system-wide Python installation. 
It allows you to create an isolated environment where you can install and manage dependencies for each project without affecting other projects or the global Python setup.
A developer may need to maintain multiple Python virtual environments, each with different versions of libraries for reasons such as:

### 1. **Project-Specific Dependencies**
- Project A might use **Django 2.2**, while Project B uses **Django 3.2**.
- One project may rely on **NumPy 1.18**, while another may need **NumPy 1.21** due to performance optimizations or new features.
By isolating dependencies in separate virtual environments, a developer ensures that each project runs with the exact versions it was built and tested with, preventing compatibility issues.

### 2. **Avoiding Dependency Conflicts**
Some libraries may have conflicting dependencies. For example:
- Project A may require **Pandas 1.x**, which in turn depends on a specific version of **matplotlib**.
- Project B may need a newer or older version of **Pandas**, which has different compatibility requirements.
By using virtual environments, developers can avoid conflicts between different projects that rely on incompatible versions of libraries.

### **3. Different Python Versions**
Sometimes, it's not just the libraries but also the Python version itself that differs between projects. Virtual environments allow a developer to create isolated environments with different versions of Python:
- Project A might run on **Python 3.7**, while Project B needs **Python 3.9**.
This helps test compatibility and ensure that each project uses the appropriate Python version without interfering with other projects.
