def string(s1,s2):
    s1.replace(' ','').lower()
    s2.replace(' ','').lower()

    return sorted(s1)==sorted(s2)

print(string('test','estt'))