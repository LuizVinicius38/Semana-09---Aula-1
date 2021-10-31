n = 1
contPar = 0
contImpar = 0
while n <= 100:
    x = int(input(""))
    if x % 2 == 0:
        contPar += 1
    if x % 2 >= 1:
        contImpar += 1
    n = n + 1
print(contPar)
print(contImpar)
