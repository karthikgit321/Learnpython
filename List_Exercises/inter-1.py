'''
string=input("enter the string and remove repeated characters in a string")
k=''.join(set(string))
print(k)
'''

def RemoveDupliChar():
    word=input("Enter the string to be searched")
    NewWord = " "
    index = 0
    for char in word:
        if char != NewWord[index]:
            NewWord += char
            index += 1
    print(NewWord.strip())

RemoveDupliChar()