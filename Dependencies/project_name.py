# What shall we name the new project?
import os

def set_project_name():
  print("\n=> Select project name")
  # ask the user
  user_input = input("What's the name of the project? (use spaces to separate words): ").strip()
  # ask user to confirm
  confirm = input(f"Please confirm project name is {user_input.lower()} Y/N ")
  answers = ["y", "n"]
  # repeat ask for confirmation
  while confirm == "n" or confirm not in answers:
    user_input = input("What's the name of the project? (use spaces to separate words): ").strip()
    confirm = input(f"Please confirm project name is {user_input.lower()} Y/N ")
  # construct folder name based on user input
  project_name = user_input.title().replace(" ", "-")
  # check if path exists
  if os.path.exists(f"{os.getcwd()}/{project_name}"):
    print("Path either exists or project name is not valid. Please try again")
    return set_project_name()
  else:
    return project_name