hodnoty = [7, 2, 10, 5, 2, 8, 1, 6, 9, 4, 2, 8, 5, 10, 3, 7, 1, 4, 6, 9, 8, 2, 5, 5]

while True:
    prohozeno = False
    for i in range(len(hodnoty) - 1):
        if hodnoty[i] < hodnoty[i+1]:
            hodnoty[i], hodnoty[i+1] = hodnoty[i+1], hodnoty[i]
            prohozeno = True

print(hodnoty)