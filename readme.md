# Kivy Pong Example Application

Example game application made using the Kivy documentation with some additions and notes.

## Summary

This project was derrived from the sample game application provided via the Kivy documentation (see Credits and Resources). It has been further expanded upon and annotated for educational purposes.

## Getting Started - Development

*NOTE*: This application was developed on a Windows machine using Python version 3.8.2, however, any sufficiently recent version of Python 3 that is capable of installing/running Kivy should be capable of running this application. Additionally, this project includes a `requirements.txt` file that utilizes packages unneccessary to execute the aplication itself (e.g. flake8 is used for linting but not required to run the game).

### Prerequisites

- Python 3 installed (and in the system path - e.g., you can run `python fily.py` commands from your preferred command line)
- This project is cloned/copied locally and you have a "shell"/"command prompt" in that directory (e.g. `user@machine:~kivy-paddle-ball-game# `)

### Steps

Assuming the prerequisites have been fulfilled:

1. Install the required Python packages

`PS C:\Users\username\workspace\kivy-paddle-ball-game> python -m pip install -r requirements.txt`

*Note: the only package required is Kivy (and its requirements), should you have issues using the requirments file, simply `python -m pip install kivy` to get the required version of the package (and its requirements) for your version of Python*

2. Execute the game

`PS C:\Users\username\workspace\kivy-paddle-ball-game> python paddle-ball-game`

## Credits and Resources

A list of resources that, in some way, aided my learning and thereby influenced the development of this project - these are in no particular order.

- [Pong Game Tutorial](https://kivy.org/doc/stable/tutorials/pong.html)
- [Usage of \_\_main\_\_.py in Python](https://www.geeksforgeeks.org/usage-of-__main__-py-in-python/)
- [Escaping special characters in markdown](http://tech.saigonist.com/b/code/escaping-special-characters-markdown.html)
