print ("***Tip Calculatir***")
billamount = float(input("What was the total bill? "))
tip = int(input("How much would you like to tip? "))
people = int(input("How many people to split the bill? "))
tip_percentage = tip/100
total_tip = billamount * tip_percentage
total_bill = billamount + total_tip
finalamount = total_bill/people
eachshare = round(finalamount,2)
print("Each person should pay:",eachshare)