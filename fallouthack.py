def main():
    """This will call other functions and served as a caller"""
    count = 1
    results, tries = [], []
    while 1:
        text = input("Getting possible password #%d : "%count)
        if "/" not in text:
            results.append(text)
            count += 1
        else:
            break

    print(result_printer(results))

    while 1:
        text = input("Please try some word \n What word have you tried? : ")
        correctness = input("and they are what likeness? : ")

        raw_text = []
        raw_text.append(text)
        raw_text.append(correctness)
        tries.append(raw_text)

        if correctness == 0:
            zero_likeness(results, tries, text)
        elif correctness == len(results[0]):
            result_printer(results)
            break
        elif correctness > 0:
            likeness(results, tries, text)

        result_printer(results)




def zero_likeness(results, tries, answer):
    """This function is for the entropy that gives 0 likeness.

        Program will delete the answer that are similar to the answer
        and delete itself from existence"""

    tries.append(answer)

    return results, tries

def likeness(results, tries, answer):
    """This function is for entropy that gives at least 1 likeness.

    Program will find the intersection of the results.
    If it can detects that they are in pattern,
    program will delete the word that are not in that pattern"""

    return results, tries

def result_printer(results):
    """Designing the way that the possible answer will be print out"""

    print("Possible answer is...")
    for i in results:
        print(i, end="\t")

main()

"""

empty
enact
swore
helps
knows
names
stake
marks
large
price
unite
stark
torch
handy

"""
