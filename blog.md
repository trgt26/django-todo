# Django Todo App

Hi! today I will guide you to create a simple todo app using django.

Before we start make sure you have python installed in your system.

Now, we will start by creating a virtual environment. It will keep our dependencies isolated. So, open up the command prompt and execute the following command.

```
python -m venv venv
```
This will create a virtual environment named `venv`.


Then, by running the following command, we will activate our virtual environment.
```
source venv/bin/activate 
```

Now, to install django in `venv` run this command.

```
pip install django
```
## Creating project and app

Now, we will create django project, for that, execute the following command.

```
django-admin startproject todo_site
```
This will create some files and directories. Now, we will go to the directory named `todo_site`.

Here, we will create an app by executing the following command.

```
python manage.py startapp todo
```
This will create an app named `todo` in the the current directory.

## Creating Model

Before we write model, we include our current app to the `settings.py` file. for that open, `todo_site/settings.py` file and add `todo` to `INSTALLED_APPS` list. The list will look like the following,

```py
INSTALLED_APPS = [
    'todo',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

## Writing Templates

## Defining URLs




