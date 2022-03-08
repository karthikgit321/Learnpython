def charcount(str):
    duplicates={}
    for char in str:
        if char in duplicates:
            duplicates[char]+=1
        else:
            duplicates[char]=1
    print(duplicates)

    for key,value in duplicates.items():
        if value>1:
            print(key,end='')

charcount('google.com')

