# pcost.py
#
# Exercise 1.27
def pcost(filename):
    suma = 0.0
    with open(filename,'rt') as f:
        next(f)
        for line in f:
            try:
                suma=suma+float(line.split(',')[2])*float(line.split(',')[1])
            except ValueError:
                print("Couldn't parse", line)
    return(suma)

print(pcost('Work\Data\missing.csv'))