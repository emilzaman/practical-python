# pcost.py
#
# Exercise 1.27
suma = 0.0
with open('Work/Data/portfolio.csv','rt') as f:
    next(f)
    for line in f:
        suma=suma+float(line.split(',')[2])*float(line.split(',')[1])
print (f'Total cost is: {suma:.2f}')