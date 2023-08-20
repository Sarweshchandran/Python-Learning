n = int(input("Enter the number of list item:"))
name = []
print("Enter the list items")
for i in range(0,n):
    x = input()
    name.append(x)
for i in range(0,n):
    print(name[i].capitalize())