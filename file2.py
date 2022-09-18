from ast import operator
import keyword


        # lines = self.file.readlines()
        # for line in lines:
        #     buffer = ""
        #     self.leximBegin = 0
        #     self.forward =0
        #     index =0
        #     while index < len(line):
        #         if line[index]==" " or line[index] in self.__specialCharacters:
        #             self.leximBegin=index+1
        #             if  buffer in self.__is_operators:
        #                 print(f"{buffer} : Operator")
        #             elif buffer in self.__specialCharacters:
        #                 print(f"{buffer} : Special Character")
        #             # elif self.is_identifier(buffer):
        #             #     print(f"{buffer} : Identifier")
        #             elif self.is_keyword(buffer):
        #                 print(f"{buffer} : Keyword")
        #             elif buffer in self.__numbers:
        #                 print(f"{buffer} : Number")
                    
        #             if line[index] in self.__specialCharacters:
                        
        #                 print(f"{line[index]} : Special Character")
        #         if line[index] in self.__is_operators:
        #                 temp = line[index]
        #                 while temp in self.__is_operators:
        #                     index+=1
        #                     temp += line[index]
        #                 print(f"{temp} : Special Character")


                    
                
        #         self.forward+=1
        #         buffer=line[self.leximBegin:self.forward]
        #         index+=1

import keyword
from re import L
from symtable import symtable
class Lexical:
    def __init__(self,filePath) -> None:
        self.file = open(filePath,'r')
        self.__specialfunctions=['open','print']
        self.__specialCharacters=[',','[',']','(',')',':','.','?','{','}']
        self.__is_operators=['+','-','*','/','>','<','=']
        self.__numbers=['0','1','2','3','4','5','6','7','8','9']
        self.symbolTable = []
        self.symbolTable_dic={}
        self.buffer_symbol_table=[]
        self.ans= []

    
    def scanner(self):

        lines = self.file.readlines()
        
        for line in lines:
            buffer = []
            # print(f"tokens so far {self.ans}")
            
            leximBegin = 0
            forward =0
            index =0
            while index < len(line):
                buffer.append(line[index])
                if line[index]=='\n':
                    index+=1
                    continue
                if line[index] in self.__is_operators:
                    if line[leximBegin:forward] != ' ' and line[leximBegin:forward] !='':
                        self.ans.append(line[leximBegin:forward])
                    temp = line[forward]
                    leximBegin=forward

                    while True:
                        forward+=1
                        temp+=line[forward]
                        if temp in self.__is_operators:
                            
                            
                            index = forward
                        else:
                            break
                    
                    if leximBegin<forward:
                        if line[leximBegin:forward] != ' ' and line[leximBegin:forward] != '':
                            self.ans.append(line[leximBegin:forward])
                        leximBegin = forward
                    # else:
                    #     ans.append(line[forward])
                    #     leximBegin = forward
                        
                    forward=index
                
              

                if line[index] == " ":
                    if line[leximBegin:forward] != ' ' and line[leximBegin:forward] != '':
                        self.ans.append(line[leximBegin:forward])
                    temp = line[forward]
                    leximBegin=forward
                    while True:
                        forward+=1
                        temp+=line[forward]
                        if temp == " ":
                            
                            
                            index = forward
                        else:
                            break   
                    if leximBegin<forward:
                        if leximBegin<forward:
                            if line[leximBegin:forward] != ' ' and line[leximBegin:forward] != '':
                                self.ans.append(line[leximBegin:forward])
                            leximBegin = forward
                        else:
                            if line[leximBegin:forward] != ' ' and line[leximBegin:forward] !='':
                                self.ans.append(line[forward])
                            leximBegin = forward
                        
                    forward=index

                if line[index] in self.__specialCharacters:
                    if line[leximBegin:forward] != ' ' and line[leximBegin:forward] !='':
                        self.ans.append(line[leximBegin:forward])
                
                    if line[leximBegin:forward] != ' ' and line[leximBegin:forward] !='':
                        self.ans.append(line[forward])
                    forward+=1
                    leximBegin = forward
                    index = forward

                index+=1
                forward = index

                    # try:
                    #     buffer+=line[leximBegin:forward]
                    #     print(line,leximBegin,forward)
                    #     print(f"{buffer} :  back")
                    #     leximBegin = forward
                    #     buffer = ''
                    # except:
                    #     print("SOrry ")
                    # operator = line[forward]
                    # temp = index
                    # while True:
                    #     temp+=1
                    #     operator+= line[temp]
                    #     if operator in self.__is_operators:
                    #         index=temp
                    #     else:
                    #         break
                    # print(f"{buffer} : Buffer After")

                    


                
                # if line[index] == " ":

                #     try:
                #         buffer+=line[leximBegin:forward]
                #         print(f"{buffer} :  back")
                #         leximBegin = forward
                #         buffer = ''
                #     except:
                #         print("SOrry ")
                # index+=1
                # forward = index
                

 


         
            
            
        
    def name(self, language,type):

    
        operator={
                '+' : "Addition Operator",
                '-': "Subtraction Operator",
                '*': "Multiplication Operator",
                '/' : "Division Operator",
                '>' : "Greater-than Operator",
                '<' : "Less-than Operator",
                '=' : "Assignment Operator",
                '+=' : "Assignment Operator",
                '-=':"Assignment Operator",
                '*=':"Assignment Operator",
                "/=" : "Assignment Operator",
                '==' : "Compaision Operator"
        }
        if type.lower() == "operator":
          
            return operator[language]


    def is_keyword(self,language_string):
        
            if keyword.iskeyword(language_string):
                return True
            else:
                return False
    
    def is_identifier(self, language_string):
   
        # try:
        if language_string[0]  in self.__numbers or language_string[0] in self.__specialCharacters or language_string[0] in self.__is_operators or language_string in self.__specialfunctions:
        
                return False
        # except:
        else:
            return True

    def is_operator(self,language_string):
          
                
        if language_string not in self.__is_operators:
                    return False
        return True

    def is_number(self,language_string):
        for i in range(len(language_string)):
            
            if language_string[i] not in self.__numbers:
                return False
        return True
    
    def scan(self):
        language = self.file.readlines()
        li=[]
        l=[]
        for i in range(len(language)):
            st=str(language[i])
            stf=""
            for i in st:
                if  i=="\n":
                    continue
                else:
                    stf+=i
                    li.append(i)
            l.append(stf)
        s=[]
        t=[]
        special=[]
        for i in range(len(l)):
            sub=""
            left = 1

            for j in l[i]:
            
                if j!=" " and j not in self.__specialCharacters :
                    sub+=j

                    
                else:
                    if j in self.__specialCharacters:
                        special.append(j)
                    if sub!='':
                        t.append(sub)
                    sub=""

                    continue
            if sub!='':
                t.append(sub)
            s.append(sub)


        for i in t:
            # print(i)
            if  self.is_keyword(i):
                self.symbolTable.append((i,"Keyword"))
            elif self.is_identifier(i):
                self.symbolTable.append((i,"Identifier"))

            elif self.is_number(i):
                self.symbolTable.append((i,"Number"))


        for i in special:
            self.symbolTable.append((i,"Special Characters"))
        


     

        for i in t:
            # print(i)
            if  self.is_keyword(i):
                self.symbolTable_dic[i]="Keyword"
            elif self.is_identifier(i):
                self.symbolTable_dic[i]="Identifier"

            elif self.is_number(i):
                self.symbolTable_dic[i]="Number"
            elif self.is_operator(i):
              
                self.symbolTable_dic[i] = self.name(language=i,type="operator")
        for i in special:
            self.symbolTable_dic[i]="Special Characters"





    
    def show_symbolTable(self):
        # for key,value in self.symbolTable_dic.items():
        #     print(f"{key} : {value}")
        for i,j in self.symbolTable:
            print(f"<{i} : {j}>")

    def show_bufferSymbolTable(self):
        # a=self.buffer_symbol_table
        # for key,value in self.symbolTable_dic.items():
        #     print(f"{key} : {value}")
        print(self.ans)
        for i in self.ans:
            # print(i)
            if  self.is_keyword(i):
               
                self.buffer_symbol_table.append((i,"Keyword"))
                # a.append((i,"Keyword"))
            elif self.is_identifier(i):
                self.buffer_symbol_table.append((i,"Identifier"))

            elif self.is_number(i):
                self.buffer_symbol_table.append((i,"Number"))
                # a.append((i,"Number"))
            elif self.is_operator(i):
                self.buffer_symbol_table.append((i,"Operator"))
                
            elif i in self.__specialCharacters:
                self.buffer_symbol_table.append((i,"Special Character"))
                
            # else:
            #     self.show_bufferSymbolTable.append((i,"Identifier"))
            #     a.append((i,"Identifier"))
        
        for i,j in self.buffer_symbol_table:
            print(f"<{i} : {j}>")


a=Lexical('file.py')
a.scanner()
a.show_bufferSymbolTable()
print(a.ans)
# print(a.ans)
# a.show_symbolTable()

    