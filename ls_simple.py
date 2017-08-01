#!/usr/bin/python
CONFIG='./ls_simple.cfg'

import sys
import os

def readConfigFile(path=None):
    # Default path
    if not path:
        path = './ls.cfg'
    try:
        fdCfg=open(path,'ru')
        newRoot=fdCfg.read().strip()
        fdCfg.close()
        return(newRoot)
    except Exception as err:
        sys.stderr.write(str(err) + '\n')
        sys.stderr.write('Cannot read config file contents.')
        return(None)


# Determine our root
rootDir=readConfigFile(CONFIG)
if not rootDir:
    sys.stderr.write('Cannot determine the root dir. Exiting.')
    sys.exit(1)

# List the contents of the directory passed as
# the first argument after the exctuable name.
# If no argument, list the root directroy contents
if len(sys.argv) < 2:
    sys.stdout.write(rootDir + '\n')
else:
    # The directroy requested is / then we still just print rootDir
    if sys.argv[1] == '/':
        sys.stdout.write(rootDir + '\n')
    else:
        # We really got a full path
        # Does it start with rootDir?
        if sys.argv[1].startswith(rootDir):
            dirToList=sys.argv[1]
        # Is it a path realtive to a rootDir?
        elif os.path.join('/',sys.argv[1]).startswith(rootDir):
            dirToList=os.path.join('/',sys.argv[1])
        # If none of the above, we cannot list
        else:
            sys.stderr.write('Cannot list ' + sys.argv[1] + '\n')
            sys.exit(1)

        # The actual directory listing
        try:
            for i in os.listdir(dirToList):
                print os.path.join(dirToList,i)

        except Exception as err:
            sys.stderr.write(str(err) + '\n')
            sys.stderr.write('Cannot list ' + dirToList + '\n')
            sys.exit(1)
