# <p align="center">Session authentication</p>

- [Learning Objectives](#Learning_Objectives)
- [Requirements](#requirements)
- [Mandatory Tasks](#Mandatory_Tasks)

## Learning Objectives

Background Context

In this project, you will implement a Session Authentication. You are not allowed to install any other module.

In the industry, you should not implement your own Session authentication system and use a module or framework that doing it for you (like in Python-Flask: Flask-HTTPAuth). Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing.

- What authentication means
- What session authentication means
- What Cookies are
- How to send Cookies
- How to parse Cookies

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

## Mandatory tasks


### Task 0. Et moi et moi et moi!
### Task 1. Empty session
### Task 2. Create a session
### Task 3. User ID for Session ID
### Task 4. Session cookie
### Task 5. Before request
### Task 6. Use Session ID for identifying a User
### Task 7. New view for Session Authentication
### Task 8. Logout