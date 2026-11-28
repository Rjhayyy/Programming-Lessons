house = 1000000
good_credit = True
bad_credit = False

if good_credit:
    pay = 0.1 * house
    print("Payment is",pay)
elif bad_credit:
    pay = 0.2 * house
    print("Payment is",pay)
else:
    print("Please tell me credit status")