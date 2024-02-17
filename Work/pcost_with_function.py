# pcost.py
#
# Exercise 1.27
def pcost(filename):
    suma = 0.0
    with open(filename,'rt') as f:
        next(f)
        for line in f:
            suma=suma+float(line.split(',')[2])*float(line.split(',')[1])
    return(suma)

print(pcost('Work\Data\portfolio.csv'))