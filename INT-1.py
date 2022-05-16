def duplicates(str):
    dict1={}
    for char in str:
        if char not in dict1:
            dict1[char]=str.count(char)
    print (dict1)

    for key,value in dict1.items():
        if value>1:
            print(key,value,end='')


duplicates("chennai")