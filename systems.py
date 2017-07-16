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

def result_printer(results, wording): # Designing the way that the possible answer will be print out
    print(wording +"\n" + ("-" * int(len(wording)*1.5)))
    for i in results:
        print(i, end="\t")
    print("\n")

def command_center(results, actions): # Redirect additional features using commands
    if len(actions) != 1: print("Welcome to command center. Here's what we can do...\n1.  /edit 2.  /quit")
    if not actions.startswith("/"): actions = input("What do you want to do?")

    if actions == "/edit" or actions == "1":
        list_editor(results)
    if actions == "/quit" or actions == "2":
        exit_and_save()

def list_editor(results): # Make the item in the list editable using this function
    while True:
        result_printer(results, "Here's everything you have")

        actions = input("What word do you want to change?")
        if results.find(actions):
            results[results.find(actions)] = actions
        actions = input("Have you done editing?").upper()
        if 'Y' in actions:
            if debug_mode: print("[Debug] You have done editing...") # FOR DEBUG
            break

def screen_clear(): # Cleaning screen for the program. Does not work more than this
    os.system('cls' if os.name == 'nt' else 'clear')

def file_save(results): # Creating the cache file and save it in the same directory
    if cache_create:
        if os.path.exists(cache_file_name):
            # Try to create the file
            if debug_mode_basic or debug_mode: print("[Debug] File does exists. Deleting it now...") # FOR DEBUG
            if cache_delete: os.remove(cache_file_name)
    # Start writing in that file with the data in results

        file = open(cache_file_name, "w")

        # Creating file headers
        text = "Vocabulary cache in : " + str(datetime.datetime.now().strftime("%A, %d %B %Y %I:%M %p.")) + "\n" \
                   + "If you wish to shut data caching out, please go check out the Python script." + "\n"
        file.write(text)

        for i in results:
            if (debug_mode_basic or debug_mode):
                print("[Debug] Writing %s to %s"%(i, cache_file_name)) # FOR DEBUG
                text = i + "\n"
            file.write(text)
    file.close()

def exit_and_save(): # Deleting the cache and quitting the program safely
    if debug_mode_basic or debug_mode: print("[Debug] Deleting cache file now...") # FOR DEBUG
    if cache_delete: os.remove(cache_file_name)

    if debug_mode_basic or debug_mode: print("[Debug] Shutting the program down now. Thank you!") # FOR DEBUG
    exit()