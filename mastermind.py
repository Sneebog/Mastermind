import random 
import sys

# #For a human game
# num_args = len(sys.argv)
# if num_args >= 3: 
#     valid_args = True  
#     input_file  = sys.argv[1]
#     output_file = sys.argv[2]
#     code_length = sys.argv[3]
# else:
#     valid_args = False
codelength = 3
#colour dictionary 
colour_dictionary = ["red", "blue", "yellow", "green", "orange"]


def generateguess(): #create a random code
    code = ""
    for i in range(0, codelength): #for the number of different pins
        colour_num = random.randint(0, codelength) # for the random colours
        code += colour_dictionary[colour_num] + " "
    code = code.split()
    return code

def valid(code):
    #check there is valid guesses 
    if len(code) == codelength: #valid length
        valid = True
        for colour in code:
            if not (colour in colour_dictionary ):
                valid = False
    else:
        valid = False
    return valid

def valid_file(lines):
    #check the inputfile is valid
    if len(lines) > 2:
        codestring,modestring = lines[0], lines[1]
        code, mode = codestring.split(), modestring.split()
        if code[0] == "code" and mode[0] == "player":
            return True, code, mode
        else:
            return False, [], []
    else:
        return False, [], []

        
def give_feedback(code, guess):         
    if valid(guess):
        colour_pins = [""] * len(guess)#make colour pins list
        colour_set  = [] #to ensure a white peg cant get assigned if colour is already assigned
        for i in range(len(guess)):#loop through the guesses
            if code[i] == guess[i]: #if the guess is the right colour in right position
                colour_pins[i] = "black"
                colour = code[i]
                colour_set.append(colour)

        for i in range(len(guess)):#loop through the guesses
            for j in range(len(code)):
                if code[j] == guess[i] and colour_pins[j] == "" and not (code[j] in colour_set): #if the guess is the right colour wrong position
                        colour_pins[j] = "white"
                        colour_set.append(code[j])

        colour_pins.sort() # sort so it returns in order of black and white
        #colour_pins = " ".join(colour_pins) #turn it back into a string
        return colour_pins # return in 
    else:
        return "ill-formed guess provided"

def guess(code, mode, guessarray = None,  max_guess = 12): #the main guessing function 
    guess_num = 0
    solved = False
    file = open("outputfile", "w")
    while guess_num != max_guess and not solved: #loop until the maximum guesses are reached and until it is solved
        guess_num += 1 #increment the guess number 
        if mode == "test":
            guess_string = input("Enter Guess: ")
            print("")
        elif mode == "human":
            if guess_num < len(guessarray):
                guess_string = guessarray[guess_num - 1]
            else:
                break
        elif mode == "computer":
          #computer(code, feedback)
            guess_string = generateguess()
        guess = guess_string.split()
        feedback = give_feedback(code, guess) #get the feedback from the guess
        if len(feedback) == codelength:
            feedbackstring = [peg for peg in feedback if peg != ""]
            feedbackstring = " ".join(feedbackstring)
        else:
            feedbackstring = feedback
        if mode == "test":
            print("Guess ", guess_num, ":", feedbackstring) #print the feedback
        else:
            text = "Guess " + str(guess_num) + ": " + feedbackstring + "\n"
            file.write(text)
        
        #check if the code has been solved
        if all(peg == "black" for peg in feedback):
            solved = True

    #return end statements
    if mode == "test":
        if solved: #return end statements
            print("You won in ", guess_num, " guesses. Congratulations!")
        else:
            print("You lost the code was:", code)
        print("The game was completed. Further lines were ignored.")
    else:
        if solved: #return end statements
            file.write("You won in " + str(guess_num) + " guesses. Congratulations!\n")
        else:
            file.write("You lost the code was: " + " ".join(code) + "\n")
        file.write("The game was completed. Further lines were ignored.\n")
    file.close()

#code for reading the file
def readfile(file):
    inputfile = open(file, "r" ) #opens the file
    lines = [line.strip() for line in inputfile.readlines()]
    return lines
   
def mastermind(lines):
    is_valid, code, mode = valid_file(lines)
    if is_valid:
        code = code[1:]
        if valid(code):
            if len(mode) == 2 and (mode[1] == "human" or mode[1] == "computer"):
                guess_lines = lines[2:]
                guess(code, mode[1], guess_lines)
                return 0 #The programme ran successfully
            else:
                return 5 #No or ill-formed player provided")
        else:
            return 4 #No or ill-formed code provided"
    else:
        return 2 #There was an issue with the input file       
    

#print(give_feedback(["blue","red", "orange"], ["red", "orange", "orange"]))
print(mastermind(readfile("inputexample1.txt")))
#print(colour_dictionary)
#guess(generateguess(), "test" )
# if valid_args:
#     lines = readfile(input_file)
#     print(mastermind(lines))
# else:
#     print(1) 