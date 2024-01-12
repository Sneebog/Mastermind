import random 

def generatecode():
    code = ""
    for i in range(4):
        colornum = random(0, 5)
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
    guess = guessstring.split()
    return guess

# def give_feedback(code, guess):
#     colourpins = [""] * len(code) #make colour pins list
#     for i in range(len(code)): #loop through the guesses
#         if code[i] == guess[i]: #if the guess is the right colour in right position 
#             colourpins[i] = "black"
#         else:
#             for j in range(0, len(code)): 
#                 if code[j] == guess[i] and colourpins[i] == "" :
#                         colourpins[i] = "white"
#                         break
                    
#     #colourpins.sort() # sort so it returns in order of black and white
#     return colourpins

# print(give_feedback(["o", "g", "r"], ["gr", "o", "o"]))
                
def give_feedback(code, guess):
    colour_pins = [""] * len(guess)#make colour pins list

    for i in range(len(guess)):#loop through the guesses
        if code[i] == guess[i]: #if the guess is the right colour in right position
            colour_pins[i] = "black"

    for i in range(len(guess)):#loop through the guesses
        if colour_pins[i] == "":
            white_flag = False #to ensure it doesnt make two white for one colour
            for j in range(len(code)):
                if code[j] == guess[i] and colour_pins[j] == "" and not white_flag: #if the guess is the right colour wrong position
                    colour_pins[j] = "white"
                    white_flag = True
    colour_pins.sort() # sort so it returns in order of black and white
    colour_pins = "".join(colour_pins)
    return colour_pins

print(give_feedback(["o", "g", "r"], ["gr", "o", "o"]))


