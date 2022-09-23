from tabulate import tabulate


def validate(transition,start_state,final_state,given_word):
        curr_state = start_state
        print(f'Checking validity for {given_word} \n')
        print(f'Start state -->{start_state} \n')
        print("State Transistion \n")
        print('******************************************************************************')
        for curr_char in given_word:
            if(curr_state, curr_char) not in transition.keys():
                curr_state = None                
            else:
                next_state = transition[(curr_state, curr_char)]
                print(f'With delta({curr_state},{curr_char}) going to state {next_state}')
                curr_state = next_state
        print('******************************************************************************')
        a = curr_state in final_state        
        return a 
    


def main():
    file = input("General Instruction : \n --------------------------------------------------------------------------- \n Firstly enter the path to your dfa file expression \n"+
                            
                            "General File instruction Format: \n"+
                            "--------------------------------------------------------------------------- \n"
                            "first line is number of state\n 2nd line is alphabets with space separator\n"
                            +" 3rd line is  start state\n 4th line is end state can be multiple so separated by comma(',') \n "+
                            "Finally transition table:\n"+
                            "\n"+
                            "********************************************************************************** \n"+
                            "Enter the path to dfa exp file :"
                        )

    with open(file ,"r") as file:


        num_of_states = int(file.readline())
        print('Number of states :', num_of_states)
        alphabet = file.readline().strip()
        print('Alphabet symbols :', alphabet)
        alphabet_list = alphabet.split()
        headers = alphabet.split()
        headers.insert(0,"state")
        start_state = file.readline().strip()
        print('Starting state: ', start_state)
        end_state = file.readline().strip(',')
        print('Ending states: ', end_state)
        print("Transition table:")
        delta_transition = {}
        delta_table = []

        for line in file:
            current_transition = line.strip()
            current_transition = current_transition.split()
            delta_table.append(current_transition)
            for i in range(len(alphabet_list)):
                delta_transition[tuple([current_transition[0], alphabet_list[i]])] = current_transition[i+1]
    
    print(tabulate(delta_table,headers=headers,tablefmt='fancy_grid') )


    given_word = None
    while True:
        given_word = input('Enter a word to check validity(click "ctrl + c" to exit): ')

        
        if validate(delta_transition, start_state, end_state,given_word):
            print("Accepting word \n")
        else:
            print("Invalid Word\n")


if __name__=="__main__":
    print("************Starting the program************")
    main()