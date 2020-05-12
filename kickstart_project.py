import os, re
import subprocess as sub

# see list of projects
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
    if len(filtered_projects) == 0:
      print("No projects found in this folder")
    else:
      for index, project in enumerate(filtered_projects, start=1):
        print(f"{index}: {project}")

def get_project_name():
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
    print("Path either exists or path name is not valid. Please try again")
    return get_project_name()
  else:
    return project_name

def select_language():
  print("\n=> Select language")
  languages = ["Python", "Ruby", "Javascript", "None"]
  for index, language in enumerate(languages, start=1):
    print(f'{index}: {language}')
  user_input = int(input("What language will you be scripting in? Select index ").strip())
  if user_input <= len(languages):
    print(f"You selected {languages[user_input - 1]}")
    return languages[user_input - 1]
  else:
    print(f"Your list doesn\'t contain as many languages (max = {len(languages)})")
    return select_language()

def initialize_project():
  # create project folder and add README.md with
  # project_name as h1
  project_name = get_project_name()
  os.mkdir(project_name)
  os.chdir(os.path.join(os.getcwd(), project_name))
  with open('README.md', "w") as readme:
    readme.write(f"# {project_name}")
  # initialize repo and do first commit
  sub.run(['git', 'init'])
  sub.run(['git', 'add', '.'])
  sub.run(['git', 'commit', '-m', '"initial commit"'])
