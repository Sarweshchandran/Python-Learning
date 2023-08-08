num = int(input("Enter the number:"))

def evenoddfunc(num):
    if(num % 2 == 0):
        print("The given number is ", num, " is even.")
    else:
        print("The given number is", num, " is odd.")
evenoddfunc(num)
