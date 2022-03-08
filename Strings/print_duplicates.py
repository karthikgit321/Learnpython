def remove_duplicates(str):
    duplicates=[]
    for char in str:
        if str.count(char)>1:
            if char not in duplicates:
                duplicates.append(char)
    return (''.join(duplicates))

print(remove_duplicates("java"))

