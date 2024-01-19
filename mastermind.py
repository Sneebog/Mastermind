#get modules
import random 
import sys
from  pathlib import Path

# Get the number of arguements
num_args          = len(sys.argv)

#set default values for optional arguements
code_length       = 5
max_guess         = 12
colour_dictionary = []

#for a human game
if num_args > 2: #if there is enough arguements get the arguements
    valid_args  = True #indicate there were enough arguements
    #get the arguements
    input_file  = sys.argv[1]
    output_file = sys.argv[2]
    #get the optional arguements
    if num_args > 3:
        if type(sys.argv[3]) == str and sys.argv[3].isdigit(): #check the code length is valid
            code_length = int(sys.argv[3])
        else:
            print("invalid code length, defualt used")
        if num_args > 4:
            if type(sys.argv[4]) == str and sys.argv[4].isdigit(): #check the maximum guesses is valid
                max_guess   = int(sys.argv[4])
            else:
                print("invalid maximum guesses, default used")
            if num_args > 5:
                for i in range(5, num_args): #get the colours ensuring they are strings
                    if type(sys.argv[i]) == str:
                        colour_dictionary.append(sys.argv[i])
else:
    valid_args = False #there were not enough arguements

#create default colour dictionary if a dictionary doesn't yet exist
if colour_dictionary == []:
    colour_dictionary = ["red", "blue", "yellow", "green", "orange"]

#make a dictionary of the error codes
error_dictionary = ["The programme ran successfully",
                     "Not enough programme arguments provided",
                      "There was an issue with the input file",
                      "There was an issue with the output file",
                      "No or ill-formed code provided",
                      "No or ill-formed player provided",]

#create the functions
def generateguess(): #create a random guess
    code = ""
    for i in range(0, code_length): #for the number of different pins
        colour_num = random.randint(0, code_length) # for the random colours
        code += colour_dictionary[colour_num] + " "
    return code

def valid(code): #check there is valid guess / code
    if len(code) == code_length: #valid length
        valid = True
        for colour in code:
            if colour not in colour_dictionary: #valid colours
                valid = False
    else:
        valid = False

    return valid #return boolean 

def valid_file(file):
    #check the file has a valid path
    path = Path(file)
    return path.is_file()

        
def give_feedback(code, guess): #gets the feedback from a guess   

    if valid(guess): #ensure guess is valid
        colour_pins = [""] * len(guess)#make colour pins list
        colour_set  = [] #to ensure a white peg cant get assigned if colour is already assigned

        #for black pegs
        for i in range(len(guess)):#loop through the guesses
            if code[i] == guess[i]: #if the guess is the right colour in right position
                colour_pins[i] = "black"
                colour         = code[i]
                colour_set.append(colour) #add colour to the set

        #for white pegs
        for i in range(len(guess)):#loop through the guesses
            for j in range(len(code)):
                if code[j] == guess[i] and colour_pins[j] == "" and not (code[j] in colour_set): #if the guess is the right colour wrong position
                        colour_pins[j] = "white"
                        colour_set.append(code[j]) #add colour to the set

        colour_pins.sort() # sort so it returns in order of black and white
        return colour_pins # return pegs
    else:
        return "Ill-formed guess provided" #invalid guess

def guess(code, mode, guessarray = None): #the main guessing function that prints the guesses, feedback and end statements
    guess_num = 0
    solved    = False #flag to check if the code has been solved
    file      = open(output_file, "w") #open the outputfile to write to
    #open new file if computer is playing 
    if mode == "computer":
        comp_file = open("computerGame.txt", "w")
    while guess_num != max_guess and not solved: #loop until the maximum guesses are reached and until it is solved
        guess_num += 1 #increment the guess number 

        #get the guess
        if mode == "human":
            if guess_num < len(guessarray) + 1:
                guess_string = guessarray[guess_num - 1] #take it from the input file
            else:
                break #break loop if no more guesses in file 
        elif mode == "computer":
            guess_string = generateguess() #create random guess for computer
            comp_file.write(guess_string + "\n") #write it to the file 
        
        guess    = guess_string.split() #convert guess to array of colours
        feedback = give_feedback(code, guess) #get the feedback from the guess

        #turn feedback into a string to be printed
        if len(feedback) == code_length:
            feedbackstring = [peg for peg in feedback if peg != ""]
            feedbackstring = " ".join(feedbackstring)
        else:
            feedbackstring = feedback #if it is an invalid guess

        #write the guess to the outputfile
        text = "Guess " + str(guess_num) + ": " + feedbackstring + "\n"
        file.write(text)
        
        #check if the code has been solved
        if all(peg == "black" for peg in feedback):
            solved = True

    #return end statements
    if solved: #if the games is won
        file.write("You won in " + str(guess_num) + " guesses. Congratulations!\n")
        if guess_num < len(guessarray): #if the game was completed with more guesses remaining
            file.write("The game was completed. Further lines were ignored.\n")
    else: #the game has been lost
        file.write("You lost. Please try again.\n")
        if guess_num == max_guess: # if the max guesses caused the loss
            file.write("You can only have " + str(max_guess) + " guesses.\n")

    #close the files
    if mode =="computer":
        comp_file.close()
    file.close() 

def readfile(file): #code for reading the file
    inputfile = open(file, "r" ) #opens the file
    lines     = [line.strip() for line in inputfile.readlines()] #converts it into lines
    return lines
   
def mastermind(): #main mastermind function that checks everything is valid and then runs the game
    if valid_args: #check there a valid number of arguements
        #check if the input file is valid
        if valid_file(input_file): 
            lines = readfile(input_file) #get the lines of the input file 
            if len(lines) >= 2:
                #check the outputfile is valid
                if valid_file(output_file): 
                    #get the code and the mode from the input file
                    code_string,mode_string = lines[0], lines[1]
                    code, mode              = code_string.split(), mode_string.split()
                    if code[0] == "code" and valid(code[1:]): #check if the code is valid 
                        code = code[1:] #get only the colours of the code
                        if len(mode) == 2 and mode[0] == "player" and (mode[1] == "human" or mode[1] == "computer"): #check if the mode is valid
                            guess_lines = lines[2:] #get the guesses
                            guess(code, mode[1], guess_lines) #run the mastermind game
                            return 0 #The programme ran successfully
                        else:
                            return 5 #No or ill-formed player provided
                    else:
                        return 4#No or ill-formed code provided 
                else:
                    return 2#There was an issue with the output file 
            else:
                return 2 #There was an issue with the input file 
        else:
            return 2 #There was an issue with the input file       
    else:
        return 1 #Not enough programme arguments provided


#call the mastermind function
exit_code = mastermind()
#write the exit code
print(str(exit_code)+ ": " + error_dictionary[exit_code]) 
if exit_code > 3: #if there is an output file write the exit code to it
    file = open(output_file, "w")
    file.write(error_dictionary[exit_code])
    file.close()