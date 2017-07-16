"""
Fallout 4 Hacking minigame Helper
---------------------------------
Please go read README.md for an instructions on what you can do.

Thanks!
- @son9912
"""

# Importing dependencies libraries
import os                            # Allows OS system call power
import os.path                       # Allows OS system call power

# Import dependencies files
import systems # Import systems.py
import configurations # Imports configurations.py

def main(): # Served as function caller and receptions
    count, results = 1, [],

    while 1:
        systems.screen_clear()
        systems.result_printer(results, "Vocabulary Lists")

        text = input("Please type in possible password #%-2d : "%count)

        if text.startswith("/"):
            results = systems.command_center(results, text)

        elif text.isalpha():
            if (count > 1) and (len(text) != len(results[0])):
                    print("'%s' is not a valid text length. (expecting: %d) Please try again..."%(text, len(results[0])))
                    continue
            else:
                results.append(text.upper())
                count += 1

        elif len(results) < 1:
                print("Please type something to start a program.")
                continue

        else:
                error_code = 0
                systems.screen_clear()
                break

    print("Done recieving more vocabulary...\nSaving...\n")
    systems.file_save(results)

    count = 0

    while 1:
        count += 1
        if len(results) <= 0:
            print("We have a problem with something... Recovering data from cache..." if cache_create else "You have disabled our cache system. We are unable to retrieve this...")
            # and actually pull data from the cache created.

        if count > 4:
            print("We have failed you. Please report this error immediately!")
            print("You may continue, restart or make new issues in repository.")

        if len(results) == 1:
            print("You have solved the riddle!")
            print("The answer is :", results[0])
            break

        systems.result_printer(results, "Possible answer")
        recommends(results)

        print("\nAttempt #%.1d. Please try some word on your game terminal."%count)
        text = input("What word have you tried? : ").upper()
        correctness = int(input("and they are what likeness? : "))
        systems.screen_clear()
        results = password_filter(results, text, correctness)

    systems.exit_and_save()

def password_filter(results, word, number): # Filters the password that does not satisfies the relationship
    possible_answer=[]
    if configurations.debug_mode: print("[Debug] ----- Word -----|-- Similarity --") # FOR DEBUG
    for check_answer in results:
        n = 0
        for i,v in enumerate(word):
            if check_answer[i] == v:
                n += 1
        if configurations.debug_mode: print("[Debug] " + check_answer, n) # FOR DEBUG
        if n == number:
            possible_answer.append(check_answer)
    if configurations.debug_mode: print("[Debug] " + possible_answer) # FOR DEBUG
    return possible_answer

def recommends(results): # Calculate the word relationship for a chance of password elimination
    length = len(results[0])
    chars, answer = [], []
    for i in range(length):
        s = "".join(v[i] for v in results)
        char = max((s.count(j),j)for j in s)
        chars.append(char)

    max_char = max(chars)

    for i in results:
        if i[chars.index(max_char)] == max_char[1]:
            answer.append(i)

    systems.result_printer(answer, "Recommend word contains : %s"%max_char[1])

# Automatic update
if configurations.auto_update:
    if configurations.debug_mode: print("[Debug] Updating the repository to the newest version...")
    os.system("git pull")
    if configurations.debug_mode: print("[Debug] Your repository is updated!")


# Program will starts here...
main()
