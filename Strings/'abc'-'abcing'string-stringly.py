def string(str):
    if len(str)>2:
        if str[-3:]=='ing':
            str=str+'ly'
        else:
            str=str+'ing'
    return str

print(string('ab'))
print(string('abc'))
print(string('string'))