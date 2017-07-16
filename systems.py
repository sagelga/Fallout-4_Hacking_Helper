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
import configurations # Imports configurations.py

def result_printer(results, wording): # Designing the way that the possible answer will be print out
    if not len(results) == 0: # Will print if the program does not recieve a blank print
        print(wording)
        print("-" * int(len(wording)*1.5))
        for i in results:
            print(i, end="\t")
        print("\n")

def command_center(results, actions): # Redirect additional features using commands
    if len(actions) != 1: print("Welcome to command center. Here's what we can do...\n1.  /edit 2.  /quit")
    if not actions.startswith("/"): actions = input("What do you want to do?")

    if actions == "/edit" or actions == "1":
        results = list_editor(results)
    if actions == "/quit" or actions == "2":
        exit_and_save()

    return results

def list_editor(results): # Make the item in the list editable using this function
    while True:
        screen_clear()
        result_printer(results, "Here's everything you have")

        actions = input("Please type /stop to finish your editing\nWhat word do you want to change?  : ")

        if actions .startswith("/"):
            if actions == "/stop":
                break
            elif actions == "/quit":
                exit_and_save()
        else:
            actions = actions.upper()

        if actions in results:
            for i in range(len(results)):
                if results[i] == actions:
                    results[i] = input("What do you want the word %s to become? : "%(results[i])).upper()
        else:
            print("We cannot find the word %s in the list. Please check for typos..."%actions)

    # After done with list modification
    return results

def screen_clear(): # Cleaning screen for the program. Does not work more than this
    os.system('cls' if os.name == 'nt' else 'clear')

def file_save(results): # Creating the cache file and save it in the same directory
    if configurations.cache_create:
        if os.path.exists(configurations.cache_file_name):
            # Try to create the file
            if configurations.debug_mode_basic or configurations.debug_mode: print("[Debug] File %s does exists. Deleting it now..."%configurations.cache_file_name) # FOR DEBUG
            if configurations.cache_delete: os.remove(configurations.cache_file_name)
    # Start writing in that file with the data in results

        file = open(configurations.cache_file_name, "w")

        # Creating file headers
        import datetime                      # Getting user's time for cache timestamps
        text = "Vocabulary cache in : " + str(datetime.datetime.now().strftime("%A, %d %B %Y %I:%M %p.")) + "\n" \
                   + "If you wish to shut data caching out, please go check out the Python script." + "\n"
        file.write(text)

        for i in results:
            if (configurations.debug_mode_basic or configurations.debug_mode):
                print("[Debug] Writing %s to %s"%(i, configurations.cache_file_name)) # FOR DEBUG
                text = i + "\n"
            file.write(text)
    file.close()

def exit_and_save(): # Deleting the cache and quitting the program safely
    if configurations.cache_delete:
        if os.path.exists(configurations.cache_file_name):
            # Try to create the file
            if configurations.debug_mode_basic or configurations.debug_mode: print("[Debug] File %s does exists. Deleting it now..."%configurations.cache_file_name) # FOR DEBUG
            os.remove(configurations.cache_file_name)

    if configurations.debug_mode: print("[Debug] Shutting the program down now. Thank you!") # FOR DEBUG
    exit()
