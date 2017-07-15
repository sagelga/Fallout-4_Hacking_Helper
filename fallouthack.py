import math
import os
import tkinter
import os.path

# Global Configurations
debug_mode = True               # Starts the program with logging mode (All)
debug_mode_basic = True         # Starts the program with logging mode (Unstable features)

cache_file_name = "cache.txt"
cache_delete = True             # Allow program to delete cache file
cache_create = True             # Allow program to create cache file


def main(): """Served as function caller and receptions"""
    count, results, error_code = 1, [], 0

    while 1:
        screen_clear()
        result_printer(results, "Vocabulary Lists")
        if error_code == 1:
            print("'%s' is not a valid text length. (expecting: %d) Please try again..."%(text, len(text[count-1])))
        if error_code == 2:
            print("Please type something to start a program.")
        text = input("Please type in possible password #%-2d : "%count)

        if text.isalpha():
            if count != 1:
                if len(text) != len(results[0]):
                    error_code = 1
                    continue
            results.append(text.upper())
            count += 1
            error_code = 0
        elif text != "":
            command_center(results)
        else:
            if len(results) < 1:
                error_code = 2
                continue
            else:
                error_code = 0
                screen_clear()
                break

    print("Done recieving more vocabulary...\nSaving...\n")
    file_save(results)

    while 1:
        if len(results) <= 0:
            print("We have a problem with something... Reverting the vocabulary set...")

        if len(results) == 1:
            print("You have solved the riddle!")
            print("The answer is :", results[0])
            break

        result_printer(results, "Possible answer")
        recommends(results)

        print("\n\nPlease try some word...")
        text = input("What word have you tried? : ").upper()
        correctness = int(input("and they are what likeness? : "))
        screen_clear()
        results = password_filter(results, text, correctness)

def password_filter(results, word, number): """Filters the password that does not satisfies the relationship"""
    possible_answer=[]
    if debug_mode: print("----- Word -----|-- Similarity --") # FOR DEBUG
    for check_answer in results:
        n = 0
        for i,v in enumerate(word):
            if check_answer[i] == v:
                n += 1
        if debug_mode: print(check_answer, n) # FOR DEBUG
        if n == number:
            possible_answer.append(check_answer)
    if debug_mode: print(possible_answer) # FOR DEBUG
    return possible_answer

def recommends(results): """Calculate the word relationship for a chance of password elimination"""
    length = len(results[0])
    chars, answer = [], []
    for i in range(length):
        s= "".join(v[i] for v in results)
        char = max((s.count(j),j)for j in s)
        chars.append(char)

    max_char = max(chars)

    for i in results:
        if i[chars.index(max_char)] == max_char[1]:
            answer.append(i)

    result_printer(answer, "Recommended")

def result_printer(results, wording): """Designing the way that the possible answer will be print out"""
    print(wording)
    print("-" * len(wording))
    for i in results:
        print(i, end="\t")
    print("\n")

def command_center(results): """Redirect additional features using commands"""
    print("Welcome to command center. Here's what we can do...\n 1. /edit 2. /quit")
    actions = input("What do you want to do?")
    if actions == "/quit" or actions == "2":
        exit_and_save()
    elif actions == "/edit" or actions == "1":
        result_printer(results, "What word do you want to edit?")

def list_editor(results): """Make the item in the list editable using this function."""

def screen_clear(): """Cleaning screen for the program. Does not work more than this"""
    os.system('cls' if os.name == 'nt' else 'clear')

def screen_size(): """Calculate screen size in length and width"""
    root = tkinter.Tk()
    root.withdraw()

    width, height = root.winfo_screenwidth(), root.winfo_screenheight()
    if debug_mode: print(width, "x", height, "is your current screen size")
    return width, height

def file_save(results): """Creating the cache file and save it in the same directory"""
    if not os.path.exists(cache_file_name):
        # Try to create the file
        if debug_mode_basic or debug_mode: print("File does not exists. Creating it now...") # FOR DEBUG
    # Start writing in that file with the data in results
    file = open(default_file_name, "w")
    for i in results:
        if debug_mode_basic or debug_mode: print("Writing %s to %s"%(i, default_file_name)) # FOR DEBUG
        file.write(i+"\n")
    file.close()

def exit_and_save(): """Deleting the cache and quitting the program safely"""
    if debug_mode_basic or debug_mode: print("Deleting cache file now...")
    os.remove("cache.txt")

    if debug_mode_basic or debug_mode: print("Shutting the program down now. Thank you!")
    exit()

main()