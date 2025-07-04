# <p align="center">Unittests and Integration Tests</p>

- [Learning Objectives](#Learning_Objectives)
- [Requirements](#requirements)
- [Mandatory Tasks](#Mandatory_Tasks)

Unit testing is the process of testing that a particular function returns expected results for different set of inputs. A unit test is supposed to test standard inputs and corner cases. A unit test should only test the logic defined inside the tested function. Most calls to additional functions should be mocked, especially if they make network or database calls.

The goal of a unit test is to answer the question: if everything defined outside this function works as expected, does this function work as expected?

Integration tests aim to test a code path end-to-end. In general, only low level functions that make external calls such as HTTP requests, file I/O, database I/O, etc. are mocked.

Integration tests will test interactions between every part of your code.

Execute your tests with

`$ python -m unittest path/to/test_file.py`


## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- The difference between unit and integration tests.
- Common testing patterns such as mocking, parametrizations and fixtures


## Requirements

### Python Scripts

- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.9)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` (version 2.5)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- All your functions and coroutines must be type-annotated.

## Mandatory tasks

### Task 0. Parameterize a unit test
### Task 1. Parameterize a unit test
### Task 2. Mock HTTP calls
### Task 3. Parameterize and patch
### Task 4. Parameterize and patch as decorators
### Task 5. Mocking a property
### Task 6. More patching
### Task 7. Parameterize
### Task 8. Integration test: fixtures