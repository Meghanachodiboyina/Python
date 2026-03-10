def simple_interest(p, t, r):
    si = (p * t * r) / 100
    return si

p = float(input("Enter principal: "))
t = float(input("Enter time: "))
r = float(input("Enter rate: "))

print("Simple Interest:", simple_interest(p, t, r))