##
## EPITECH PROJECT, 2021
## 302separation
## File description:
## 302separation
##

import sys
import os
import re

def createFriends(file):
    com = []

    for i in file:
        reg = re.compile("^(\w+|\w* \w*) is friends with (\w+|\w* \w*)$")
        res = reg.search(i)
        com.append((res.group(1), res.group(2)))
    return com
        
def getFile(name):
    file = []

    f = open(name, 'r')
    file = f.read()
    file = file.split('\n')        
    return file

def checkArgs(name):
    try:
        open(name, 'r')
    except:
        print("Could not open file!")
        return 2
    if os.stat(name).st_size == 0:
        print('Error: File is empty')
        exit(84)

def checkFile(name): 
    file = getFile(name)
    comb = createFriends(file)

def help():
    print("USAGE\n\t./302separation file [n | p1 p2]\n")
    print("DESCRIPTION\n\tfile\tfile that contains the list of Facebook connections")
    print("\tn\tmaximum length of the paths")
    print("\tpi\tname of someone in the file")

def main():
    if len(sys.argv) == 2 and sys.argv[1] == "-h":
        help()
        exit(84)
    if len(sys.argv) != 2:
        help()
        exit(84)
    name = sys.argv[1]
    if checkArgs(name) == 2:
        exit(84)
    checkFile(name)

if __name__ == '__main__':
    main()