str="hello how are you"
str1=str.split()
print(str1)
str2=[]
for i in str1:
    str2.append(i[::-1]+'ay')
    # str2.append("ay")
print(' '.join(str2))
