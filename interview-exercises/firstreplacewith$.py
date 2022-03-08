
def dollar(str):
    char=str[0]
    str=str[1:]
    str1=str.replace(char,'$')
    print(char+str1)

dollar('restart')