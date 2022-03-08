

    #Function to reverse words in a given string.
def reversewords():
    S = 'i.like.this.program.very.much'
    l = []
    rev = S.split('.')
    print(rev)
    for i in range(len(rev), 0, -1):
        l.append(rev[i-1])
        print(l)
    reversed_word = '.'.join(l)
    print(reversed_word)


reversewords()