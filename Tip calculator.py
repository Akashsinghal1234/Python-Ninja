#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to tip calculator. ")

total_bill = float(input("what was the total bill ? "))
tip_percent = int(input("What percentage tip would you like to give ? 10, 12, or 15? "))

tip_to_share = total_bill * tip_percent / 100 
final_to_share_tip = total_bill + tip_to_share 

to_split_bill = int(input("How many people to split the bill? "))

split_result = final_to_share_tip / to_split_bill

print(round(split_result , 2 ))

