 Award
#### Author: [Kelvinrono](https://github.com/kelvinrono)
## Description
This is an application that allows users to post their projects and also can view other people's projects
As a user of the web application you will be able to:
1. Register and sign up for the applications
2. A user can post his/her own project
3. A uder can also rate and review other people projects basing on different factors


## Setup and installations
* Clone Project to your machine
* Activate a virtual environment on terminal: `source virtual/bin/activate`
* Install all the requirements found in requirements file.
* On your terminal run `python3.8 manage.py runserver`
* Access the live site using the local host provided
## Getting started
### Prerequisites
* python3.8
* virtual environment
* pip
#### Clone the Repo and rename it to suit your needs.
```bash
git clone https://github.com/kelvinrono/api
```
#### Initialize git and add the remote repository
```bash
git init
```
```bash
git remote add origin <your-repository-url>
```
#### Create and activate the virtual environment
```bash
python3.8 -m venv virtual
```
```bash
source virtual/bin/activate
```
#### Install dependancies
Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`
#### Make and run migrations
```bash
python3.8 manage.py check
python manage.py makemigrations news
python3.8 manage.py sqlmigrate news 0001
python3.8 manage.py migrate
```
#### Run the app
```bash
python3.8 manage.py runserver
```
Open [localhost:8000](http://127.0.0.1:8000)
## Testing the Application
`python3.8 manager.py tests`
## Built With
* [Python3.6](https://docs.python.org/3/)
* Django
* Boostrap
* HTML
* CSS

### Licence
This project is under the  [MIT](LICENSE) licence