# A very handy tool to change between lower case and upper case letters, or convert to mix case and transform your text.

import pandas as pd

print("Welcome user!")
print("Accidentally left the caps lock on and typed something, but can't be bothered to start again and retype it all?")
print("Well, simply enter your text and choose the case you want to convert to!")


def print_options():
    print(" ")
    print(f"You've given the sentence: {sentence}")
    print(" ")
    print("Please choose one of the following options: ")
    print("1. Change case to UPPER CASE")
    print("2. Change case to lower case")
    print("3. Change case to AlTeRnAtInGcAsE")
    print("4. Change case to Title Case")
    print("5. Give the character count")
    print("6. Give the char. count of a certain letter")
    print("7. Give the number of unique characters")
    print(" ")
    print("8. Re-enter the sentence")


def alternating_case(text):
    mytext = ''
    for i in range(len(text)):
        if not i % 2:
            mytext = mytext + text[i].upper()
        else:
            mytext = mytext + text[i].lower()
    return mytext


def capitalised_case(text):
    split_text = text.split()
    text_list = []
    new_text = ' '
    for i in split_text:
        text_list.append(i[0].upper() + i[1:])
    new_text = new_text.join(text_list)
    return new_text


def inverse_case(text):
    mytext = ''
    for i in text:
        if i.isupper():
            mytext = mytext + i.lower()
        else:
            mytext = mytext + i.upper()
    return mytext


def character_count(text, letter):
    lettercount = []
    for i in text:
        if i == letter:
            lettercount.append(letter)
    return len(lettercount)


def unique_character_count(text):
    templist = []
    for i in text:
        if i not in templist:
            templist.append(i)
    return len(templist)


def restart_app():
    resp = input("Do you want to continue? Say Yes or No: ").upper()
    if resp in ['YES', 'Y']:
        return True


def ask_save(rslt):
    resp2 = input("Do you want to copy the results to your clipboard?: ").upper()
    if resp2 in ['YES', 'Y']:
        df = pd.DataFrame([rslt])
        df.to_clipboard(index=False, header=False)
        print("Copied the result to your clipboard!")


while True:
    program_on = True
    while program_on:
        sentence = input("Please enter the sentence: ")
        print_options()
        response = ''
        while response not in [1, 2, 3, 4, 5, 6, 7, 8]:
            response = int(input("Enter your choice: "))
        if response == 1:
            result = sentence.upper()
            print(result)
            ask_save(result)
            program_on = False
        elif response == 2:
            result = sentence.lower()
            print(result)
            ask_save(result)
            program_on = False
        elif response == 3:
            result = alternating_case(sentence)
            print(result)
            ask_save(result)
            program_on = False
        elif response == 4:
            result = capitalised_case(sentence)
            print(result)
            ask_save(result)
            program_on = False
        elif response == 5:
            result = len(sentence)
            print(f"There are {result} characters(including spaces) in the given sentence.")
            ask_save(result)
            program_on = False
        elif response == 6:
            character = input("Please enter the letter: ")
            result = character_count(sentence, character)
            print(f"There are {result} {character}'s in the given sentence.")
            ask_save(result)
            program_on = False
        elif response == 7:
            result = unique_character_count(sentence)
            print(f"There are {result} unique characters in the given sentence.")
            ask_save(result)
            program_on = False
        elif response == 8:
            program_on = True
    if not restart_app():
        print(" ")
        print("-----------------------")
        print("Thanks for using this app! Hit me up on Discord: mightykiller#9119")
        print("-----------------------")
        break
