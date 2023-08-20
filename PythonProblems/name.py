n = int(input("Enter total number of names:"))
Name = []
print("\n Enter names: ")
for i in range(0, n):
    x = input()
Name.append(x)

print("\n Names are:")

for i in range(0, n):

    print(Name[i].capitalize())