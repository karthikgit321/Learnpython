#Input: {[([])]} --> Returns true
#Input: {[([])}] --> Returns false
def rev():
    str=''
    test=input("Enter the string")
    for i in range(len(test),0,-1):
        str=str+test[i-1]
    return str

str=rev()
print(str)


def rev():
    s="restart"
    str=''
    for i in s:
        str=i+str
    print(s)


