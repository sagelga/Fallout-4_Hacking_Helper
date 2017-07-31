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
import configurations as settings  # Imports configurations.py


# Designing the way that the possible answer will be print out
def result_printer(results, wording):
    if not len(results) == 0:  # Will print if the program does not recieve a blank print
        print(wording + " (%d)" % len(results))
        print("-" * len(wording))
        for i in results:
            print(i, end="\t")
        print("\n")


def command_center(results, actions):  # Redirect additional features using commands
    actions = input("""Welcome to command center. Here's what we can do...
1. /edit\t2. /quit
What do you want to do? : """)

    if actions.startswith("/edit") or actions == "1":
        results = list_editor(results, actions)
    if actions.startswith("/quit") or actions == "2":
        exit_and_save()

    return results


def list_editor(results, actions):  # Make the item in the list editable using this function

    one_time = False

    if len(results) < 1:
        print("You cannot use /edit when you have a blank vocabulary list")
        return results

    while True:
        screen_clear()
        result_printer(results, "Here's everything you have")

        actions = actions[5:].strip().upper()
        if actions == "":
            actions = input("Please type /stop to finish your editing\n \
                      What word do you want to change? : ")
        else:
            one_time = True

        if actions.startswith("/"):
            if actions.startswith("/stop"):
                break
            else:
                command_center(results, actions)
        else:
            actions = actions.upper()

        if actions in results:
            for i, _ in enumerate(results):
                if results[i] == actions:
                    results[i] = input(
                        "What do you want '%s' to become? : " % (results[i])).upper()
        else:
            print(
                "We cannot find '%s' in the list. Please check for typos..." % actions)

        if one_time:
            break

    # After done with list modification
    return results


def screen_clear():  # Cleaning screen for the program. Does not work more than this
    os.system('cls' if os.name == 'nt' else 'clear')


def file_save(results):  # Creating the cache file and save it in the same directory
    if settings.cache_create:
        if os.path.exists(settings.cache_file_name):
            # Try to create the file
            if settings.debug_mode_basic or settings.debug_mode:
                print("[Debug] File %s does exists. Deleting it now..." %
                      settings.cache_file_name)  # FOR DEBUG
            if settings.cache_delete:
                os.remove(settings.cache_file_name)
    # Start writing in that file with the data in results

        file = open(settings.cache_file_name, "w")

        # Creating file headers
        import datetime  # Getting user's time for cache timestamps
        text = "Vocabulary cache in : " + str(datetime.datetime.now().strftime("%A, %d %B %Y %I:%M %p.")) + "\n" \
            + "If you wish to shut data caching out, please go check out the Python script." + "\n"
        file.write(text)

        for i in results:
            if (settings.debug_mode_basic or settings.debug_mode):
                print("[Debug] Writing %s to %s" %
                      (i, settings.cache_file_name))  # FOR DEBUG
                text = i + "\n"
            file.write(text)
    file.close()


def exit_and_save():  # Deleting the cache and quitting the program safely
    if settings.cache_delete:
        if os.path.exists(settings.cache_file_name):
            # Try to delete the file, because it is still exists.
            if settings.debug_mode_basic or settings.debug_mode:
                print("[Debug] File %s does exists. Deleting it now..." %
                      settings.cache_file_name)  # FOR DEBUG
            os.remove(settings.cache_file_name)

    if settings.debug_mode:
        print("[Debug] Shutting the program down now. Thank you!")  # FOR DEBUG
    exit()
