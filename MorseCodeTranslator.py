# Created by Rebecca C
# Works with upper and lower case,
# Improve by adding while loop instead of stopping
# allow it to take dashes - and underscores _ as some may use interchangably
# code improve output by separating words differently than letters
# work with American and International morse code
# improve efficiency of morse to english

# morse dictionary
morseDictionary = {"A": ".-",
                   "B": "-...",
                   "C": "-.-.",
                   "D": "-..",
                   "E": ".",
                   "F": "..-.",
                   "G": "--.",
                   "H": "....",
                   "I": "..",
                   "J": ".---",
                   "K": "-.-",
                   "L": ".-..",
                   "M": "--",
                   "N": "-.",
                   "O": "---",
                   "P": ".--.",
                   "Q": "--.-",
                   "R": ".-.",
                   "S": "...",
                   "T": "-",
                   "U": "..-",
                   "V": "...-",
                   "W": ".--",
                   "X": "-..-",
                   "Y": "-.--",
                   "Z": "--..",
                   "1": ".----",
                   "2": "..---",
                   "3": "...--",
                   "4": "....-",
                   "5": ".....",
                   "6": "-....",
                   "7": "--...",
                   "8": "---..",
                   "9": "----.",
                   "0": "-----", }

# function to handle english to morse translation
def englishToMorse():
    print("Input English Sequence, letters need to be separated by spaces: ")
    translateString = ''
    userInput = input().upper()
    for letter in userInput.split():
        translateString = translateString + ' ' + morseDictionary[letter]
    print(translateString)

# function to handlt morse to english translation
def morseToEnglish():
    print("Input Morse Code Sequence using dots(.) and dashes(-) letters need to be separated by spaces: ")
    translateString = ''
    userInput = input()
    for letter in userInput.split():
        for key, value in morseDictionary.items():
            if letter == value:
                translateString = translateString + " " + key
    print(translateString)


# actual working code
translateOption = '1'
#while(translateOption != '1'or translateOption != '2'):
print("OPTIONS: \n1. MORSE TO ENGLISH \n2. ENGLISH TO MORSE \n")
translateOption = input("Your Choice: ")

print("see mee!!!")
if translateOption == '1':
    morseToEnglish()
elif translateOption == '2':
    englishToMorse()
else:
    print("invalid input, please restart and try again")




