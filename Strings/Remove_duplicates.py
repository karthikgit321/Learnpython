def dup(String):
    l=''
    for i in String:
        if i not in l:
            l=l+i
    print(l)

dup("Helllo")