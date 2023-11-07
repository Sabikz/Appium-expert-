## 
Virtual environment management

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

>```pytest -s -v functional/android./tests./test_android.py```


To run tests, you need to call pytest specifying the directory to save the report files, and then call allure to generate and provide the report:

>```pytest --alluredir=allure-results ; allure serve allure-results```

If you need to visualize test execution, you must use the --headed parameter to render the browser and the --slowmo N (ms) parameter to set the required delay between steps. 

>```pytest --alluredir=allure-results --headed --slowmo 200 ; allure serve allure-results```
