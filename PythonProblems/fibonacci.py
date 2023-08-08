n = int(input("Enter the number:"))
def fibonacci(n):
    a = 0
    b = 1
    if n ==1:
        print(n)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            n = a+b
            a = b
            b = n
            print(n)
fibonacci(n)