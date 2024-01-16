import random 

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

def get_guess(guessstring):
    guess = guessstring.split() #turn the guesses into an array
    return guess

def give_feedback(code, guess):
    if len(code) == len(guess):
        colour_pins = [""] * len(guess)#make colour pins list
        colour_set  = []
        for i in range(len(guess)):#loop through the guesses
            if code[i] == guess[i]: #if the guess is the right colour in right position
                colour_pins[i] = "black"
                colour = code[i]
                colour_set.append(colour)

        for i in range(len(guess)):#loop through the guesses
            for j in range(len(code)):
                #if colour_pins[j] == "":
                    #white_flag = False #to ensure it doesnt make two white for one colour
                if code[j] == guess[i] and colour_pins[j] == "" and not (code[j] in colour_set): #if the guess is the right colour wrong position
                        colour_pins[j] = "white"
                        colour_set.append(code[j])

        colour_pins.sort() # sort so it returns in order of black and white
        colour_pins = " ".join(colour_pins) #turn it back into a string
        return colour_pins # return in 
    else:
        return " ill-formed guess provided"

def guess(code, mode, guessarray = None,  max_guess = 10): #the main guessing function 
    guess_num = 0
    solved = False
    outputfile = open("outputexample", "w")
    while guess_num != max_guess and not solved: #loop until the maximum guesses are reached and until it is solved
        guess_num += 1 #increment the guess number 
        if mode == "test":
            guess = input("Enter Guess: ")
            print("")
        elif mode == "human":
            guess = guessarray[guess_num - 1]
        #elif mode == "computer"
        #   computer(code, feedback)
        feedback = give_feedback(code, get_guess(guess)) #get the feedback from the guess
        if mode == "test":
            print("Guess ", guess_num, ":", feedback) #print the feedback
        else:
            text = "Guess " + str(guess_num) + ":" + str(feedback) + "\n"
            outputfile.write(text)
        feedback = feedback.split() 
        if len(feedback) == len(code): #check if the feedback is the same length as the the code (Each peg is correct)
            feedback_flag = True #use flag to check each peg is correct 
            for peg in feedback: #check that each peg is a black peg
                if peg != "black":
                    feedback_flag = False
            if feedback_flag:
                solved = True #set to solved to end the loop
    if mode == "test":
        if solved: #return end statements
            print("You won in ", guess_num, " guesses. Congratulations!")
        else:
            print("You lost the code was:", code)
        print("The game was completed. Further lines were ignored.")
    else:
        if solved: #return end statements
            outputfile.write("You won in " + str(guess_num) + " guesses. Congratulations!\n")
        else:
            outputfile.write("You lost the code was:" + str(code) + "\n")
        outputfile.write("The game was completed. Further lines were ignored.\n")
    outputfile.close()
code = generatecode()
codearray = code.split()
#print(code)
#guess(10, codearray)



print(give_feedback(["r","b", "o", "g"], ["p", "b", "g", "g"]))

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


mastermind(readfile("inputexample1.txt"))
