
def takeREAndString(input_string,regularExpression,operations):
    n = len(input_string)
    m = len(regularExpression)

    def validate(i, j):
    
        if j == m:
            return i == n
        if i < n and (input_string[i] == regularExpression[j] or regularExpression[j] in operations):
            identical =True
        else:
            identical =  False

        if j + 1 < m and regularExpression[j + 1] in operations:
            return validate(i, j + 2) or (identical and validate(i + 1, j))
        return identical and validate(i + 1, j + 1)

    return validate(0, 0)




def starter():
    regularExpression = input("Enter the Regular Expression: ")
    n = int(input("Enter the number of string to check"))
    operations = ["*","+"]
    for i in range(n):
        input_string = input("Enter required string ")
        output = takeREAndString(input_string,regularExpression,operations)
        if output:
            print(f"For the regular expression {regularExpression} , given string {input_string} is valid")
        else:
             print(f"For the regular expression {regularExpression} , given string {input_string} is invalid")


if __name__=="__main__":
    print("************Starting the program************")
    starter()