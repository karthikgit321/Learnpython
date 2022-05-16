# str1 = "It's raining cats and cats"
#
# def cats(str1,old,new):
#     str=str1.split()
#     if str[-1]==old:
#         str[-1]=new
#     print(str)
#     print(" ".join(str))
#
# cats(str1,"cats","dogs")

text = "Its raining cats and cats".split(' ') # splits it at space
text[text.index('cats', text.index('cats')+1)] = 'dogs' # find where cat occurs after the first occurrence (if you have 3 instead of two and want to replace the third, this won't work) and replaces it
text = " ".join(text)
print(text)