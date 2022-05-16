num=1234
reverse_no=0

while num>0:
    digit=num%10
    reverse_no=reverse_no*10+digit
    num=num//10
print(reverse_no)
