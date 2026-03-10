#simple interest = P*T*R /100

principle_amt = float(input("enter principle amount:"))
time = float(input("enter time in years:"))
rate = float(input("enter rate of interest:"))
simple_interest = (principle_amt * time* rate)/100
print("simple interest is :",simple_interest)
total_amount= principle_amt + simple_interest
print("total amount with interest is:",total_amount)