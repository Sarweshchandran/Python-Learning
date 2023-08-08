num = int(input("Enter the number:"))

def primefunc(num):
    if(num == 1):
        print("The given number is ", num, " is not prime.")
    elif(num>1):
        for x in range(2,num):
            if(num % x ==0):
                print("The given number is", num, " is  prime.")
                break
        else:
            print("The given number is", num, "not prime.")
primefunc(num)

