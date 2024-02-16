# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.00

month=1

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000



while principal > 0:
    payment = round(min(2684.11, principal * (1+rate/12)),2)
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal = round(principal * (1+rate/12) - payment - 1000,2)
        total_paid = round(total_paid + payment + 1000,2)
    else:
        principal = round(principal * (1+rate/12) - payment,2)
        total_paid = round(total_paid + payment,2)
    print(month, total_paid, principal, payment)
    month += 1

    

print ('Total paid', round(total_paid,2))