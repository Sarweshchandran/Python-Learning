num = 0
tot = 0.0
while True:
    sval = input('Enter a number:')
    if sval == 'done':
        break
    try:
        val = float(sval)
        print(val)
        num = num +1
        tot = tot + val
    except:
        print('Invalid Input')
    continue
    #num = num + 1
    #tot = tot + val
print('All Done!')
print(tot, num, tot/num)
