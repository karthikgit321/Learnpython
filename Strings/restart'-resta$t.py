def firstoccurence(str):
    char=str[0]
    str=str.replace(char,'$')
    print(char+str[1:])

firstoccurence('pepper')

def change_char(str1):
  char = str1[0]
  str1 = str1.replace(char, '$')
  str1 = char + str1[1:]

  return str1

print(change_char('pepper'))