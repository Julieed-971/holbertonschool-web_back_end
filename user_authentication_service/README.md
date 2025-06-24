# <p align="center">User authentication service</p>

- [Learning Objectives](#Learning_Objectives)
- [Requirements](#requirements)
- [Mandatory Tasks](#Mandatory_Tasks)

## Learning Objectives

*In the industry, you should not implement your own authentication system and use a module or framework that doing it for you (like in Python-Flask: Flask-User). Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing.*

- How to declare API routes in a Flask app
- How to get and set cookies
- How to retrieve request form data
- How to return various HTTP status codes


## Requirements

### Python Scripts

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.9)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` (version 2.5)
- You should use `SQLAlchemy`
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- All your functions should be type annotated
- The flask app should only interact with `Auth` and never with `DB` directly.
- Only public methods of `Auth` and `DB` should be used outside these classes

## Setup

You will need to install bcrypt

```
pip3 install bcrypt
```

## Mandatory tasks

### Task 0. User model
### Task 1. create user
### Task 2. Find user
### Task 3. update user
### Task 4. Hash password
### Task 5. Register user
### Task 6. Basic Flask app
### Task 7. Register user
### Task 8. Credentials validation
### Task 9. Generate UUIDs
### Task 10. Get session ID
### Task 11. Log in
### Task 12. Find user by session ID
### Task 13. Destroy session
### Task 14. Log out
### Task 15. User profile
### Task 16. Generate reset password token
### Task 17. Get reset password token
### Task 18. Update password
### Task 19. Update password end-point