age = int(input("Enter the current age"))
Total_years = 90
Remaining_years = Total_years-age
days = Remaining_years*365
weeks = Remaining_years*52
months = Remaining_years*12

message=f"you have {days} days, {weeks} weeks,{months} months"

print(message)