"""
Create a Django project, in 
a virtualenv with psycopg2 installed. 

"""
from subprocess import call
from os import chdir, mkdir


""" Prompt the user for a project name, then
Run the django-admin startproject cmd  """
def start_project():
    
    proj_name = input("Enter a project name: ")

    # Throw an exception is proj_name is null
    if not proj_name:
        raise Exception('Project name cannot be null!')

    mkdir(proj_name)
    chdir(proj_name)

    """Create virtualenv w/ Pipenv, and install packages"""
    # Make sure pip is up-to-date
    call('python -m pip install --upgrade pip')
    # Install pipenv, if it is not already installed
    call('pip install pipenv')
    call('pipenv install django')
    call('pipenv install psycopg2')
    call('django-admin.exe startproject ' + proj_name)
    
    open('README.md', 'a')


"""
Initialize empty git repo, then add + commit all project files
"""
def git():

    call('git init')
    call('git add -A')
    call('git commit -m "initial commit" ')


# Add an app to the project
def create_app():

    app_name = input("Enter a name for your first Django project app: ")
    call('django-admin.exe startapp ' + app_name)

    # Throw an exception is app_name is null
    if not app_name:
        raise Exception('App name cannot be null!')


def main():

    start_project()
    create_app()
    git()
        

main()