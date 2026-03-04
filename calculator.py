num1 = float(input("enter first number"))
num2 = float(input("enter second number"))
operation = input("enter which operation do u want (+,-,*,/,//,%,**): ")
if operation == '+':
    print("addition:",num1+num2)
elif operation == '-':
    print("subtraction:",num1-num2)
elif operation == '*':
    print("multiplication:",num1*num2)
elif operation == '/':
    if num2 == 0:
        print("denominator is zero so zero division error")
    else:
        print("division:",num1/num2)
elif operation == '//':
    if num2 == 0:
        print("denominator is zero so zero division error")
    else:
        print("floor division:",num1//num2)
elif operation == '%':
    print("modulus:",num1%num2)
elif operation == '**':
    print("power:",num1**num2)
else:
    print("invalid operation pls check it")
