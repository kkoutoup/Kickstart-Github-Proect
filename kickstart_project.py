import os, re
import subprocess as sub

# see list of projects
def see_project_list():
  print("=> Existing projects")
  # see a list of projects?
  see_projects = input("Do you want to see a list of projects? Y/N ").lower().strip()
  # list folders
  if see_projects == "y":
    # only want folder names not other files
    project_list = os.listdir(os.getcwd())
    pattern = re.compile(r'(\.\w+$)')
    filtered_projects = list(filter(lambda item: not pattern.search(item), project_list))
    if len(filtered_projects) != 0:
      counter = 1
      for project in filtered_projects:
        print("{}: {}".format(counter, project))
        counter += 1
    else:
      print("No projects found in this folder")

def get_project_name():
  print("=> Set project name")
  # ask the user
  user_input = input("What's the name of the project? (use spaces to separate words): ").strip()
  # ask user to confirm
  confirm = input('Please confirm project name is "{}" Y/N  '.format(user_input)).lower()
  answers = ["y", "n"]
  # repeat ask for confirmation
  while confirm == "n" or confirm not in answers:
    user_input = input("What's the name of the project? (use spaces to separate words): ").strip()
    confirm = input('Please confirm project name is "{}" Y/N  '.format(user_input)).lower()
  else:
    project_name = user_input.title().replace(" ", "-")
    return project_name

def initialize_project():
  # create project folder and add README.md with
  # project_name as h1
  project_name = get_project_name()
  os.mkdir(project_name)
  os.chdir(os.path.join(os.getcwd(), project_name))
  with open('README.md', "w") as readme:
    readme.write("# {}".format(project_name))
  # initialize repo and do first commit
  sub.run(['git', 'init'])
  sub.run(['git', 'add', '.'])
  sub.run(['git', 'commit', '-m', '"initial commit"'])