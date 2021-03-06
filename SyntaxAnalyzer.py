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
    Start_selection = ['int', 'string', 'float', 'char', 'bool', 'ID', 'this', 'super', 'while', 'for', 'if', 'do',
                       'break', 'continue', 'try', 'print', 'return', 'INCDEC', 'def', 'public', 'private', 'class', 'static', '$']

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
        else:
            return False

# dot problem


def SST(Tks):
    global I
    SST_sel = ['char', 'int', 'string', 'bool', 'float', 'ID', 'this', 'super', 'while', 'for', 'if', 'do',
               'break', 'continue', 'try', 'print', 'return', '++', '--', 'def', 'class', 'static', 'public', 'private', '$']
    if(Tks['classPart'][I] in SST_sel):
        if(DT(Tks)):
            if(SST1(Tks)):
                return True
        elif(Tks['classPart'][I] == 'ID'):
            I += 1
            if(SST2(Tks)):
                return True
            return True
        elif(TS(Tks)):
            if(Tks['classPart'][I] == 'ID'):
                I = + 1
                if(R(Tks)):
                    if(SST3(Tks)):
                        return True
            return True
        elif(INCDECOP(Tks)):
            if(TS(Tks)):
                if(Tks['classPart'][I] == 'ID'):
                    I += 1
                    if(R(Tks)):
                        return True
                return True
        elif (While_st(Tks)):
            return True
        elif (if_else_st(Tks)):
            return True
        elif (for_st(Tks)):
            return True
        elif (do_while_st(Tks)):
            return True
        elif (break_st(Tks)):
            return True
        elif (continue_st(Tks)):
            return True
        elif (try_except_st(Tks)):
            return True
        elif (print_st(Tks)):
            return True
        elif (return_st(Tks)):
            return True
        elif (Fn_call(Tks)):
            return True
    else:
        return False


def Fn_call(Tks):
    global I
    if(Tks['classPart'][I] == 'ID'):
        I += 1
        if(Tks['classPart'][I] == '('):
            I += 1
            if(Parameter1(Tks)):
                if(Tks['classPart'][I] == ')'):
                    return True
    else:
        return False


def While_st(Tks):
    global I
    While_sel = ['char', 'int', 'string', 'bool', 'float', 'ID', 'this', 'super', 'while', 'for', 'if', 'do',
                 'break', 'continue', 'try', 'print', 'return', '++', '--', 'def', 'class', 'static', 'public', 'private']
    if(Tks['classPart'][I] in While_sel):
        if(Tks['classPart'][I] == 'while'):
            I += 1
            if(Tks['classPart'][I] == '('):
                I += 1
                if(OE(Tks)):
                    if(Tks['classPart'][I] == ')'):
                        if(Body(Tks)):
                            return True
    else:
        return False


def if_else_st(Tks):
    global I
    if_else_sel = ['char', 'int', 'string', 'bool', 'float', 'ID', 'this', 'super', 'while', 'for', 'if', 'do',
                   'break', 'continue', 'try', 'print', 'return', '++', '--', 'def', 'class', 'static', 'public', 'private']
    if(Tks['classPart'][I] in if_else_sel):
        if(Tks['classPart'][I] == 'if'):
            I += 1
            if(Tks['classPart'][I] == '('):
                I += 1
                if(OE(Tks)):
                    if(Tks['classPart'][I] == ')'):
                        if(Body(Tks)):
                            if(Else(Tks)):
                                return True
    else:
        return False


def Else(Tks):
    global I
    if(Tks['classPart'][I] == 'else'):
        I += 1
        if(Body(Tks)):
            return True
    else:
        return False


def for_st(Tks):
    global I
    for_st_sel = ['char', 'int', 'string', 'bool', 'float', 'ID', 'this', 'super', 'while', 'for', 'if', 'do',
                  'break', 'continue', 'try', 'print', 'return', '++', '--', 'def', 'class', 'static', 'public', 'private']
    if(Tks['classPart'][I] in for_st_sel):
        if(Tks['classPart'][I] == 'for'):
            I += 1
            if(Tks['classPart'][I] == '('):
                I += 1
                if(C1(Tks)):
                    if(C2(Tks)):
                        if(Tks['classPart'][I] == ';'):
                            I += 1
                            if(C3(Tks)):
                                if(Tks['classPart'][I] == ')'):
                                    I += 1
                                    if(Body(Tks)):
                                        return True
    else:
        return False


def C1(Tks):
    global I
    C1_sel = ['int', 'string', 'char', 'float', 'bool', 'super', 'this', 'ID', ';',
              'IC', 'CC', 'SC', 'FC', '!', '++', '--', '(']
    if(Tks['classPart'][I] in C1_sel):
        if(DEC(Tks)):
            return True
        elif(Assign_st(Tks)):
            return True
        elif(Tks['classPart'][I] == ';'):
            return True
    else:
        return False


def C2(Tks):
    C2_sel = ['ID', ';', 'IC', 'CC',
              'SC', 'FC', '!', '++', '--', '(']
    if(Tks['classPart'][I] in C2_sel):
        if(OE(Tks)):
            return True
    else:
        return False


def C3(Tks):
    global I
    C3_sel = ['++', '--', 'super', 'this', 'ID', ')']
    if(Tks['classPart'][I] in C3_sel):
        if(TS(Tks)):
            if(Tks['classPart'][I] == 'ID'):
                I += 1
                if(R(Tks)):
                    if(SST3(Tks)):
                        return True
                    return True
                return True
        elif(INCDECOP(Tks)):
            if(TS(Tks)):
                if(Tks['classPart'][I] == 'ID'):
                    I += 1
                    if(R(Tks)):
                        return True
                return True
            return True
    else:
        return False


def Assign_st(Tks):
    global I
    assign_st_sel = ['char', 'int', 'string', 'bool', 'float', 'ID', 'this', 'super',
                     'IC', 'SC', 'CC', 'FC', '!', '++', '--', ';', '(']
    if(Tks['classPart'][I] in assign_st_sel):
        if(TS(Tks)):
            if(Tks['classPart'][I] == 'ID'):
                I += 1
                if(R(Tks)):
                    if(Assign_Op(Tks)):
                        if(OE(Tks)):
                            if(Tks['classPart'][I] == ';'):
                                return True
    else:
        return False


def do_while_st(Tks):
    global I
    do_while_sel = ['char', 'int', 'string', 'bool', 'float', 'ID', 'this', 'super', 'while', 'for', 'if', 'do',
                    'break', 'continue', 'try', 'print', 'return', '++', '--', 'def', 'class', 'static', 'public', 'private']
    if(Tks['classPart'][I] in do_while_sel):
        if(Tks['classPart'][I] == 'do'):
            I += 1
            if(Body(Tks)):
                if(While1(Tks)):
                    return True
    else:
        return False

# While1 used for do_while


def While1(Tks):
    global I
    if(Tks['classPart'][I] == 'while'):
        I += 1
        if(Tks['classPart'][I] == '('):
            I += 1
            if(OE(Tks)):
                if(Tks['classPart'][I] == ')'):
                    if(Tks['classPart'][I] == ';'):
                        return True
    else:
        return False


def break_st(Tks):
    global I
    if(Tks['classPart'][I] == 'break'):
        I += 1
        if(Tks['classPart'][I] == ';'):
            return True
    else:
        return False


def continue_st(Tks):
    global I
    if(Tks['classPart'][I] == 'continue'):
        I += 1
        if(Tks['classPart'][I] == ';'):
            return True
    else:
        return False


def try_except_st(Tks):
    global I
    if(Tks['classPart'][I] == 'try'):
        I += 1
        if(t_body(Tks)):
            if(catch(Tks)):
                return True
            return True
    else:
        return False


def t_body(Tks):
    global I
    if(Tks['classPart'][I] == ';'):
        return True
    elif(Tks['classPart'][I] == '{'):
        I += 1
        if(t_MST(Tks)):
            if(Tks['classPart'][I] == '}'):
                return True
            return True
    else:
        return False


def t_MST(Tks):
    if(t_SST(Tks)):
        if(t_MST(Tks)):
            return True
        return True
    else:
        return False


def t_SST(Tks):
    if(DEC(Tks)):
        return True
    elif(FuncDec(Tks)):
        return True
    elif(if_else_st(Tks)):
        return True
    elif(try_except_st(Tks)):
        return True
    elif(print_st(Tks)):
        return True
    else:
        return False


def catch(Tks):
    global I
    if(Tks['classPart'][I] == 'catch'):
        I += 1
        if(Tks['classPart'][I] == '('):
            I += 1
            if(ET(Tks)):
                I += 1
                if(Tks['classPart'][I] == 'ID'):
                    if(Tks['classPart'][I] == ')'):
                        I += 1
                        if(catch_body(Tks)):
                            if(catch(Tks)):
                                if(Finally(Tks)):
                                    return True
                                return True
                            return True
    else:
        return False


def ET(Tks):
    if(Tks['classPart'][I] == 'Arithmetic Exception'):
        return True
    elif(Tks['classPart'][I] == 'Array Index out of Bound Exception'):
        return True
    elif(Tks['classPart'][I] == 'Class not found Exception'):
        return True
    elif(Tks['classPart'][I] == 'File not found Exception'):
        return True
    elif(Tks['classPart'][I] == 'IO Exception'):
        return True
    elif(Tks['classPart'][I] == 'Interrupt Exception'):
        return True
    elif(Tks['classPart'][I] == 'String Index out of Bound Exception'):
        return True
    else:
        return False


def catch_body(Tks):
    global I
    if(Tks['classPart'][I] == ';'):
        return True
    elif(Tks['classPart'][I] == '{'):
        I += 1
        if(catch_MST(Tks)):
            if(Tks['classPart'][I] == '}'):
                return True
            return True
    else:
        return False


def catch_MST(Tks):
    if(catch_SST(Tks)):
        if(catch_MST(Tks)):
            return True
        return True
    else:
        return False


def catch_SST(Tks):
    if(DEC(Tks)):
        return True
    elif(FuncDec(Tks)):
        return True
    elif(if_else_st(Tks)):
        return True
    elif(throw(Tks)):
        return True
    elif(print_st(Tks)):
        return True
    else:
        return False


def throw(Tks):
    global I
    if(Tks['classPart'][I] == 'throw'):
        I += 1
        if(Tks['classPart'][I] == 'new'):
            I += 1
            if(ET(Tks)):
                if(Tks['classPart'][I] == '('):
                    I += 1
                    if(OE(Tks)):
                        if(Tks['classPart'][I] == ')'):
                            I += 1
                            if(Tks['classPart'][I] == ';'):
                                return True
    else:
        return False


def Finally(Tks):
    global I
    if(Tks['classPart'][I] == 'finally'):
        I += 1
        if(catch_body(Tks)):
            return True
    else:
        return False


def Obj_DEC(Tks):
    global I
    if(Tks['classPart'][I] == 'ID'):
        I += 1
        if(Tks['classPart'][I] == 'ID'):
            I += 1
            if(Tks['classPart'][I] == '='):
                I += 1
                if(Tks['classPart'][I] == 'new'):
                    I += 1
                    if(Tks['classPart'][I] == 'ID'):
                        I += 1
                        if(Tks['classPart'][I] == '('):
                            I += 1
                            if(Parameter1(Tks)):
                                if(Tks['classPart'][I] == ')'):
                                    I += 1
                                    if(Tks['classPart'][I] == ';'):
                                        return True
    else:
        return False


def print_st(Tks):
    global I
    if(Tks['classPart'][I] == 'print'):
        I += 1
        if(Tks['classPart'][I] == '('):
            I += 1
            if(OE(Tks)):
                if(Tks['classPart'][I] == ')'):
                    if(Tks['classPart'][I] == ';'):
                        return True
    else:
        return False


def return_st(Tks):
    global I
    if(Tks['classPart'][I] == 'return'):
        I += 1
        if(OE(Tks)):
            if(Tks['classPart'][I] == ';'):
                return True
    else:
        return False


def INCDECOP(Tks):
    global I
    if(Tks['classPart'][I] == '++'):
        I += 1
        return True
    elif(Tks['classPart'][I] == '--'):
        I += 1
        return True
    else:
        return False


def R(Tks):
    global I
    R_sel = ['.ID', '+=', '-=', '*=', '/=', '%=', '=', '++', '--', ';', ')']
    if(Tks['classPart'][I] in R_sel):
        if(Tks['classPart'][I] == '.'):
            I += 1
            if(Tks['classPart'][I] == 'ID'):
                I += 1
                if(Ref(Tks)):
                    if(Init(Tks)):
                        return True
        return True
    else:
        return False


def Ref(Tks):
    if(ID_ref(Tks)):
        if(Ref1(Tks)):
            if(Ref(Tks)):
                return True
    else:
        return False


def Ref1(Tks):
    global I
    if(Tks['classPart'][I] == '('):  # for .Fn()
        I += 1
        if(Tks['classPart'][I] == ')'):
            return True
    elif(Tks['classPart'][I] == '['):  # for  Arr[]
        I += 1
        if(Tks['classPart'][I] == ']'):
            return True
    else:
        return False


def ID_ref(Tks):
    global I
    if(Tks['classPart'][I] == '.'):
        I += 1
        if(Tks['classPart'][I] == 'ID'):
            I += 1
            if(Ref(Tks)):
                return True
    else:
        return False


def SST1(Tks):
    global I
    if(Tks['classPart'][I] == 'ID'):
        I += 1
        if(Init(Tks)):
            if(List(Tks)):
                return True
    elif(BR(Tks)):
        if(Tks['classPart'][I] == 'ID'):
            I += 1
            if(A1(Tks)):
                return True
    else:
        return False


def SST2(Tks):
    global I
    if(Tks['classPart'][I] == '('):
        I += 1
        if(Parameter1(Tks)):
            if(Tks['classPart'][I] == ')'):
                return True
        return True
    elif(R(Tks)):
        if(SST3(Tks)):
            return True
    elif(Tks['classPart'][I] == 'ID'):
        I += 1
        if(Tks['classPart'][I] == '='):
            I += 1
            if(Tks['classPart'][I] == 'new'):
                I += 1
                if(Tks['classPart'][I] == 'ID'):
                    I += 1
                    if(Tks['classPart'][I] == '('):
                        I += 1
                        if(Parameter1(Tks)):
                            if(Tks['classPart'][I] == ')'):
                                I += 1
                                if(Tks['classPart'][I] == ';'):
                                    return True
    else:
        return False


# selection set for SST1 SST2 SST3 incomplete
def SST3(Tks):
    global I
    if(Assign_Op(Tks)):
        if(OE(Tks)):
            if(Tks['classPart'][I] == ';'):
                return True
    elif(INCDECOP(Tks)):
        if(Tks['classPart'][I] == ';'):
            return True
        return True
    else:
        return False

# Declaration


def DEC(Tks):
    global I
    DEC_sel = ['char', 'int', 'string', 'bool', 'float', 'ID', 'this', 'super', 'while', 'for', 'if', 'do',
               'break', 'continue', 'try', 'print', 'return', '++', '--', 'def', 'class', 'static', 'public', 'private']
    if(Tks['classPart'][I] in DEC_sel):
        if(DT(Tks)):
            if(Tks['classPart'][I] == 'ID'):
                I += 1
                if(Init(Tks)):
                    if(List(Tks)):
                        return True
    else:
        return False


def Init(Tks):
    global I
    Init_sel = ['=', ';', ',', '+=', '-=', '*=', '/=', '%=', '--', '++', ')']
    if(Tks['classPart'][I] in Init_sel):
        if(Tks['classPart'][I] == '='):
            I += 1
            if(OE(Tks)):
                return True
    else:
        return False


def List(Tks):
    global I
    List_sel = [';', ',', 'private', 'public', 'protected', 'int', 'char', 'string', 'bool', 'float', 'def', 'ID', 'super', 'this', 'while',
                'for', 'if', 'return', 'print', 'break', 'continue', 'try', '++', '--', 'IC', 'CC', 'FC', 'SC', '!', '(']
    if(Tks['classPart'][I] in List_sel):
        if(Tks['classPart'][I] == ';'):
            I += 1
            return True
        elif(Tks['classPart'][I] == ','):
            I += 1
            if(Tks['classPart'][I] == 'ID'):
                I += 1
                if(Init(Tks)):
                    if(List(Tks)):
                        return True
                return True
        else:
            return False
    else:
        return False


def BR(Tks):
    global I
    if(Tks['classPart'][I] == '['):
        I += 1
        if(Tks['classPart'][I] == ']'):
            I += 1
            if(BR(Tks)):
                return True
            return True
    else:
        return False


def A1(Tks):
    global I
    if(Tks['classPart'][I] == '='):
        I += 1
        if(Tks['classPart'][I] == 'new'):
            I += 1
            if(DT(Tks)):
                if(BR1(Tks)):
                    if(Tks['classPart'][I] == ';'):
                        I += 1
                        return True
    else:
        return False


def BR1(Tks):
    global I
    if(Tks['classPart'][I] == '['):
        I += 1
        if(IP(Tks)):
            if(Tks['classPart'][I] == ']'):
                I += 1
                if(BR1(Tks)):
                    return True
                return True
    else:
        return False

# Array [<IP>]


def IP(Tks):
    global I
    if(Tks['classPart'][I] == 'IC'):  # Check this ?
        I += 1
        return True
    else:
        return False

# For Fun_call / Arguments

# c


def Parameter1(Tks):
    if(Const(Tks)):
        if(Const1(Tks)):
            return True
        return True
    else:
        return False


def Const(Tks):
    global I
    if(Tks['classPart'][I] == 'IC'):
        I += 1
        return True
    elif(Tks['classPart'][I] == 'CC'):
        I += 1
        return True
    elif(Tks['classPart'][I] == 'FC'):
        I += 1
        return True
    elif(Tks['classPart'][I] == 'SC'):
        I += 1
        return True
    else:
        return False


def Const1(Tks):
    global I
    if(Tks['classPart'][I] == ','):
        I += 1
        if(Parameter1(Tks)):
            return True
        return True
    else:
        return False
# c


def Assign_Op(Tks):
    if(Tks['classPart'][I] == '='):
        return True
    elif(Tks['classPart'][I] == '+='):
        return True
    elif(Tks['classPart'][I] == '-='):
        return True
    elif(Tks['classPart'][I] == '*='):
        return True
    elif(Tks['classPart'][I] == '/='):
        return True
    elif(Tks['classPart'][I] == '%='):
        return True
    else:
        return False


# dot problem
def TS(Tks):
    TS_sel = ['ID', 'this', 'super']
    global I
    if Tks['classPart'][I] in TS_sel:
        if(Tks['classPart'][I] == 'this'):
            I += 1
            return True
        elif (Tks['classPart'][I] == 'super'):
            I += 1
            return True
        return True
    else:
        return False


def FuncDec(Tks):
    global I
    Funcdecl_sel = ['def', 'ID', 'int', 'string', 'char', 'float', 'bool', 'this', 'super', 'while', 'for', 'if',
                    'do', 'break', 'continue', 'try', 'print', 'return', '++', '--', 'class', 'public', 'private', 'static', '$']
    if(Tks['classPart'][I] in Funcdecl_sel):
        if(Tks['classPart'][I] == 'def'):
            I += 1
            if(DT(Tks)):
                if(Tks['classPart'][I] == 'ID'):
                    I += 1
                    if(Tks['classPart'][I] == '('):
                        I += 1
                        if(Parameter(Tks)):
                            if(Tks['classPart'][I] == ')'):
                                I += 1
                                if(Body(Tks)):
                                    return True
    else:
        return False


def ClassDec(Tks):
    global I
    Classdecl_sel = ['def', 'ID', 'int', 'string', 'char', 'float', 'bool', 'this', 'super', 'while', 'for', 'if',
                     'do', 'break', 'continue', 'try', 'print', 'return', '++', '--', 'class', 'public', 'private', 'static', '$']
    if(Tks['classPart'][I] in Classdecl_sel):
        if(C_AM(Tks)):
            if(Tks['classPart'][I] == 'class'):
                I += 1
                if(Tks['classPart'][I] == 'ID'):
                    I += 1
                    if(Tks['classPart'][I] == '('):
                        I += 1
                        if(Tks['classPart'][I] == ')'):
                            I += 1
                            if(inh(Tks)):
                                if(C_body(Tks)):
                                    return True
    else:
        return False


def C_AM(Tks):
    C_AM_sel = ['public', 'private', 'class']
    global I
    if Tks['classPart'][I] in C_AM_sel:
        if(Tks['classPart'][I] == 'public'):
            I += 1
            return True
        elif(Tks['classPart'][I] == 'private'):
            I += 1
            return True
        return True
    else:
        return False


def inh(Tks):
    global I
    inh_sel = ['extends', ';', '{']
    if(Tks['classPart'][I] in inh_sel):
        if(Tks['classPart'][I] == 'extends'):
            I += 1
            if(Tks['classPart'][I] == 'ID'):
                I += 1
                return True
        return True
    else:
        return False


def C_body(Tks):
    global I
    C_body_sel = ['ID', 'int', 'string', 'char', 'float', 'bool', 'this', 'super', 'while', 'for', 'if', 'do',
                  'break', 'continue', 'try', 'print', 'return', '++', '--', 'class', 'public', 'private', 'static', '$', ';', '{']
    if(Tks['classPart'][I] in C_body_sel):
        if(Tks['classPart'][I] == ';'):
            I += 1
            return True
        elif(Tks['classPart'][I] == '{'):
            I += 1
            if(C_MST(Tks)):
                if(Tks['classPart'][I] == '}'):
                    return True
                return True
    else:
        return False


def C_MST(Tks):
    global I
    C_MST_sel = ['def', 'ID', 'int', 'string', 'char',
                 'float', 'bool', 'public', 'private', 'protected', '}']
    if(Tks['classPart'][I] in C_MST_sel):
        if(C_SST(Tks)):
            # if(C_MST(Tks)):
            #     return True
            return True
    else:
        return False


def C_SST(Tks):
    global I
    C_SST_sel = ['def', 'ID', 'int', 'string', 'char',
                 'float', 'bool', 'public', 'private', 'protected', '}']
    if(Tks['classPart'][I] in C_SST_sel):
        if(C_Decl(Tks)):
            return True
        elif(C_FuncDecl(Tks)):
            return True
        elif(Array_Decl(Tks)):
            return True
        elif(Constructor(Tks)):
            return True
        return True
    else:
        return False


# Decl inside class
def C_Decl(Tks):
    global I
    C_Decl_sel = ['def', 'ID', 'int', 'string', 'char',
                  'float', 'bool', 'public', 'private', 'protected', '}']
    if(Tks['classPart'][I] in C_Decl_sel):
        if(AM(Tks)):
            if(DT(Tks)):
                if(Tks['classPart'][I] == 'ID'):
                    I += 1
                    if(Init(Tks)):
                        if(List(Tks)):
                            return True
                        return True
    else:
        return False


def AM(Tks):
    AM_sel = ['public', 'private', 'protected']
    global I
    if Tks['classPart'][I] in AM_sel:
        if(Tks['classPart'][I] == 'public'):
            I += 1
            return True
        elif(Tks['classPart'][I] == 'private'):
            I += 1
            return True
        elif(Tks['classPart'][I] == 'protected'):
            I += 1
            return True
        return True
    else:
        return False


def C_FuncDecl(Tks):
    global I
    C_Funcdecl_sel = ['def', 'ID', 'int', 'string', 'char',
                      'float', 'bool', 'public', 'private', 'protected', '}']
    if(Tks['classPart'][I] in C_Funcdecl_sel):
        if(AM(Tks)):
            if(Tks['classPart'][I] == 'def'):
                I += 1
                if(RT(Tks)):
                    if(Tks['classPart'][I] == 'ID'):
                        I += 1
                        if(Tks['classPart'][I] == '('):
                            I += 1
                            if(Parameter(Tks)):
                                if(Tks['classPart'][I] == ')'):
                                    I += 1
                                    if(F_body(Tks)):
                                        return True
    else:
        return False


def RT(Tks):
    if(Tks['classPart'][I] == 'void'):
        return True
    elif(DT(Tks)):
        return True
    else:
        return False

# Function body


def F_body(Tks):
    global I
    F_body_sel = ['def', 'ID', 'int', 'string', 'char',
                  'float', 'bool', 'public', 'private', 'protected', '}']
    if(Tks['classPart'][I] in F_body_sel):
        if(Tks['classPart'][I] == ';'):
            return True
        elif(Tks['classPart'][I] == '{'):
            I += 1
            if(F_MST(Tks)):
                if(Tks['classPart'][I] == '}'):
                    return True
    else:
        return False

# MST inside Function


def F_MST(Tks):
    F_MST_sel = ['super', 'this', 'ID', '=', '+=', '-=', '*=', '/=',
                 '%=', 'while', 'for', 'do', 'if', 'return', 'print', '}']
    if(Tks['classPart'][I] in F_MST_sel):
        if(F_SST(Tks)):
            if(F_MST(Tks)):
                return True
            return True
    else:
        return False

# SST inside Function


def F_SST(Tks):
    F_SST_sel = ['super', 'this', 'ID', '=', '+=', '-=', '*=', '/=',
                 '%=', 'while', 'for', 'do', 'if', 'return', 'print', '}']
    if(Tks['classPart'][I] in F_SST_sel):
        if(Dec1(Tks)):
            return True
        elif(While_st(Tks)):
            return True
        elif(for_st):
            return True
        elif(do_while_st(Tks)):
            return True
        elif(if_else_st(Tks)):
            return True
        elif(return_st(Tks)):
            return True
        elif(print_st(Tks)):
            return True
    else:
        return False

# Decl inside Function


def Dec1(Tks):
    global I
    if(TS(Tks)):
        if(Tks['classPart'][I] == 'ID'):
            I += 1
            if(Assign_Op(Tks)):
                if(OE(Tks)):
                    return True
                return True
    elif(DT(Tks)):
        if(Tks['classPart'][I] == 'ID'):
            I += 1
            if(List(Tks)):
                return True
    else:
        return False


def Array_Decl(Tks):
    global I
    if(DT(Tks)):
        if(BR(Tks)):
            if(Tks['classPart'][I] == 'ID'):
                I += 1
                if(A1(Tks)):
                    return True
    else:
        return False


def Constructor(Tks):
    global I
    if(Tks['classPart'][I] == 'ID'):
        I += 1
        if(Tks['classPart'][I] == '('):
            I += 1
            if(Tks['classPart'][I] == ')'):
                I += 1
                if(F_body(Tks)):
                    return True
    else:
        return False


def DT(Tks):
    global I
    datatype_sel = ['char', 'string', 'int',
                    'bool', 'float', 'ID', 'main', '[']
    if(Tks['classPart'][I] in datatype_sel):
        if(Tks['classPart'][I] == 'int'):
            I += 1
            return True
        elif(Tks['classPart'][I] == 'char'):
            I += 1
            return True
        elif(Tks['classPart'][I] == 'string'):
            I += 1
            return True
        elif(Tks['classPart'][I] == 'float'):
            I += 1
            return True
        elif(Tks['classPart'][I] == 'bool'):
            I += 1
            return True
    else:
        return False


def Parameter(Tks):
    global I
    parameter_sel = ['char', 'int', 'string', 'bool', 'float', ')']
    if(Tks['classPart'][I] in parameter_sel):
        if(DT(Tks)):
            if(Tks['classPart'][I] == 'ID'):
                I += 1
                if(P1(Tks)):
                    return True
        return True
    else:
        return False


def P1(Tks):
    global I

    if(Tks['classPart'][I] == '='):
        I += 1
        if(OE(Tks)):
            if(P2(Tks)):
                return True
            return True
    else:
        return False


def P2(Tks):
    global I
    if(Tks['classPart'][I] == ','):
        I += 1
        if(Parameter(Tks)):
            return True
        return True
    else:
        return False


def OE(Tks):
    OE_sel = ['super', 'this', 'ID', 'while', 'for', 'do', 'if', 'return', 'print', 'IC', 'CC',
              'SC', 'FC', '!', '++', '--', '(', ')', ';', 'char', 'int', 'string', 'bool', 'float']
    if(Tks['classPart'][I] in OE_sel):
        if(AE(Tks)):
            if(OE1(Tks)):
                return True
    else:
        return False


def OE1(Tks):
    global I
    if(Tks['classPart'][I] == '||'):
        I += 1
        if(AE(Tks)):
            if(OE1(Tks)):
                return True
    else:
        return False


def AE(Tks):
    if(RE(Tks)):
        if(AE1(Tks)):
            return True
    else:
        return False


def RE(Tks):
    if(E(Tks)):
        if(RE1(Tks)):
            return True
        return True
    else:
        return False


def AE1(Tks):
    global I
    if(Tks['classPart'][I] == '&&'):
        I += 1
        if(RE(Tks)):
            if(AE1(Tks)):
                return True
            return True
    else:
        return False


def E(Tks):
    if(T(Tks)):
        if(E1(Tks)):
            return True
        return True
    else:
        return False


def RE1(Tks):
    if(REO(Tks)):
        if(E(Tks)):
            if(RE1(Tks)):
                return True
        return True
    else:
        return False


def REO(Tks):
    global I
    relationalOP = ['<', '>', '<=', '>=', '!=', '==']
    if(Tks['classPart'][I] == '<'):
        I += 1
        return True
    elif(Tks['classPart'][I] == '>'):
        I += 1
        return True
    elif(Tks['classPart'][I] == '<='):
        I += 1
        return True
    elif(Tks['classPart'][I] == '>='):
        I += 1
        return True
    elif(Tks['classPart'][I] == '!='):
        I += 1
        return True
    elif(Tks['classPart'][I] == '=='):
        I += 1
        return True
    else:
        return False


def PM(Tks):
    global I
    if(Tks['classPart'][I] == '+'):
        I += 1
        return True
    elif(Tks['classPart'][I] == '-'):
        I += 1
        return True
    else:
        return False


def MDM(Tks):
    global I
    if(Tks['classPart'][I] == '*'):
        I += 1
        return True
    elif(Tks['classPart'][I] == '/'):
        I += 1
        return True
    elif(Tks['classPart'][I] == '%'):
        I += 1
        return True
    else:
        return False


def T(Tks):
    if(F(Tks)):
        if(T1(Tks)):
            return True
    else:
        return False


def E1(Tks):
    if(PM(Tks)):
        if(T(Tks)):
            if(E1(Tks)):
                return True
        return True
    else:
        return False


def T1(Tks):
    if(MDM(Tks)):
        if(F(Tks)):
            if(T1(Tks)):
                return True
        return True
    else:
        return False


def F(Tks):
    global I
    if(Tks['classPart'][I] == 'ID'):
        I += 1
        if(F1(Tks)):
            return True
        return True
    elif(Tks['classPart'][I] == 'IC' or Tks['classPart'][I] == 'CC' or Tks['classPart'][I] == 'SC'):
        if(Const(Tks)):
            return True
        return True
    elif(Tks['classPart'][I] == '!'):
        I += 1
        if(F(Tks)):
            return True
    elif(INCDECOP(Tks)):
        if(TS(Tks)):
            if(Tks['classPart'][I] == 'ID'):
                I += 1
                if(R(Tks)):
                    return True
    elif(OE(Tks)):
        return True
    elif(Tks['classPart'][I] == '('):
        I += 1
        if(OE(Tks)):
            if(Tks['classPart'][I] == ')'):
                return True
            # return True
    else:
        return False


def F1(Tks):
    global I
    F1_sel = ['ID', '(']
    if(Tks['classPart'][I] in F1_sel):
        if(Tks['classPart'][I] == '('):
            I += 1
            if(Parameter1(Tks)):
                if(Tks['classPart'][I] == ')'):
                    return True
            return True
        elif(R(Tks)):
            if(INCDECOP(Tks)):
                return True
        return True
    else:
        return False


def Body(Tks):
    global I
    body_sel = [';', '{', 'int', 'char', 'string', 'bool', 'float', 'ID', 'while', 'if', 'for', 'do',
                'break', 'continue', 'try', 'print', 'return', 'INCDEC', 'else', 'def', 'class', 'static', '$']
    if(Tks['classPart'][I] in body_sel):
        if(Tks['classPart'][I] == ';'):
            I += 1
            return True
        elif(Tks['classPart'][I] == '{'):
            I += 1
            if(MST(Tks)):
                if(Tks['classPart'][I] == '}'):
                    return True
    else:
        return False

# dot problem


def MST(Tks):
    global I
    MST_sel = ['int', 'char', 'bool', 'float', 'string', 'ID', 'this', 'super',
               'while', 'for', 'if', 'do', 'break', 'continue', 'print', 'return', 'INCDEC', '}']

    if(Tks['classPart'][I] in MST_sel):
        if(SST(Tks)):
            if(MST(Tks)):
                return True
        return True
    else:
        return False


def Main(Tks):
    global I
    if(Tks['classPart'][I] == 'static'):
        I += 1
        if(DT(Tks)):
            if(Tks['classPart'][I] == 'Main'):
                I += 1
                if(Tks['classPart'][I] == '('):
                    I += 1
                    if(Tks['classPart'][I] == 'string'):
                        I += 1
                        if(Tks['classPart'][I] == '['):
                            I += 1
                            if(Tks['classPart'][I] == ']'):
                                I += 1
                                if(Tks['classPart'][I] == 'args'):
                                    I += 1
                                    if(Tks['classPart'][I] == ')'):
                                        I += 1
                                        if(Body(Tks)):
                                            return True
        return True
    else:
        return False
