#!/usr/bin/python
import sys
import os

# List the contents of the directory passed as
# the first argument after the exctuable name.
# If no argument, list '/' (root).
if len(sys.argv) < 2:
    dirToList='/'
else:
    dirToList=(sys.argv[1])

for i in os.listdir(dirToList):
    print os.path.join(dirToList,i)
