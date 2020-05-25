# See a list of existing projects in the folder
import os
import re
def see_project_list():
  print("=> See existing projects")
  # see a list of projects?
  see_projects = input("Do you want to see a list of projects? Y/N ").lower().strip()
  # list folders
  if see_projects == "y":
    # only want folder names not other files
    project_list = os.listdir(os.getcwd())
    pattern = re.compile(r'(\.\w+$)')
    filtered_projects = list(filter(lambda item: not pattern.search(item), project_list))
    # check folders are present
    if len(filtered_projects) == 0:
      print("No projects found in this folder")
    else:
      for index, project in enumerate(filtered_projects, start = 1):
        if project == "__pycache__" or "Dependencies":
          print("No projects found in this folder")
        else:
          print(f"{index}: {project}")