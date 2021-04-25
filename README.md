# Starcounter
Starcounter is a server application which lists one user's repositories and counts total amount of the stars that he/she has earned.
The program has been written in Python 3.8 and is based on Django framework.
## How to start the application
The easiest way to run Starcounter is to:
- clone this repository
- open terminal/powershell and navigate to the folder where docker-compose.yml is stored
- type ``` docker-compose up ``` (for windows) or ``` sudo docker-compose up ``` (for linux)

There is an alternative, though. You can use virtual environment. For windows, advance with the following instructions (it is assumed that python 3.8 or higher is installed):
```
py -m pip install --user virtualenv
py -m venv env
.\env\Scripts\activate
```
Then, copy all the files from this repository and paste it in the newly created 'env' folder. Next:
```
py -m pip install requests
py -m pip install django
```
navigate to the folder where manage.py file is stored. Lastly, type:
```
python manage.py runserver
```
open the browser and paste the following link: http://127.0.0.1:8000/stars/fokamdk99/

For linux (it is assumed that python 3.8 or higher is installed):
```
python3 -m pip install --user virtualenv
python3 -m venv env
source env/bin/activate
```
Then, copy all the files from this repository and paste it in the newly created 'env' folder. Next:
```
python3 -m pip install requests
python3 -m pip install django
```
navigate to the folder where manage.py file is stored. Lastly, type:
```
python3 manage.py runserver
```
open the browser and paste the following link: http://127.0.0.1:8000/stars/fokamdk99/

## Testing
There has been prepared a suit of unit tests. To run them, navigate to the folder where manage.py file is stored and type (for windows):
```
python manage.py test
```
and for linux type:
```
python3 manage.py test
```

## Extension possibilities
There are number of possible features that may be added in the future. One issue is that version of the program from commit 2309430 uses so called "unauthenticated user" which is allowed to make only 60 requests per hour to github rest api. Authenticating the user will bump the limit rate to 5000 requests per hour. Another idea is to add methods that will allow to create an issue or enable adding reactions to issue comments.
