def recommends(list_word):
    lenght = len(list_word[0])
    chars = []
    for i in range(lenght):
        s= "".join(v[i] for v in list_word)
        char = max((s.count(j),j)for j in s)
        chars.append(char)
        
    max_char = max(chars)
    print("\nRecommends words :"+" ".join(i for i in list_word if i[chars.index(max_char)]==max_char[1]))

def main():
    """This will call other functions and served as a caller"""
    count, triggers = 1, 1
    results = []
    while triggers:
        text = input("Getting possible password #%-2d : "%count)
        if not text.startswith("/"):
            results.append(text.upper())   
            count += 1
        else:
            triggers = 0
        
    print("\nHere's what you have included.")

    while 1:
        if len(results) <= 1:
            print("You have solved the hack!")
            print("The answer is :", results[0])
            break
        
        result_printer(results)
        recommends(results)
        text = input("\n\nPlease try some word...\nWhat word have you tried? : ").upper()
        correctness = int(input("and they are what likeness? : "))
        print()
        results = list_filter_word(results, text, correctness)

def list_filter_word(results, word, number):
    possible_answer=[]
    # print("----- Word -----|-- Similarity --")
    for check_answer in results:
        n = 0
        for i,v in enumerate(word):
            if check_answer[i] == v:
                n += 1
        # print(check_answer, n)
        if n == number:
            possible_answer.append(check_answer)
    # print(possible_answer)
    return possible_answer

def result_printer(results):
    """Designing the way that the possible answer will be print out"""

    print("Possible answer is...")
    print("---------------------")
    for i in results:
        print(i, end="\t")

main()
