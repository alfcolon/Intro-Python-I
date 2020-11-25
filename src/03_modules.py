"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE

systemArguments = sys.argv

for argument in systemArguments:
    print(argument)

# Print out the OS platform you're using:
systemPlatform = sys.platform
print(systemPlatform)

# Print out the version of Python you're using:
pythonVersion = sys.version
print(pythonVersion)

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
currentProcessID = os.getpid()
print(currentProcessID)

# Print the current working directory (cwd):
# YOUR CODE HERE
currentWorkingDirectory = os.getcwd()
print("The current working directory is " + currentWorkingDirectory)

# Print out your machine's login name
import getpass
username = getpass.getuser()
print(username)
