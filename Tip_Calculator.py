#Tip calculator
#eg:- if the total bill is 150,add tip and divide split the bill for how many ever people u want
print("Welcome to the tip calculator")
bill=float(input("What was the total bill? $"))
Tip=float(input("what percentage top would you like to give? 10,12, or 15? "))
actual_tip=float(Tip/100)
Total_people=int(input("Enter the count of people to split the bill?"))

actual_bill=actual_tip*bill
Total_bill=actual_bill+bill
split_bill= Total_bill/Total_people
#final_amount=round(split_bill,2)
final_amount="{:.2f}".format(split_bill)
print(f"Each person should pay ${final_amount}")