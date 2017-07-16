# Global Configurations
auto_update = True                         # Automatically update this python script everytime it starts [Default = False]

debug_mode = False                        # Starts the program with logging mode (All) [Default = False]
debug_mode_basic = False             # Starts the program with logging mode (Unstable features) [Default = False]

cache_file_extension = "txt"         # Do not edit this. [Default = "txt"]
cache_file_name = "cache"            # Warning: Do not use the [Default = "cache"]

cache_delete = True                         # Allow program to delete cache file [Default = True]
cache_create = True                         # Allow program to create cache file [Default = True]

# Importing dependencies libraries
import os                       # Allows OS system call power
import os.path             # Allows OS system call power
import  datetime        # Getting user's time for cache timestamps

# Import dependencies files
from systems import * # Import system.py

def main(): # Served as function caller and receptions
    count, results, error_code = 1, [], 0

    while 1:
        screen_clear()
        result_printer(results, "Vocabulary Lists")

        text = input("Please type in possible password #%-2d : "%count)

        if error_code == 1:
            print("'%s' is not a valid text length. (expecting: %d) Please try again..."%(text, len(text[count-1])))
        if error_code == 2:
            print("Please type something to start a program.")

        if text.isalpha():
            if count != 1:
                if len(text) != len(results[0]):
                    error_code = 1
                    continue
            else:
                results.append(text.upper())
                count += 1
                error_code = 0
        elif text.startswith("/"):
            command_center(results, text)
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

    count = 0
    while 1:
        count += 1
        if len(results) <= 0:
            print("We have a problem with something... Recovering data from cache...")

        if count > 4:
            print("We have failed you. Please report this error immediately!")
            print("You may continue, restart or make new issues in repository.")

        if len(results) == 1:
            print("You have solved the riddle!")
            print("The answer is :", results[0])
            break

        result_printer(results, "Possible answer")
        recommends(results)

        print("\nAttempt #%.1d. Please try some word on your game terminal."%count)
        text = input("What word have you tried? : ").upper()
        correctness = int(input("and they are what likeness? : "))
        screen_clear()
        results = password_filter(results, text, correctness)

    exit_and_save()

def password_filter(results, word, number): # Filters the password that does not satisfies the relationship
    possible_answer=[]
    if debug_mode: print("[Debug] ----- Word -----|-- Similarity --") # FOR DEBUG
    for check_answer in results:
        n = 0
        for i,v in enumerate(word):
            if check_answer[i] == v:
                n += 1
        if debug_mode: print("[Debug] " + check_answer, n) # FOR DEBUG
        if n == number:
            possible_answer.append(check_answer)
    if debug_mode: print("[Debug] " + possible_answer) # FOR DEBUG
    return possible_answer

def recommends(results): # Calculate the word relationship for a chance of password elimination
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

# Edit every configurations here
# For developers only!
cache_file_name  = cache_file_name + "." + cache_file_extension

# Automatic update
if auto_update:
    if debug_mode: print("[Debug] Updating the repository to the newest version...")
    os.system("git pull")
    if debug_mode: print("[Debug] Your repository is updated!")


# Program will starts here...
main()
