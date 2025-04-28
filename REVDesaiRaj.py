'''
Name: Raj Desai
Date: April 28, 2025
Module: 03REV- Review Python Fundamentals
Description: I am developing Vowel counter program. The user is asked to enter a sentence. Once the user enters a sentence, the program will run to scan for all vowels (a,e,i,o,u). For every vowel found in the sentence, it will increase the vowel count +1. In the end, the program will display the total number of vowels in the sentence.
'''

# Constants
TITLE = "Welcome to vowel counter program!"
PROMPT = "Enter any text: "
LINE = '-'

def main():
    print(TITLE)
    print(LINE * len(TITLE))
    
    text = input(PROMPT).upper()
    
    vDict, total = findVowelCount(text)
    
    generateReport(vDict, total)

def findVowelCount(text):
    vDict = {'A':0, 'E':0, 'I':0, 'O':0, 'U':0}
    total = 0

    for character in text:
        if character in vDict:
            vDict[character] += 1
            total += 1

    return vDict, total

def generateReport(vDict, total):

    print()
    print("VOWEL COUNT REPORT:")
    print("--------------------")
    print("Vowel          Count")
    print("--------------------")
    
    for vowel, count in vDict.items():
        print(vowel,"               ", count)
    print("--------------------")
    print("Total            ",total)
    print("--------------------")
    

# Call main function
main()