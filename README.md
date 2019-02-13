# my_curr_converter

### Installation

The application requires Python 3 to run.
Install python 3 from https://realpython.com/installing-python/


virtual environment is a part of standard library for python3. 


Follow the installation steps as mentioned below,
```sh
$ python3.6 -m venv <NAME_OF_THE_ENVIRONMENT> 
$ source <NAME_OF_THE_ENVIRONMENT>/bin/activate
```
Above mentioned commands create a virtual-env named <NAME_OF_THE_ENVIRONMENT> (This is a custom name). Second command activates the virtual env. Virtual environment creates a isolated environment for all the package installation.

Install all the packages listed in requirements.txt. Follow the steps below,
```sh
$ pip install -r requirements.txt
```

Although the app does not interact with the database you can run all the migrations as follows,
```sh
$ python manage.py migrate
```

The app needs a active internet connection to work as it interacts with the online APIs.

### Starting the application
The application can be started by executing the command below. The app starts at http://localhost:8000

```sh
$ python manage.py runserver
```
