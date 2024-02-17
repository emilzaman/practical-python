def sum(n):
    suma = 0
    while n > 0:
        suma = suma + n
        n = n - 1
    return(suma)

a = sum(100)
print(a)