n = 1729
for i in range(n):
    for j in range(n):
        if i**3 + j**3 == n:
            print(i,j)