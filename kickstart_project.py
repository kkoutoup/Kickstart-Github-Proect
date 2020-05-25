#! /usr/bin/env python3
import os
import re
import sys
import subprocess as sub

# read imports from folder
sys.path.append('/home/kkoutoup/Projects/Kickstart-Github-Project/Dependencies')

from Dependencies.see_project_list import see_project_list
from Dependencies.project_name import set_project_name
from Dependencies.select_language import select_language, set_language_extension

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
  sub.run(['git', 'commit', '-m', '"Initial commit"'])

if __name__=="__main__":
  initialize_project()