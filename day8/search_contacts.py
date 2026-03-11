contacts={}
n = int(input("enter how many contacts:"))
for i in range(n):
    name=input("enter name:")
    contact_number=input("enter contact number:")
    contacts[name]=contact_number

search = input("enter name to search in contacts")
if search in contacts:
    print("contact number:",contacts.get(search))
else:
    print("name is not in contacts")