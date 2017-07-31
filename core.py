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
from time import sleep

# Import dependencies files
import systems          # Import systems.py
import configurations as settings   # Imports configurations.py


# Served as function caller and receptions
def main():
    print("Robco Industries (TM) Termlink Protocol")
    print("Welcome to Fallout 4 Hacking Solver")
    sleep(2)
    count, results, text = 1, [], ""
    error_code = 0

    while 1:
        systems.screen_clear()
        systems.result_printer(results, "Vocabulary Lists")

        if error_code == 0:
            print()
        elif error_code == 1:
            print("Please type something to start a program.")
        elif error_code == 2:
            print("'%s' is not a valid text length. (getting: %-2d| expecting: %-2d)" % (
                text, len(text), len(results[0])))
        elif error_code == 3:
            print("'%s' is already exists in the vocabulary list." % text)
        else:
            print("We are encontering the unexpectancies. Please restart the program...")

        text = input("Please type in possible password #%-2d : " % count)

        if text.startswith("/"):
            results = systems.command_center(results, text)

        elif text.isalpha():
            if (count > 1) and (len(text) != len(results[0])):
                error_code = 2

            else:
                results.append(text.upper())
                count += 1
                error_code = 0

        elif len(results) < 1:
            error_code = 1

        elif text in results:
            error_code = 3

        else:
            error_code = 0
            systems.screen_clear()
            break

    systems.file_save(results)

    count = 1

    while 1:
        if len(results) <= 0:
            print("We have a problem with something... Recovering data from cache..." if settings.cache_create else "You have disabled our cache system. We are unable to retrieve this...")
            break
            # and actually pull data from the cache created.

        if count > 4:
            print("We have failed you. We use too much attempt.")
            print(
                "You may continue, restart or make new issues in our repository for further investigation.")

        if len(results) == 1:
            print("You have solved the riddle!")
            print("The answer is :", results[0])
            break

        systems.result_printer(results, "Possible answer")
        recommends(results)

        print("\nAttempt #%d. Please try some word on your game terminal." % count)

        text = input("What word have you tried? : ").upper()

        if text.startswith("/"):
            results = systems.command_center(results, text)

        if text == "":  # When input is not fine
            print("Are you sure that you have solved it? \nPress ENTER again to confirm.")
            if input() == "":
                break
            else:
                continue

        count += 1  # When the input is still in tact

        if text not in results:
            print("Word '%s' does not exists in your vocabulary list" % text)
            continue

        correctness = int(input("and they are what likeness? : "))

        systems.screen_clear()
        results = password_filter(results, text, correctness)

    systems.exit_and_save()


# Filters the password that does not satisfies the relationship
def password_filter(results, word, number):
    possible_answer = []

    if settings.debug_mode:
        print("[Debug] ----- Word -----|-- Similarity --")  # FOR DEBUG

    for check_answer in results:
        n = 0

        for i, v in enumerate(word):
            if check_answer[i] == v:
                n += 1

        if settings.debug_mode:
            print("[Debug] " + check_answer, n)  # FOR DEBUG
        if n == number:
            possible_answer.append(check_answer)

    if settings.debug_mode:
        print("[Debug] " + possible_answer)  # FOR DEBUG

    return possible_answer


# Calculate the word relationship for a chance of password elimination
def recommends(results):
    length = len(results[0])
    chars, answer = [], []
    for i in range(length):
        s = "".join(v[i] for v in results)
        char = max((s.count(j), j)for j in s)
        chars.append(char)

    max_char = max(chars)

    for i in results:
        if i[chars.index(max_char)] == max_char[1]:
            answer.append(i)

    systems.result_printer(
        answer, "Recommend word")


# Automatic update
if settings.auto_update:
    if settings.debug_mode:
        print("[Debug] Updating the repository to the newest version...")
    os.system("git pull")
    if settings.debug_mode:
        print("[Debug] Your repository is updated!")


# Program will starts here...
main()
