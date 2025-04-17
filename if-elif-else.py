total_bill = 7000
if total_bill>= 10000:
    discount= 0.1
elif 5000 <= total_bill< 10000:
    discount=0.07
elif 2000 <= total_bill< 5000:
    discount= 0.05
else:
    discount = 0
total_bill = total_bill - discount* total_bill
print("Your total bill is:",total_bill)