# IP Address Reachability Checker
Provide an IP address an the application rund the ping command for the given IP address thereby returning the result of the ping command

## Requirements 

Python 3.6+, python-pip

## Installation

First clone this repository.

    `$ git clone https://github.com/Yash151/resize-image.git`
    `$ cd resize-image`

Install necessary python packages

    `$ pip  install -r requirements.txt`

Run the application

    `$ python views.py`

To use the applciation for resizing your image, access the below url in your browser:

    http://localhost:5000

## Vulnerabilities

### Command Injection

    This exploits the insufficient security of sanitizing given input IP address. Due to this we are able to run multiple malicious commands by providing them in the given input area

#### Attack string on Windows machine

    `127.0.0.1"& password.txt"`

#### Attack string for any other OS

    `127.0.0.1"; cat /password.txt"`

### Cross-Site Scripting Attack (XSS)

    This exploit allows the attacker to run a malicious javascript code by injecting the script from the input area provided. This exploit is also possible due to the fact that there is no proper sanitization of user input.

#### Attack string for XSS

    `<script>alert('This is an XSS attack')</script>`


