# str='geeksfor geeks'
# l=[]
# def test_str():
#     for i in str:
#         if i not in l:
#             l.append(i)
#
# print(''.join(l))

s ='geeksfor geeks'


def test_str():
    newstring = ''
    for string in s:
        if string not in newstring:
            newstring+=string
    print(newstring)