def string(str):
    a=str.find('not')
    b=str.find('poor')
    c=''
    if b>a and a>0 and b>0:
        c=str.replace(str[a:b+4],'good')
        return c
    else:
        return str

c=print(string('The lyrics is not that poor!'))
c=print(string('The lyrics is poor!'))