from  typing import *


def printans(arr:List)->None:
    for ans in arr:
        print(ans)

def driver(directory:str)->None:

    with open(directory,'r') as file:
        s = file.readline()
        # E->E+T/T
    f = s[0]
    other = s[3:]
    a =  []
    beta =[]
    li = other.strip('\n').split('|')
    beta_count=0
    for st in li:
        
        if f == st[0]:
            a.append(st[1:])
        else:
            beta_count += 1 
            beta.append(st)

    part1 = ""
    part2 =" "

    final_answer = []


    for i in range(len(a)):
        fd = f+"'"
        part1 = f + "->" + beta[i] + fd    
        part2 = fd+"->"+a[i]+fd+"|Epshila"
        final_answer.append(part1)
        final_answer.append(part2)
        printans(final_answer)


if __name__ == "__main__":
    directory = input("Please provide location of text-file with grammar \n")
    driver(directory)
    
    


