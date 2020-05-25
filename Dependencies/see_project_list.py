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
    exclude = ["share", "bin", "include", "lib", "lib64", "Dependencies"] # exclude venv and dependencies folders
    if len(filtered_projects) == 0 or sorted(filtered_projects) == sorted(exclude):
      print("No projects found in this folder")
    else:
      for project in filtered_projects:
        if project not in exclude:
          print(f"- {project}")