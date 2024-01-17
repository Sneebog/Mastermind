import random 
import sys

# #For a human game
# inputfile  = sys.argv[1]
# outputfile = sys.argv[2]
# codelength = sys.argv[3]
codelength = 3
#colour dictionary 
colour_dictionary = ["red", "blue", "yellow", "green", "orange"]

def generatecode(): #create a random code
    code = ""
    for i in range(4): #for the number of different pins
        colornum = random.randint(0, 5) # for the random colours
        if colornum == 0:
            code += "red "
        elif colornum == 1:
            code += "blue "
        elif colornum == 2:
            code += "green "
        elif colornum == 3:
            code += "yellow "
        elif colornum == 4: 
            code += "white "
        else:
            code += "purple "
    return code

def valid(code):
    #check there is valid guesses 
    if len(code) == codelength: #valid length
        valid = True
        for colour in code:
            if not (colour in colour_dictionary ):
                valid = False
    else:
        valid= False

    return valid

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
        #elif mode == "computer"
        #   computer(code, feedback)
        guess = guess_string.split()
        feedback = give_feedback(code, guess) #get the feedback from the guess
        if len(feedback) == codelength:
            feedbackstring = [peg for peg in feedback if peg != ""]
            feedbackstring = " ".join(feedbackstring)
        else:
            feedbackstring = feedback
        if mode == "test":
            print("Guess ", guess_num, ": ", feedbackstring) #print the feedback
        else:
            text = "Guess " + str(guess_num) + ": " + feedbackstring + "\n"
            file.write(text)
        

        if all(peg == "black" for peg in feedback):
            solved = True

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



print(give_feedback(["blue","red", "orange"], ["red", "orange", "orange"]))

#code for opening files and outputting them

def readfile(file):
    inputfile = open(file, "r" ) #opens the file
    filearray = []
    while True:
        text = inputfile.readline() #reads a line of the file
        if text == "": #end of file
            break
        else:
            filearray.append(text.strip()) #adds the line of text to the array and removes the newline
    inputfile.close() #closes the file
    return filearray 


def mastermind(filearray):
    codestring,modestring = filearray[0], filearray[1]
    code, mode = codestring.split(), modestring.split()
    if code[0] == "code" and mode[0] == "player":
        code = code[1:]
        mode = mode[1]
        guessarray = filearray[2:]     
        guess(code, mode, guessarray)
    else:
        print("")

mastermind(readfile("inputexample1.txt"))
