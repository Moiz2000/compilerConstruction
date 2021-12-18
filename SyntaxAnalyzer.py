import pandas as pd
I = 0


def Syntax_Analyzer(Tokens):
    Tks = pd.DataFrame(Tokens)
    global I
    if Start(Tks):
        print("Valid Syntax")
    else:
        print("Sytax Error at Line Number", Tks['LineNo'][I])


# check for dot
def Start(Tks):
    global I

    Start_selection = ['int', 'string', 'float', 'char', 'bool', 'ID', 'this', 'super', ''
                       'while', 'for', 'if', 'do', 'break', 'continue', 'try', 'print', 'return', 'INCDEC', 'def', 'public', 'private', 'class', 'static', '$']

    if (Tks['classPart'][I] in Start_selection):
        if(SST(Tks)):
            if(Start(Tks)):
                return True
            return True
        elif(FuncDec(Tks)):
            if(Start(Tks)):
                return True
            return True
        elif(ClassDec(Tks)):
            if(Start(Tks)):
                return True
            return True
        elif(Main(Tks)):
            if(Start(Tks)):
                return True
            return True
        elif(Tks['classPart'][I] == '$'):
            return True
        else:
            return False


def SST(Tks):
    pass


def FuncDec(Tks):
    pass


def ClassDec(Tks):
    pass


def Main(Tks):
    pass
