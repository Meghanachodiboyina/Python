contacts ={}

n = int(input("how many contacts do u want to enter:"))

for i in range(n):
    name = input("enter name: ")
    contact_number = int(input("enter contact number"))
    contacts[name]=contact_number
print("contacts",contacts)
    