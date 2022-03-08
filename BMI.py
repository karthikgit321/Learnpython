weight=float(input("enter your weight in kg: "))
height=float(input("enter your height in m: "))

BMI=weight/(height*height)
print(BMI)
if BMI<18.5:
    print(f"your BMI Is {BMI},You are underweight")
elif BMI<25:
    print(f"your BMI Is {BMI},You are Normal weight")
elif BMI<30:
    print(f"your BMI Is {BMI},You are over weight")
elif BMI<35:
    print(f"your BMI Is {BMI},You are obese")
else:
    print(f"your BMI Is {BMI},You are clinically obese")
