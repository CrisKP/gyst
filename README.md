# gyst
Gyst is an open-source web app for stress-free Django Girls workshop planning

## Get started
* Clone this repo
* Go to the project directory: ```cd  gyst```
* Create a virtual environment: ```python3 -m venv ve --prompt="gyst"```
  * Use whatever prompt you like
* Activate the virtual environment: ```. ve/bin/activate ```
* Install the requirements: ```pip install -r requirements.txt```

## Run tests 
* Running ```pytest --cov=.``` from the root directory will run all tests and output a coverage report to the terminal. 
* Running ```pytest --cov=. --cov-report html``` will create an interactive html coverage report in the root directory. Open the ```index.html``` file in the ```htmlcov``` directory to browse files that are in need of coverage. You'll want to delete the ```htmlcov``` directory between test runs. 
