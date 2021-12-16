from regex import *
import pandas as pd

file = "words.txt"
# file3 = "words.txt"
lineNo = 1    # line no in file
temp = ""     # store word

classPart = []
ValuePart = []
line = []

Qotation = addFlag = equalFlag = minusFlag = multiplyFlag = divideFlag = scommentFlag = mcommentFlag = moduloFlag = lessthanFlag = notFlag = greaterthanFlag = orFlag = dotFlag = AndFlag = False

qoutationCount = addCount = equalCount = minusCount = AndCount = orCount = mcommentCount = last_line = 0

char = qotationTemp = dotTemp = dotTemp1 = dot = ""


def printWord(string):

    global temp, char, lineNo, classPart, ValuePart, line

    classPart.append(str(is_keyword(string)))
    ValuePart.append(temp)
    line.append(lineNo)
    # file2 = open("lexical.txt", "a")
    # file2.write("{0}  {1}  {2}\n ".format(
    #     str(is_keyword(string)), temp, lineNo))
    # file2.close()
    temp = ""


def Printing():

    global classPart, ValuePart, line
    file2 = open("lexical.txt", "a")

    data = {
        "classPart": classPart,
        "ValuePart": ValuePart,
        "LineNo": line
    }
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    df = pd.DataFrame(data)
    file2.write(str(df))
    file2.close()
    temp = ""
    print(df)


def wordCount(file):

    global lineNo, temp, Qotation, qoutationCount, addCount, equalCount, addFlag, equalFlag, minusCount, minusFlag, multiplyFlag, moduloFlag, divideFlag, notFlag, greaterthanFlag, lessthanFlag, char, AndCount, AndFlag, orCount, orFlag, dotFlag, dotTemp, dotTemp1, dot, scommentFlag, mcommentFlag, mcommentCount, last_line, qotationTemp

    punctuator = [',', ';', '(', ')', '{', '}', '[', ']', ':', '?']

    # with open(file3, 'r') as file1:
    #     lines = file1.readlines()
    #     last_line_no = lines.index(lines[-1])
    #     last_line = lines[-1]

    with open(file, 'r') as files:  # open and close files
        for line in files:             # iterate through lines in file
            for char in line:          # iterate through character in a line
                # if new line character founded , print temp increase line no by 1 and reset char and temp
                if char == "\n" and Qotation == False and mcommentFlag == False:
                    if temp != "":
                        #print(temp, lineNo)
                        printWord(temp)
                        char = ""
                        lineNo += 1
                        # print(lineNo)
                    else:
                        scommentFlag = False
                        temp = ""
                        char = ""
                        lineNo += 1
                        # print(lineNo)
                elif char == "\n" and mcommentFlag == True:
                    lineNo += 1

                # if single comment hash is found
                if char == "#" and mcommentFlag == True:
                    pass
                elif char == "#" and Qotation == True:
                    pass
                elif char == '#':
                    if temp != '':
                        #print(temp, lineNo)
                        printWord(temp)
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
                    if temp != "" and mcommentCount == 1:
                        #print(temp, lineNo)
                        printWord(temp)
                        temp = char
                        char = ''
                    elif mcommentCount == 2:
                        temp = ""
                        char = ""
                        mcommentCount = 0
                        mcommentFlag = False

                # if mcommentFlag == True and mcommentCount == 1 and lineNo == last_line_no+1:
                #     if last_line[-1:] == "~":
                #         pass
                #     else:
                #         l1 = files.readlines()
                #         temp = temp + "\n"
                #         for i in range(len(l1)):
                #             temp = temp + l1[i]
                #         #print(temp, lineNo)
                #         printWord(temp)
                #         temp = ""
                #         char = ""
                #         mcommentFlag = False
                #         mcommentCount = 0
                #         break

                # space condition
                if char == " " and Qotation == True:
                    pass
                elif char == " " and scommentFlag == True:
                    char = ""
                elif char == " " and mcommentFlag == True:
                    pass
                elif char == " ":
                    addFlag = False
                    addCount = 0
                    minusCount = 0
                    minusFlag = False
                    equalFlag = False
                    multiplyFlag = False
                    equalCount = 0
                    AndCount = 0
                    AndFlag = False
                    dotFlag = False
                    orCount = 0
                    orFlag = False
                    if temp != "":
                        #print(temp, lineNo)
                        printWord(temp)
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
                        #print(temp, lineNo)
                        printWord(temp)
                    #print(char, lineNo)
                    temp = temp + char
                    printWord(temp)
                    temp = ""
                    char = ""

                if char == "\"" and scommentFlag == True:
                    char = ""
                elif char == "\"" and mcommentFlag == True:
                    pass
                elif char == "\"":
                    qotationTemp = char
                    Qotation = True
                    qoutationCount += 1

                    if temp != "" and qoutationCount == 1:
                        #print(temp, lineNo)
                        printWord(temp)

                    if char == "\"" and qoutationCount == 2:
                        qoutationCount = 0
                        Qotation = False
                        #print(temp, lineNo)
                        printWord(qotationTemp+temp+qotationTemp)
                        qotationTemp = ""

                    char = ""

                elif char == "\n" and qoutationCount == 1:
                    qoutationCount = 0
                    Qotation = False
                    #print(qotationTemp+temp, lineNo)
                    qotationTemp = qotationTemp+temp
                    temp = qotationTemp
                    printWord(qotationTemp)
                    char = ""
                    lineNo += 1
                    # print(lineNo)

                # addition condition
                if char == "+" and Qotation == True:
                    pass
                elif char == "+" and scommentFlag == True:
                    char = ""
                elif char == "+" and mcommentFlag == True:
                    pass
                elif char == "+":
                    addCount += 1
                    if temp != "" and addFlag == False:
                        #print(temp, lineNo)
                        printWord(temp)
                    addFlag = True
                    if temp != "" and addCount == 2:
                        addCount = 0
                        addFlag = False
                        temp = temp+char
                        #print(temp, lineNo)
                        printWord(temp)
                        char = ""

                if "+" in temp and char == "=" and Qotation == True:
                    pass
                elif "+" in temp and char == "=" and scommentFlag == True:
                    char = ""
                elif "+" in temp and char == "=" and mcommentFlag == True:
                    pass
                elif "+" in temp and char == "=":
                    temp = temp+char
                    #print(temp, lineNo)
                    printWord(temp)
                    addCount = 0
                    addFlag = False
                    char = ""

                if "+" in temp and char != "" and re.fullmatch("([+|-][0-9]+)|([0-9]+)", char) and Qotation == True:
                    pass
                elif "+" in temp and char != "" and re.fullmatch("([+|-][0-9]+)|([0-9]+)", char) and scommentFlag == True:
                    char = ""
                elif "+" in temp and char != "" and re.fullmatch("([+|-][0-9]+)|([0-9]+)", char) and mcommentFlag == True:
                    pass
                elif "+" in temp and char != "" and re.fullmatch("([+|-][0-9]+)|([0-9]+)", char):
                    temp = temp+char
                    #print(temp, lineNo)
                    printWord(temp)
                    addCount = 0
                    addFlag = False
                    char = ""

                if "+" in temp and char != "=" and Qotation == True:
                    pass
                elif "+" in temp and char != "=" and scommentFlag == True:
                    char = ""
                elif "+" in temp and char != "=" and mcommentFlag == True:
                    pass
                elif "+" in temp and char != "=":
                    #print(temp, lineNo)
                    printWord(temp)
                    addCount = 0
                    addFlag = False

                # minus condition
                if char == "-" and Qotation == True:
                    pass
                elif char == "-" and scommentFlag == True:
                    char = ""
                elif char == "-" and mcommentFlag == True:
                    pass
                elif char == "-":
                    minusCount += 1
                    if temp != "" and minusFlag == False:
                        #print(temp, lineNo)
                        printWord(temp)
                    minusFlag = True
                    if temp != "" and minusCount == 2:
                        minusCount = 0
                        minusFlag = False
                        temp = temp+char
                        #print(temp, lineNo)
                        printWord(temp)
                        char = ""

                if "-" in temp and char == "=" and Qotation == True:
                    pass
                elif "-" in temp and char == "=" and scommentFlag == True:
                    char = ""
                elif "-" in temp and char == "=" and mcommentFlag == True:
                    pass
                elif "-" in temp and char == "=":
                    temp = temp+char
                    #print(temp, lineNo)
                    printWord(temp)
                    minusCount = 0
                    minusFlag = False
                    char = ""

                if "-" in temp and char != "" and re.fullmatch("([+|-][0-9]+)|([0-9]+)", char) and Qotation == True:
                    pass
                elif "-" in temp and char != "" and re.fullmatch("([+|-][0-9]+)|([0-9]+)", char) and scommentFlag == True:
                    char = ""
                elif "-" in temp and char != "" and re.fullmatch("([+|-][0-9]+)|([0-9]+)", char) and mcommentFlag == True:
                    pass
                elif "-" in temp and char != "" and re.fullmatch("([+|-][0-9]+)|([0-9]+)", char):
                    temp = temp+char
                    #print(temp, lineNo)
                    printWord(temp)
                    addCount = 0
                    addFlag = False
                    char = ""

                if "-" in temp and char != "=" and Qotation == True:
                    pass
                elif "-" in temp and char != "=" and scommentFlag == True:
                    char = ""
                elif "-" in temp and char != "=" and mcommentFlag == True:
                    pass
                elif "-" in temp and char != "=":
                    #print(temp, lineNo)
                    printWord(temp)
                    minusCount = 0
                    minusFlag = False

                # multiply
                if char == "*" and Qotation == True:
                    pass
                elif char == "*" and scommentFlag == True:
                    char = ""
                elif char == "*" and mcommentFlag == True:
                    pass
                elif char == "*":
                    if temp != "" and multiplyFlag == False:
                        #print(temp, lineNo)
                        printWord(temp)
                    multiplyFlag = True

                if "*" in temp and char == "=" and Qotation == True:
                    pass
                elif "*" in temp and char == "=" and scommentFlag == True:
                    char = ""
                elif "*" in temp and char == "=" and mcommentFlag == True:
                    pass
                elif "*" in temp and char == "=":
                    temp = temp+char
                    #print(temp, lineNo)
                    printWord(temp)
                    multiplyFlag = False
                    char = ""

                if "*" in temp and char != "=" and Qotation == True:
                    pass
                elif "*" in temp and char != "=" and scommentFlag == True:
                    char = ""
                elif "*" in temp and char != "=" and mcommentFlag == True:
                    pass
                elif "*" in temp and char != "=":
                    #print(temp, lineNo)
                    printWord(temp)
                    multiplyFlag = False

                # divide
                if char == "/" and Qotation == True:
                    pass
                elif char == "/" and scommentFlag == True:
                    char = ""
                elif char == "/" and mcommentFlag == True:
                    pass
                elif char == "/":
                    if temp != "" and divideFlag == False:
                        #print(temp, lineNo)
                        printWord(temp)
                    divideFlag = True

                if "/" in temp and char == "=" and Qotation == True:
                    pass
                elif "/" in temp and char == "=" and scommentFlag == True:
                    char = ""
                elif "/" in temp and char == "=" and mcommentFlag == True:
                    pass
                elif "/" in temp and char == "=":
                    temp = temp+char
                    #print(temp, lineNo)
                    printWord(temp)
                    divideFlag = False
                    char = ""

                if "/" in temp and char != "=" and Qotation == True:
                    pass
                elif "/" in temp and char != "=" and scommentFlag == True:
                    char = ""
                elif "/" in temp and char != "=" and mcommentFlag == True:
                    pass
                elif "/" in temp and char != "=":
                    #print(temp, lineNo)
                    printWord(temp)
                    divideFlag = False

                # modulo
                if char == "%" and Qotation == True:
                    pass
                elif char == "%" and scommentFlag == True:
                    char = ""
                elif char == "%" and mcommentFlag == True:
                    pass
                elif char == "%":
                    if temp != "" and moduloFlag == False:
                        #print(temp, lineNo)
                        printWord(temp)
                    moduloFlag = True

                if "%" in temp and char == "=" and Qotation == True:
                    pass
                elif "%" in temp and char == "=" and scommentFlag == True:
                    char = ""
                elif "%" in temp and char == "=" and mcommentFlag == True:
                    pass
                elif "%" in temp and char == "=":
                    temp = temp+char
                    #print(temp, lineNo)
                    printWord(temp)
                    moduloFlag = False
                    char = ""

                if "%" in temp and char != "=" and Qotation == True:
                    pass
                elif "%" in temp and char != "=" and scommentFlag == True:
                    char = ""
                elif "%" in temp and char != "=" and mcommentFlag == True:
                    pass
                elif "%" in temp and char != "=":
                    #print(temp, lineNo)
                    printWord(temp)
                    moduloFlag = False

                # not condition
                if char == "!" and Qotation == True:
                    pass
                elif char == "!" and scommentFlag == True:
                    char = ""
                elif char == "!" and mcommentFlag == True:
                    pass
                elif char == "!":
                    if temp != "" and notFlag == False:
                        #print(temp, lineNo)
                        printWord(temp)
                    notFlag = True

                if "!" in temp and char == "=" and Qotation == True:
                    pass
                elif "!" in temp and char == "=" and scommentFlag == True:
                    char = ""
                elif "!" in temp and char == "=" and mcommentFlag == True:
                    pass
                elif "!" in temp and char == "=":
                    temp = temp+char
                    #print(temp, lineNo)
                    printWord(temp)
                    notFlag = False
                    char = ""

                if "!" in temp and char != "=" and Qotation == True:
                    pass
                elif "!" in temp and char != "=" and scommentFlag == True:
                    char = ""
                elif "!" in temp and char != "=" and mcommentFlag == True:
                    pass
                elif "!" in temp and char != "=":
                    #print(temp, lineNo)
                    printWord(temp)
                    notFlag = False

                # greater than condition
                if char == "<" and Qotation == True:
                    pass
                elif char == "<" and scommentFlag == True:
                    char = ""
                elif char == "<" and mcommentFlag == True:
                    pass
                elif char == "<":
                    if temp != "" and greaterthanFlag == False:
                        #print(temp, lineNo)
                        printWord(temp)
                    greaterthanFlag = True

                if "<" in temp and char == "=" and Qotation == True:
                    pass
                elif "<" in temp and char == "=" and scommentFlag == True:
                    char = ""
                elif "<" in temp and char == "=" and mcommentFlag == True:
                    pass
                elif "<" in temp and char == "=":
                    temp = temp+char
                    #print(temp, lineNo)
                    printWord(temp)
                    greaterthanFlag = False
                    char = ""

                if "<" in temp and char != "=" and Qotation == True:
                    pass
                elif "<" in temp and char != "=" and scommentFlag == True:
                    char = ""
                elif "<" in temp and char != "=" and mcommentFlag == True:
                    pass
                elif "<" in temp and char != "=":
                    #print(temp, lineNo)
                    printWord(temp)
                    greaterthanFlag = False

                # less than condition
                if char == ">" and Qotation == True:
                    pass
                elif char == ">" and scommentFlag == True:
                    char = ""
                elif char == ">" and mcommentFlag == True:
                    pass
                elif char == ">":
                    if temp != "" and lessthanFlag == False:
                        #print(temp, lineNo)
                        printWord(temp)
                    lessthanFlag = True

                if ">" in temp and char == "=" and Qotation == True:
                    pass
                elif ">" in temp and char == "=" and scommentFlag == True:
                    char = ""
                elif ">" in temp and char == "=" and mcommentFlag == True:
                    pass
                elif ">" in temp and char == "=":
                    temp = temp+char
                    #print(temp, lineNo)
                    printWord(temp)
                    lessthanFlag = False
                    char = ""

                if ">" in temp and char != "=" and Qotation == True:
                    pass
                elif ">" in temp and char != "=" and scommentFlag == True:
                    char = ""
                elif ">" in temp and char != "=" and mcommentFlag == True:
                    pass
                elif ">" in temp and char != "=":
                    #print(temp, lineNo)
                    printWord(temp)
                    lessthanFlag = False

                # && condition
                if char == "&" and Qotation == True:
                    pass
                elif char == "&" and scommentFlag == True:
                    char = ""
                elif char == "&" and mcommentFlag == True:
                    pass
                elif char == "&":
                    AndCount += 1
                    if temp != "" and AndFlag == False:
                        #print(temp, lineNo)
                        printWord(temp)
                    AndFlag = True
                    if temp != "" and AndCount == 2:
                        AndCount = 0
                        AndFlag = False
                        temp = temp+char
                        #print(temp, lineNo)
                        printWord(temp)
                        char = ""

                # || condition
                if char == "|" and Qotation == True:
                    pass
                elif char == "|" and scommentFlag == True:
                    char = ""
                elif char == "|" and mcommentFlag == True:
                    pass
                elif char == "|":
                    orCount += 1
                    if temp != "" and orFlag == False:
                        #print(temp, lineNo)
                        printWord(temp)
                    orFlag = True
                    if temp != "" and orCount == 2:
                        orCount = 0
                        orFlag = False
                        temp = temp+char
                        #print(temp, lineNo)
                        printWord(temp)
                        char = ""

                # dot condition
                if char == "." and Qotation == True:
                    pass
                elif char == "." and scommentFlag == True:
                    char = ""
                elif char == "." and mcommentFlag == True:
                    pass
                elif char == ".":
                    if temp != "" and dotFlag == False:
                        if re.fullmatch("([+|-][0-9]+)|([0-9]+)", temp):
                            dotTemp = temp
                            temp = ""
                            dotFlag = True
                            dot = char
                            char = ""
                        else:
                            #print(temp, lineNo)
                            printWord(temp)
                            dotFlag = True
                            dot = char
                            char = ""
                    else:
                        dot = char
                        char = ""
                        dotFlag = True

                if dotFlag == True and Qotation == True:
                    pass
                elif dotFlag == True and scommentFlag == True:
                    char = ""
                elif dotFlag == True and mcommentFlag == True:
                    pass
                elif dotFlag == True:
                    if char != "" and re.fullmatch("([+|-][0-9]+)|([0-9]+)", char):
                        dotTemp1 += char
                        char = ""
                    elif char != "":
                        temp = dotTemp+dot+dotTemp1
                        #print(temp, lineNo)
                        printWord(temp)
                        dotFlag = False
                        dot = ""
                        dotTemp = ""
                        dotTemp1 = ""

                # equals condition
                if char == "=" and Qotation == True:
                    pass
                elif char == "=" and scommentFlag == True:
                    char = ""
                elif char == "=" and mcommentFlag == True:
                    pass
                elif char == "=":
                    equalCount += 1
                    if temp != "" and equalFlag == False:
                        #print(temp, lineNo)
                        printWord(temp)
                    equalFlag = True
                    if temp != "" and equalCount == 2:
                        equalCount = 0
                        equalFlag = False
                        temp = temp+char
                        #print(temp, lineNo)
                        printWord(temp)
                        char = ""

                if "=" in temp and char != "=" and Qotation == True:
                    pass
                elif "=" in temp and char != "=" and scommentFlag == True:
                    char = ""
                elif "=" in temp and char != "=" and mcommentFlag == True:
                    pass
                elif "=" in temp and char != "=":
                    #print(temp, lineNo)
                    printWord(temp)
                    equalCount = 0
                    equalFlag = False

                if scommentFlag == True:
                    temp = ""
                elif mcommentFlag == True:
                    temp = temp + char
                else:
                    temp = temp + char

        if mcommentFlag == True:
            #print(temp, lineNo)
            printWord(temp)
        else:
            if temp != "":
                #print(temp, lineNo)
                printWord(temp)
        Printing()


wordCount(file)
