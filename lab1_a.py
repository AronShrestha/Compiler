import keyword


import keyword
from re import L
from symtable import symtable
class Lexical:
    def __init__(self,filePath) -> None:
        self.file = open(filePath,'r')
        self.__specialfunctions=['range','open','print']
        self.__specialCharacters=[',','[',']','(',')',':','.','?','{','}']
        self.__is_operators=['+','-','*','/','>','<','=']
        self.__numbers=['0','1','2','3','4','5','6','7','8','9']
        self.symbolTable = []
        self.symbolTable_dic={}
    
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
        if language_string[0]  in self.__numbers or language_string[0] in self.__specialCharacters or language_string[0] in self.__is_operators or language_string in self.__specialfunctions:
            return False
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
        
a=Lexical('file.py')
a.scan()
a.show_symbolTable()

    