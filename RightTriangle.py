def find_tuples(p):
    tuples = []
    for i in range(1, p):
        for j in range(1, p):
            for k in range(1, p):
                if i <= j < k and i + j + k == p and i ** 2 + j ** 2 == k ** 2:
                    list = [i, j, k]
                    tuples.append(list)
    return tuples

print(find_tuples(60))
