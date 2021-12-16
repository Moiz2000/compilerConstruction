from regex import *
import json

file = "words.txt"

lineNo = 1    # line no in file
temp = ""     # store word
Qotation = False
qoutationCount = 0
addCount = 0
equalCount = 0
addFlag = False
equalFlag = False
minusFlag = False
minusCount = 0
multiplyFlag = False
divideFlag = False
moduloFlag = False
notFlag = False
lessthanFlag = False
greaterthanFlag = False
char = ""
AndCount = 0
AndFlag = False
orCount = 0
orFlag = False
dotFlag = False
dot = ""
dotTemp = ""
dotTemp1 = ""
scommentFlag = False
mcommentFlag = False
mcommentCount = 0

token_list = []

class Token:
    def __init__(self, word, word_class, line_no):
        self.word = word
        self.word_class = word_class
        self.line_no = line_no

def token_file_init():
    file = open("tokens.json", "w")
    file.write("")
    file.close()

def createToken(string):

    global token_list
    global temp
    global lineNo

    token = Token(temp, is_keyword(temp), lineNo)

    token_list.append(token)

    temp = ""

def token_file_update():
    
    global token_list
    token_dict = []

    for token in token_list:
        temp = json.dumps(token.__dict__)
        token_dict.append(temp)
    
    with open("tokens.json", "a") as tfile:
        json.dump(token_dict, tfile)
        
        



def word_analyzer(file):

    global lineNo
    global temp
    global Qotation
    global qoutationCount
    global addCount
    global equalCount
    global addFlag
    global equalFlag
    global minusCount
    global minusFlag
    global multiplyFlag
    global moduloFlag
    global divideFlag
    global notFlag
    global greaterthanFlag
    global lessthanFlag
    global char
    global AndCount
    global AndFlag
    global orCount
    global orFlag
    global dotFlag
    global dot
    global dotTemp
    global dotTemp1
    global scommentFlag
    global mcommentFlag
    global mcommentCount

    punctuator = [',', ';', '(', ')', '{', '}', '[', ']', ':', '?']

    with open(file, 'r') as files:  # open and close files
        print(files[0])
        for line in files:             # iterate through lines in file
            for char in line:          # iterate through character in a line

                # if new line character founded , print temp increase line no by 1 and reset char and temp
                if char == "\n" and Qotation == False and mcommentFlag == False:
                    if temp != "":
                        print(temp, lineNo)
                        createToken(temp)
                        char = ""
                        lineNo += 1
                        print(lineNo)
                    else:
                        scommentFlag = False
                        temp = ""
                        char = ""
                        lineNo += 1
                        print(lineNo)

                # if single comment hash is found
                if char == "#" and mcommentFlag == True:
                    pass
                elif char == "#" and Qotation == True:
                    pass
                elif char == '#':
                    if temp != '':
                        print(temp, lineNo)
                        createToken(temp)
                        temp = ''
                        char = ''
                    scommentFlag = True
                    char = ""
                # if multiple comment is found
                if char == "~" and scommentFlag == True:
                    char = ""
                elif char == "~" and Qotation == True:
                    pass 
                elif char == "~":
                    mcommentCount += 1
                    mcommentFlag = True
                    if temp != '' and mcommentCount == 1:
                        print(temp, lineNo)
                        createToken(temp)
                        temp = char
                        char = ''
                    elif mcommentCount == 2:
                        temp = ""
                        mcommentCount = 0
                        mcommentFlag = False
                        char = ""
                print(line.index(char))
                print(len(line)-1)
                print(files.index(line))
                print(len(files)-1)
                if mcommentFlag == True and mcommentCount == 1 and line.index(char) == len(line)-1 and files.index(line) == len(files)-1:
                    print(temp, lineNo)
                    createToken(temp)
                    temp = ""
                    char = ""
                    mcommentFlag = False
                    mcommentCount = 0
                               
                if char == " " and Qotation == True:
                    pass
                elif char == " " and scommentFlag == True:
                    char = ""
                elif char == " " and mcommentFlag == True:
                    pass
                elif char == " ":
                    if temp != "":
                        print(temp, lineNo)
                        createToken(temp)
                        char = ""
                    char = ""

                if char in punctuator and Qotation == True:
                    pass
                elif char in punctuator and scommentFlag == True:
                    char = ""
                elif char in punctuator and mcommentFlag == True:
                    pass
                elif char in punctuator:
                    if temp != "":
                        print(temp, lineNo)
                        createToken(temp)
                    print(char, lineNo)
                    char = ""

                if char == "\"" and scommentFlag == True:
                    char = ""
                elif char == "\"" and mcommentFlag == True:
                    pass
                elif char == "\"":
                    Qotation = True
                    qoutationCount += 1

                    if temp != "" and qoutationCount == 1:
                        print(temp, lineNo)
                        createToken(temp)

                    if char == "\"" and qoutationCount == 2:
                        qoutationCount = 0
                        Qotation = False
                        print(temp, lineNo)
                        createToken(temp)

                    char = ""
                elif char == "\n" and qoutationCount == 1:
                    qoutationCount = 0
                    Qotation = False
                    print(temp, lineNo)
                    createToken(temp)
                    char = ""
                    lineNo += 1
                    print(lineNo)

                if scommentFlag == True:
                    temp = ""
                elif mcommentFlag == True:
                    temp = temp + char
                else:
                    temp = temp+char
                

                

token_file_init()
word_analyzer(file)
token_file_update()