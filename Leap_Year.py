'''
def leap_year():
    ly=int(input("Which year do you want to check"))
    if(ly%4==0):
        if (ly%100==0):
            if (ly%400==0):
                print(f"{ly} is a leap year")
            else:
                print(f"{ly} is not a leap year")
        else:
            print(f"{ly} is a leap year")
    else:
        print(f"{ly} is not a leap year")

leap_year()
'''


def leap_year():
    ly=int(input("Which year do you want to check"))
    if(ly%4==0):
        if(ly%400==0):
            print(f"{ly} is a leap year")
        else:
            print(f"{ly} is not a leap year")
    else:
        print(ly,"is not a leap year")

leap_year()
