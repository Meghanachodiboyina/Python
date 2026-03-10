a = 10
b = 20
print("before",a,b)
a,b = b,a
print("after",a,b)

print("----------")


a=10
b=20
print("before",a,b)
temp=a
a=b
b=temp
print("after",a,b)