# Entry_Management

## How to use it
Install python 3.x from https://www.python.org/downloads/ to your computer if it not there.

## To install and run project locally

- Clone the repo in your local machine
- Go into project directory ie Entry_Management folder
- Make new virtual environment 
``` 
$python -m venv myvenv9 
$myvenv9\Scripts\activate  #for windows
$source myvenv9/bin/activate  #for ubuntu
(myvenv9)$python -m pip install --upgrade pip
(myvenv9)$pip install -r requirements.txt
```
-For email facility enter a google email id and password in entman/settings.py at end
```
EMAIL_HOST_USER = 'your@gmail.com'
EMAIL_HOST_PASSWORD = 'passwordofgmailaccount'
```
-For sms facility you have to make a account on https://www.fast2sms.com/ and get the API key and edit it in bform/views.py in visitors_new function headers.
```
$python manage.py runserver
```
Open http://127.0.0.1:8000/host/new/ and test it.
