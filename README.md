# gyst
Gyst is an open-source web app for stress-free Django Girls workshop planning

## Project Set Up
* Clone this repo
* Go to the project directory: ```cd  gyst```
* Create a virtual environment: ```python3 -m venv ve --prompt="gyst"```
  * Use whatever prompt you like
* Activate the virtual environment: ```. ve/bin/activate ```
* Install the requirements: ```pip install -r requirements.txt```

## Get started 
* Activate the virtual environment: ```. ve/bin/activate```
* Get the Google Cloud service account credentials file from one of the admins 
and place it under the root directory of the project
* In the console enter ```export GOOGLE_APPLICATION_CREDENTIALS='./<file_name>'```
* You can check the credentials export worked with ```printenv GOOGLE_APPLICATION_CREDENTIALS```
* Start the server ```python manage.py runserver```

## Useful URLs 
* Admin ```http://localhost:8000/admin```
* Photo Upload page ```http://localhost:8000/photos/upload```
* Photo Gallery page ```http://localhost:8000/photos/gallery```

## API 
* Photos list: ```http://localhost:8000/api/v1/photos```
* Photos detail: ```http://localhost:8000/api/v1/photos/<pk>```

## Run tests 
* Running ```pytest --cov=.``` from the root directory will run all tests and output a coverage report to the terminal. 
* Running ```pytest --cov=. --cov-report html``` will create an interactive html coverage report in the root directory. Open the ```index.html``` file in the ```htmlcov``` directory to browse files that are in need of coverage. You'll want to delete the ```htmlcov``` directory between test runs. 
