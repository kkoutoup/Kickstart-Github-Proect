#! /usr/bin/env python3
import os, re
import subprocess as sub

# Local dependencies
from project_list import see_project_list
from project_name import set_project_name
from select_language import select_language, set_language_extension

def initialize_project():
  # show list of existing projects
  see_project_list()
  # create project folder and coding file
  project_name = set_project_name()
  os.mkdir(project_name)
  os.chdir(os.path.join(os.getcwd(), project_name))
  with open('README.md', "w") as readme, open(f"start{set_language_extension()}", "w") as code_file:
    readme.write(f"# {project_name}")
    code_file.write("Happy times")
  # initialize repo and do first commit
  sub.run(['git', 'init'])
  sub.run(['git', 'add', '.'])
  sub.run(['git', 'commit', '-m', '"initial commit"'])

if __name__=="__main__":
  initialize_project()