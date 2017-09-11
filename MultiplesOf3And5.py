def multiples_of_3_and_5(n):
    sum = 0
    for i in range(3, n, 3):
        sum += i
    for i in range(5, n, 5):
        sum += i
    for i in range(15, n, 15):
        sum -= i
    return sum

print(multiples_of_3_and_5(7))