# Kickstart Github Project
## Category
Automation
## Description
A script that automates the steps of creating a new project on git and github
## File structure
You will need a folder that hosts your projects with `kickstart_project.py` saved inside
```
Projects-Folder
|_kickstart_project.py
```
## Setup
After placing the Python script in your folder run the following command for Linux:
`chmod +x kickstart_project.py`
This will grant the system access to the file so that you can run it from the bash shell.
## Execution
Open your shell, `cd` into your `Projects` folder where the Python script is saved and type `./kickstart_project.py`. This will launch the Python script that will ask you:
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
## Note
The Python script starts with `#! /usr/bin/env python3` which works in Linux. You may need to modify both the filepath and the `python` command depending on your Operating System.