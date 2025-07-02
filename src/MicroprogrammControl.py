from atexit import register


F1 = {"000":"NOP", "001":"ADD", "010":"CLRAC", "011":"INCAC", "100":"DRTAC", "101":"DRTAR", "110":"PCTAR", "111":"WRITE"}
F2 = {"000":"NOP", "001":"SUB", "010":"OR", "011":"AND", "100":"READ", "101":"ACTDR", "110":"INCDR", "111":"PCTDR"}
F3 = {"000":"NOP", "001":"XOR", "010":"COM", "011":"SHL", "100":"SHR", "101":"INCPC", "110":"ARTPC", "111":"HLT"}

CD = {"00":"U", "01":"I", "10":"S", "11":"Z"}
BR = {"00":"JMP", "01":"CALL", "10":"RET", "11":"MAP"}

#-------------REGISTERS----------------------------------


AC  = 20
DR  = 0
PC  = 0
AR  = 0
CAR = 0
SBR = 0

AC_COPY = AC
DR_COPY = DR
PC_COPY = PC
AR_COPY = AR

#--------------------------------------------------------
#----------------------------F1--------------------------

def NOP():
    pass

def ADD():
    global AC_COPY 
    global DR
    AC_COPY = AC + DR

def CLRAC():
    global AC_COPY
    AC_COPY = 0

def INCAC():
    global AC_COPY
    AC_COPY = AC + 1

def DRTAC():
    global AC_COPY
    global DR
    AC_COPY = DR

def DRTAR():
    global AR_COPY
    global DR
    
    AR_COPY = int((bin(DR)[2:].zfill(16))[5:] , 2)

def PCTAR():
    global AR_COPY
    global PC
    AR_COPY = PC

def WRITE():
    global AR
    global DR
    Memory[AR] = bin(DR)[2:].zfill(16)

#------------------------------F2--------------------------

def SUB():
    global AC_COPY
    AC_COPY = AC - DR

def OR():
    global AC_COPY 
    AC_COPY = AC | DR

def AND():
    global AC_COPY
    global DR
    AC_COPY = AC & DR

def READ():
    global DR_COPY
    print("AR: " , AR  )
    DR_COPY = int(Memory[AR] , 2)
   

def ACTDR():
    global DR_COPY
    global AC
    DR_COPY = AC

def INCDR():
    global DR_COPY
    DR_COPY = DR + 1

def PCTDR():
    global DR_COPY
    global PC
    DR_COPY = PC

#------------------------------F3--------------------------

def XOR():
    global AC_COPY
    global DR
    AC_COPY = AC ^ DR

def COM():
    global AC_COPY
    AC_COPY = ~AC

def SHL():
    global AC_COPY
    AC_COPY = AC << 1

def SHR():
    global AC_COPY
    AC_COPY = AC >> 1

def INCPC():
    global PC_COPY
    PC_COPY = PC + 1

def ARTPC():
    global PC_COPY
    global AR
    PC_COPY = AR

def HLT():
    pass

#-------------------------BRANCHES-------------------------------
def JMP(CD_FLAG , Address):
    global CAR
    if(CD_FLAG):
        CAR = int(Address , 2)
    else:
        CAR += 1

def CALL(CD_FLAG , Address):
    global SBR
    global CAR

    if(CD_FLAG):
        SBR = CAR + 1
        CAR = int(Address , 2)
    else:
        CAR += 1   

def MAP():
    global CAR
    global DR

    
    print(str(bin(DR)[2:].zfill(16))[1:5])
    temp = '0' + str(bin(DR)[2:].zfill(16)[1:5]) + '00'
    CAR =  int(temp , 2)

def RET():
    global CAR
    global SBR
    CAR = SBR
#---------------------------CONDITIONS-----------------------------
def I_COND():
    global DR
    I = int(bin(DR)[2:].zfill(16)[0])
    if(I):
        return True
    else:
        return False
def U_COND():
    return True
def S_COND():
    global AC
    S = int(bin(AC)[2:].zfill(16)[15])
    if(S):
        return True
    else:
        return False

def Z_COND():
    global AC
    Z = (AC== 0)
    if(Z):
        return True
    else:
        return False
#--------------------------------------------------------

def CodeFunction(fun1, fun2, fun3 , FunctionDict):
    

    for fk , fv in FunctionDict.items():
        if(fv == fun1):
            return fk
        elif(fv == fun2):
            return fk
        elif(fv == fun3):
            return fk
        
    return "000"

def CodeBranch(branch):
    for bk , bv in BR.items():
        if(bv == branch):
            return bk
    return "00"
def CodeCondition(condition):
    for ck , cv in CD.items():
        if(cv == condition):
            return ck
    return "00"

def F1_functions(f1):
    if(F1[f1] == "NOP"):
        NOP()
    elif(F1[f1] == "ADD"):
        ADD()
    elif(F1[f1] == "CLRAC"):
        CLRAC()
    elif(F1[f1] == "INCAC"):
        INCAC()
    elif(F1[f1] == "DRTAC"):
        DRTAC()
    elif(F1[f1] == "DRTAR"):
        DRTAR()
    elif(F1[f1] == "PCTAR"):
        PCTAR()
    elif(F1[f1] == "WRITE"):
        WRITE()
    
def F2_functions(f2):
    if(F2[f2]=="NOP"):
        NOP()
    elif(F2[f2]=="SUB"):
        SUB()
    elif(F2[f2]=="OR"):
        OR()
    elif(F2[f2]=="AND"):
        AND()
    elif(F2[f2]=="READ"):
        READ()
    elif(F2[f2]=="ACTDR"):
        ACTDR()
    elif(F2[f2]=="INCDR"):
        INCDR()
    elif(F2[f2]=="PCTDR"):
        PCTDR()

def F3_functions(f3):
    if(F3[f3]=="NOP"):
        NOP()
    elif(F3[f3]=="XOR"):
        XOR()
    elif(F3[f3]=="COM"):
        COM()
    elif(F3[f3]=="SHL"):
        SHL()
    elif(F3[f3]=="SHR"):
        SHR()
    elif(F3[f3]=="INCPC"):
        INCPC()
    elif(F3[f3]=="ARTPC"):
        ARTPC()

def ControlUnit():
    global CAR
    global AC
    global DR
    global PC
    global AR
    global SBR

    global AC_COPY
    global DR_COPY
    global PC_COPY
    global AR_COPY
    

    global Memory
    global LABLES
    global MicroProgram
    global MicroProgramLables
    global RegisterState
    clock_counter = 0
    while(True):
        
        print("AC: " , AC)
        print("DR: " , DR)
        print("PC: " , PC)
        print("AR: " , AR)
        print("CAR: " , CAR)
        print("SBR: " , SBR)

        RegisterState["Clock" + str(clock_counter)] = [AC , DR, PC, AR, CAR, SBR]
        

        
        AC_COPY = AC
        DR_COPY = DR
        PC_COPY = PC
        AR_COPY = AR

        instruction = MicroProgram[CAR]
        
        print("instruction: " , instruction)

        if(instruction[0:9] == "000000111"):
            print("HALT")
            break

        F1_functions(instruction[0:3])
        F2_functions(instruction[3:6])
        F3_functions(instruction[6:9])

        AC = AC_COPY
        DR = DR_COPY
        PC = PC_COPY
        AR = AR_COPY


        if(instruction[9:11] == "00"):
            CD_FLAG = U_COND()
        elif(instruction[9:11] == "01"):
            CD_FLAG = I_COND()
        elif(instruction[9:11] == "10"):
            CD_FLAG = S_COND()
        elif(instruction[9:11] == "11"):
            CD_FLAG = Z_COND()
        

        if(instruction[11:13] == "00"):
            JMP(CD_FLAG , instruction[13:20])
        elif(instruction[11:13] == "01"):
            CALL(CD_FLAG , instruction[13:20])
        elif(instruction[11:13] == "10"):
            RET()
        elif(instruction[11:13] == "11"):
            MAP()

        clock_counter += 1
        
     



def MicroProgramm_Traversal():
    global MicroProgram
    global MicroProgramLables
    global CAR


    with open("MicroProgramm.txt" , 'r') as f:
        lines = f.readlines()
        
        for line in lines:# lbl: f1,f2,f3  cd br address
            if(line.isspace() == False):
                
                if(line.split()[0] == "ORG"):
                    CAR -= 1
                    CAR = int(line.split()[1])
                    CAR -= 1
                
                if(line.find(':') != -1):
                    lbl = line.split()[0][0:len(line.split()[0]) - 1]
                    MicroProgramLables[lbl] = CAR
            
                CAR += 1

        CAR = 0  
        for line in lines:
            splited_line = line.split()
            
            if(line.isspace() == False):
            
                if(splited_line[0] == "ORG"):
                    CAR -= 1
                    CAR = int(line.split()[1])
                    CAR -= 1

                elif(len(splited_line) > 1 and line.find(':') != -1):
                    
                    temp = ""
                    functions = splited_line[1].split(',')
                    if(len(functions)) == 1:
                        temp += CodeFunction("" , "" , functions[0] , F1)
                        temp += CodeFunction("" , "" ,functions[0] , F2)
                        temp += CodeFunction("" , "" ,functions[0] , F3)
                    elif(len(functions)) == 2:
                        temp += CodeFunction("" ,functions[0] , functions[1]  , F1)
                        temp += CodeFunction("" ,functions[0] , functions[1]  , F2)
                        temp += CodeFunction("" ,functions[0] , functions[1]  , F3)
                    else:
                        temp += CodeFunction(functions[0] , functions[1] , functions[2] , F1)
                        temp += CodeFunction(functions[0] , functions[1] , functions[2] , F2)
                        temp += CodeFunction(functions[0] , functions[1] , functions[2] , F3)

                    temp += CodeCondition(splited_line[2])
                    temp += CodeBranch(splited_line[3])
                    if(splited_line[4] == "NEXT"):
                        temp += bin(CAR + 1)[2:].zfill(7)
                    else:
                        temp += bin(MicroProgramLables[splited_line[4]])[2:].zfill(7)

                    MicroProgram[CAR] = temp

                elif(len(splited_line) > 1 and line.find(':') == -1):
                    
                    temp = ""
                    functions = splited_line[0].split(',')
                    if(len(functions)) == 1:
                        temp += CodeFunction("" , "" , functions[0] , F1)
                        temp += CodeFunction("" , "" ,functions[0] , F2)
                        temp += CodeFunction("" , "" ,functions[0] , F3)
                    elif(len(functions)) == 2:
                        temp += CodeFunction("" ,functions[0] , functions[1]  , F1)
                        temp += CodeFunction("" ,functions[0] , functions[1]  , F2)
                        temp += CodeFunction("" ,functions[0] , functions[1]  , F3)
                    else:
                        temp += CodeFunction(functions[0] , functions[1] , functions[2] , F1)
                        temp += CodeFunction(functions[0] , functions[1] , functions[2] , F2)
                        temp += CodeFunction(functions[0] , functions[1] , functions[2] , F3)

                    temp += CodeCondition(splited_line[1])
                    temp += CodeBranch(splited_line[2])
                    if(splited_line[2] == "RET" or splited_line[2] == "MAP"):
                        temp += "0000000"
                    elif(splited_line[3] == "NEXT"):
                        temp += bin(CAR + 1)[2:].zfill(7)
                    else:
                        temp += bin(MicroProgramLables[splited_line[3]])[2:].zfill(7)

                    MicroProgram[CAR] = temp
                
                CAR += 1


def Memory_Traversal():
    global Memory
    global LABLES
    global PC
    global MicroProgramLables
    global MicroProgram

    with open("PROGRAMM.txt" , 'r') as f:
        lines = f.readlines()
        PC = int(lines[0].split()[1] , 16)
        

        for line in lines[1:]:
            
            if(line.find(',') != -1):
                lbl = line.split()[0][0:len(line.split()[0]) - 1]
                LABLES[lbl] = PC

                if(line.split()[1] == "DEC"):
                    Memory[PC] = bin(int(line.split()[2]))[2:].zfill(16)
                elif(line.split()[1] == "HEX"):
                    Memory[PC] = bin(int(line.split()[2] , 16))[2:].zfill(16)

            PC += 1

        PC = int(lines[0].split()[1] , 16)
        for line in lines[1:] :
            
            splited_line = line.split()
            if(line.find("HALT") != -1):
                Memory[PC] = "1111111111111111"
                break
            elif(line.find(',') != -1 ):
                if('I' in splited_line != -1):
                    I = 1
                else:
                    I = 0

                opcode = bin(MicroProgramLables[splited_line[1]])[2:].zfill(7)[1:5]

                if(len(splited_line) > 2) : 
                    address = bin(LABLES[splited_line[2]])[2:].zfill(11)
                else:
                    address = '00000000000'

                temp = str(I) + str(opcode) + str(address)
            
                Memory[PC] = temp
            else:
                if('I' in splited_line != -1):
                    I = 1
                else:
                    I = 0
                opcode = (bin(MicroProgramLables[splited_line[0]])[2:].zfill(7))[1:5]
            
                if(len(splited_line) == 2 ):
                    address = bin(LABLES[splited_line[1]] )[2:].zfill(11)
                else:
                    address = '00000000000'

                temp = str(I) + str(opcode) + str(address)
    
                Memory[PC] = temp
            
            PC += 1 


Memory = dict() # address : decimal value
LABLES = dict() # lable : address 
MicroProgram = dict()
MicroProgramLables = dict()
RegisterState = dict()



def Execute_programm():
    global PC
    global CAR
    with open("PROGRAMM.txt" , 'r') as f:
        lines = f.readlines()
        PC = int(lines[0].split()[1] , 16)
        CAR = MicroProgramLables["FETCH"]

        ControlUnit()


def PrintReg():
    global RegisterState
    print(RegisterState)

def printMemory():
    global Memory
    print(Memory)



print("Memory: ",Memory)
print("LABLES: " , LABLES)
print("MicroProgram: " , MicroProgram)
print("MicroProgramLables: " , MicroProgramLables)
#print(RegisterState)