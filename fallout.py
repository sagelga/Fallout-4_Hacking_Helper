def list_filter_word(l, word, number):
    d=[]
    for j in l:
        n=0
        for i,v in enumerate(word):
            if j[i] == v:
                n+=1
        print(j, n)
        if n == number:
            d.append(j)
    print(d)
    return d


l="""test
rags
fond
boss
wind
rush
maul
owns
dark
land
time
owed
last
hard
must""".split("\n")
while 1:
    inp = input()
    out= int(input())
    l = list_filter_word(l, inp, out)
