"""
- This file could be empty, but it is required to make Python treat the directories as containing packages
- The __init__.py file can be left empty or it can contain initialization code for the package.
- This is also need as a Python convention to make the directory a package as an independent module, that can provide that 
the class and methods included on each independent file inside of this directed can be used in other files of the project as an 'import' utility
- Also for the test orgaization in different directories, each directory can have its own __init__.py file, this can allows to execute 
pytest to run the tests in each directory, as an example, if you have a directory called 'smoke_test' and another directory called 'regression_test':
   
    - smoke_test
        - __init__.py
        - login.py
        - search_product.py
    - regression_test
        - __init__.py
        - regression_login.py
        - regression_search_product.py
        - 

Command to run the tests:

Option 1: Run all tests in the directory

'pytest -m <test_directory_name>'

Example:

'pytest -m smoke_test'
'pytest -m regression_test'


# Using allure to generate a  HTML report

'pytest -m smoke_test --alluredir=allure-results'
'pytest -m regression_test --alluredir=allure-results'



Option 2: Run specific test

'pytest -m smoke_test/login.py'
'pytest -m regression_test/regression_login.py'

"""