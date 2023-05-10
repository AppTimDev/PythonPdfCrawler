## Objectives
use python script to crawl the webpage to extract all the links and then download all the pdf files.

The demo link (https://apptimdev.bsite.net/Home/Pdf) in the main.py is used to provide a webpage for the python scripts to crawl. This link is hosted using the source codes in the [project repository](#demo-reference-source). This link may not work in the future. 

---

## Environment:
- Windows 10
- Python 3.11.3
- pip 23.1.2
- pipenv 2023.4.29

---

## Project Setup
### 1. Install Python 3.11
https://www.python.org/downloads/

### 2. Install pipenv
```sh
python -m pip install --upgrade pip
python -m pip install --upgrade pipenv
``` 

### 3. Install all the packages and initialize the virtual environment
```sh
pipenv install
```

### 4. Run the script main.py under the project folder
```sh
pipenv run python main.py
```

---

## pipenv 
### Create a virtual environment (python 3.11.3 installed)
```sh
pipenv --python 3.11
```

### Install all python packages or specific packages
```sh
pipenv install
pipenv install requests beautifulsoup4 html5lib
pipenv install pytest --dev
```

### Run the python script (not enter virtual environment)
```sh
pipenv run python main.py
```

### Activate the virtual environment
```sh
pipenv shell
```

### Uninstall python package
```sh
pipenv uninstall requests beautifulsoup4
pipenv uninstall beautifulsoup4
```

### List the package dependency graph
```sh
pipenv graph
```

## Some Features of pipenv, not list all
- Pipfile is used instead of requirements.txt
- You no longer need to use pip and virtualenv separately. They work together.

---

## Commands
### Check python version
```sh
python -V
```
### Check pip version
```sh
pip -V
```
### Check the version the package pipenv
```sh
pip show pipenv
```

### List all the installed package of python
```sh
pip list
```

### Locate pip and the Python interpreter
```sh
where pip
where python
where pipenv
```

and sometimes it may be important to find the path of python interpreter using in the pipenv environment
#### Output Python interpreter, pip, pipenv  information of pipenv environment
```sh
pipenv run pip -V
pipenv --py
pipenv --version
```

#### Output virtualenv information.
```sh
pipenv --venv
```

#### Remove the virtualenv.
```sh
pipenv  --rm  
```      
 
---

## Related Projects or References
### pipenv
- https://github.com/AppTimDev/PythonVenv

### Demo Reference Source 
Crawler Pdf Webpage
- https://github.com/AppTimDev/PdfCrawlerCoreMvc
