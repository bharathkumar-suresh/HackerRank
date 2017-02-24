#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sbhar
#
# Created:     09/02/2017
# Copyright:   (c) sbhar 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def convertListToString(list1):
    return "".join(str(c) for c in list1)

def reverseSentence(str1):
    tokens=str1.split(" ")
    output=convertListToString(list(reversed(tokens[0])))
    for each in tokens[1:]:
        output=output+" "+convertListToString(list(reversed(each)))
    return output

def main():
    print reverseSentence("A abc  xyz")

if __name__ == '__main__':
    main()
