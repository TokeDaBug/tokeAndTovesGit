#!/usr/bin/env python3
import sys
# initializing options
optionA, optionB, optionNumber = None, None, None
filename = None

def usage(msg=None):
    # Print a message if there was something specific you want to the user. 
    if msg is not None:
        print(msg, "\n")
    print ("Usage: demooption.py [-a] [-b] [-c <integer>] <filename>")
    # Exit the program. We can not progress. Makes logic easier elsewhere.
    sys.exit(1)

while len(sys.argv) > 1:
    arg = sys.argv.pop(1)
    if arg == '-a':
        optionA = True
    elif arg == '-b':
        optionB = True
    elif arg == '-c':
        try:
            # There are possibility for failure here - no argument, not integer
            optionNumber = int(sys.argv.pop(1))
            if optionNumber < 1:
                raise ValueError
            
        except:
            usage()
        
            
    elif filename is None:
        filename = arg
    else:
        usage()

if filename is None:
    usage("Hey, you need a filename")
else:
    print("Using this file:", filename)
if optionA:
    print("OptionA reporting for duty")    
if optionB:
    print("OptionB is on the scene")    
if optionNumber is not None:
    with open(filename, "r") as infile:
        number_list = []

        for line in infile:
            collums = line.strip().split("\t")
            number_list.append(collums[(optionNumber - 1)])
            print(number_list)
if filename == arg:
     with open(filename, "r") as infile:
        number_list = []
        
        for line in infile:
            collums = line.strip().split("\t")
            N = len(collums) - 1
            number_list.append(collums[0:N])
            print(number_list)        

