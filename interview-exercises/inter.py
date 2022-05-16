
d1 = {("a","b","c","d","e"):[1,2,3,4,5], "x":8, "y":9}

for key in d1:
    if key == ("a","b","c","d","e"):
        for i,letter in enumerate(key):
            if letter == 'd':
                print(d1[("a","b","c","d","e")][i])

'''
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}

print(Dict[1][0])

'''