## Description

This repository contains example project files for testing the Android and IOS.

This project does not use BDD/Gherkin to describe tests. All test flow is managed through files with test functions located in the ```./tests ``` directory.

The project uses Python version no lower than 3.11.2.

## Virtual environment management

> ```pip install virtualenv```.


To initially prepare the virtual environment before use, you must use the command:

>```virtualenv venv```

To activate the virtual environment, use the command:
>```source venv/bin/activate```

To exit the virtual environment, use the command:
>```deactivate```

## Run test

> Please note: to be able to publish a report, the allure2 library, version no lower than 2.24.0, must be installed on the local system and available in $PATH.\
Installation instructions can be found in [official documentation](https://docs.qameta.io/allure-report/#_installing_a_commandline).

## Run test android

>```pytest -s -v functional/android./tests./test_android.py```


To run tests, you need to call pytest specifying the directory to save the report files, and then call allure to generate and provide the report:

>```pytest --alluredir="./reports"```

