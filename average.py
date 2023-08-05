count = 0
sum1 = 0
print('Before', count, sum1)
for value in [9, 41, 12, 3, 71, 15]:
    count = count + 1
    sum1 = sum1 + value
    print(count, sum1, value)
print('After', count, sum1, sum1 / count)