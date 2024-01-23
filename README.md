# Automate event dates 

## Purpose

This app is a personal project to help automate event created on [squarespace.com](https://www.squarespace.com/). Currently,
SquareSpace does not support creation of recurring events, this app aims to close that gap.

## Table of Contents
- [Tech Stack](#TechStack)
- [Requirements](#Requirements)
- [Getting Started](#Getting-started)

## TechStack
This app runs on Python3 on uses Selenium.py. Dependencies are managed bu pip and pipenv.

## Requirements 
To run this project you will need:
- [Python3](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/cli/pip_download/)
- [pipenv](https://pipenv.pypa.io/en/latest/)

## Getting started
### Run Locally
clone the project
```
https://github.com/aye-ron98/eventDateAutomation.git
```
Go to project directory
```commandline
cd eventDateAutomation
```
Start the virtual enviornemnt
```commandline
pipenv shell
```
Install Dependencies
```commandline
pipenv install 
```
Update Dependencies 
```commandline
pipenv update
```
Run the project
```commandline
pipenv run python main.py
```

### Configuring Pycharm 
After setting up the project, pycharm will continue to ask for you to install dependencies. This is because you must
point pycharm to the virtual enviornment created. 

Steps to configuring pycharm to point to a local enviornment may be found
[here](https://www.jetbrains.com/help/pycharm/pipenv.html#pipenv-existing-project).

#### Notes
1. You will need the location of your pipenv executable, assuming you have added it to your system paths get it by
running the following in a command line. 
```commandline
where pipenv
```
2. Once you have added the interpreter, pycharm should automatically switch to it, if it does not you will need to do 
it manually by clicking *interpreter > Show all...*.
