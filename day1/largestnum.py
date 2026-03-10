a= int(input("eneter a value"))
b= int(input("eneter b value"))
c= int(input("eneter c value"))
if a==b==c:
    print("all are equal")
elif a>b and a>c:
    print("a is bigger")
elif b>c and b>a:
    print("b is bigger")
else:
    print("c is bigger")