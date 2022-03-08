import random
name_str=input("Enter the names separated by comma\n")
names=name_str.split(',')
print(names)


random_int=random.randint(0,len(names))
print(random_int)
choose_name=names[random_int]
print(f"{choose_name} has to pay the bill")

(random.choice(names))