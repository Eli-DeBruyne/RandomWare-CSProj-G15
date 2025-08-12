# Ransomware detection software

Overview
This repository contains an academic project developed for a university cybersecurity course. The project focuses on studying the behavior of ransomware in a controlled, simulated environment and developing detection tools to identify and report suspicious activity in files.

Purpose
The goal is purely educational — to research ransomware characteristics and build software capable of detecting such threats, enhancing understanding of malware detection techniques.

Disclaimer
This project was created and tested in a safe, isolated environment for learning purposes only. It is not intended for malicious use.

## Contributors:
Abe Artus  
Elijah DeBruyne  
Zane Lesley

## To-Do
- [x] Hide file log file for virus 2 (zane)
- [x] Make a way to upload the log file for virus 2 with encryption to a different network(zane) 
- [] Detection/prescan software for virus 2 (zane)
- [] real-time detection (Hard, would require some sort of low-level kernel system)

Virus to do
- [X] Develop a simple in-directory encryption malware in Python
- [ ] Develop a virus that will go beyond its directory and change other files in Python
- [ ] Develop a similar virus to encrypt a directory in C 
- [ ] Develop a dir changing virus that will encrypt files in C

File scanner to-do
- [ ] Develop a program to detect basic encryption malware from a source file (.py)
- [ ] Detect the simple in directory encryption
- [ ] Detect malware in C
- [ ] Develop a way to detect ransomware inside of an executable c file EX: ./virus

## Virus 1:
This virus will encrypt all files in the directory it's attached too, it will print out the encryption key, but that's just in case we do something wrong...

## Virus 2:
This is a keylogger that will record the user's keystroke into a file called log.txt. It will then send this file to a different server (we are just using localhost) then will delete the original log file off the computer.
- for further information on code, here are some resources:
    1. [basics of logging](https://docs.python.org/3/howto/logging.html#logging-basic-tutorial://www.example.com)
    2. [basics of the keyboard monitoring](https://pynput.readthedocs.io/en/latest/keyboard.html#reference)
    3. [logging config](https://docs.python.org/3/library/logging.config.html)
    4. [CBC Encryption](https://pycryptodome.readthedocs.io/en/latest/src/cipher/classic.html#cbc-mode)
    5. [Socket](https://realpython.com/python-sockets/#background)

### Detection for Keylogger
Uses a Python AST to go through and look for specific keywords that are used from the keylogger Python file, to expand on this, you would continue to cover
all types of different keywords to do with keyboard monitoring and logging/writing things to a file
- for further information on code, here are some resources:
    1. [AST Documentation](https://docs.python.org/3/library/ast.html#)




## Dependencies:
- [pynput](https://pypi.org/project/pynput/)
- [pycryptodome](https://pypi.org/project/pycryptodome/)
