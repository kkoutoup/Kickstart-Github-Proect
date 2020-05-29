# Kickstart Github Project
## Category
Automation
## Description
A script that automates the steps of creating a new project on git and github.
## File structure
You will need a folder that hosts your projects with `kickstart_project.py` saved inside
```
Projects-Folder
|_Dependencies
    |_github_init.py
    |_project_name.py
    |_see_project_list.py
    |_select_language.py
|_kickstart_project.py
```
## Setup
1. Copy/clone the `Dependencies` folder and `kickstart_project.py` to the folder that contains your projects. See the diagram aboard for an example.
2. Run `chmod +x kickstart_project.py` in your terminal (Linux) to make the python script executable. Essentially, this command grants the system access to the file/changes file rights.
3. Depending on your operating system you may need to modify `#! /usr/bin/env python3` at the beginning of `kickstart_project.py`. This line tells bash where to look for the python interpreter to execute the script. Take a look at this [stackoveflow answer](https://stackoverflow.com/questions/7670303/purpose-of-usr-bin-python3) for more details.
4. Set the environment variables (Linux)
    - open your terminal and `cd` to your root directory
    - go to your bash profile with `nano` editor with `nano ~/.bash_profile`
    - type `export PYTHONPATH="path/to/dependencies/folder"` (i.e. `"home/username/Projects/Kickstart-Github-Project/Dependencies"`)
    - save and exit
This will allow the script to read from the `Dependencies` folder if it was an imported module.
## Execution
Open your shell, `cd` into your `Projects-folder` folder where the Python script is saved and type `./kickstart_project.py`. This will launch the Python script that will ask you:
1. If you want to see a list the list of current folders/projects in the same location
2. What language you'll be scripting in
3. To confirm the name of your project

Next the script will use your input to:
1. Create a new folder for your project named in UpperCamelCase with dashes (-) in between words
2. Initialize it as a git repository
3. Create a REAMDE.md file  with the project name as an `h1`
## Dependencies
Built with Python and:
- [selenium](https://selenium-python.readthedocs.io/index.html)
- os
- re
- subprocess