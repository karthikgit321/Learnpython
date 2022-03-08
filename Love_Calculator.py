print("Welcome to Love Calculator!")
name1=input("What is your name? \n")
name2=input("What is their name? \n")

combined_name=name1+name2
lower_case_name=combined_name.lower()

t=lower_case_name.count("t")
r=lower_case_name.count("r")
u=lower_case_name.count("u")
e=lower_case_name.count("e")

true=t+r+u+e

l=lower_case_name.count("l")
o=lower_case_name.count("o")
v=lower_case_name.count("v")
e=lower_case_name.count("e")

love=l+o+v+e

love_Score=int(str(true)+ str(love))

print(love_Score)

if (love_Score< 20) or (love_Score> 90):
    print(f"your love score is {love_Score}you go together like coke and mentos")
elif (love_Score>40) and (love_Score<50):
    print(f"your score is {love_Score},you are alright together")
else:
    print("your score is ",love_Score)