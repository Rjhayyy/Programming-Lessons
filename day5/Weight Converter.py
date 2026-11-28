weight = int(input("Weight: "))
weight_type = input("(K)g or (L)bs: ").lower()


if weight_type == 'k':
    lbs = weight *  2.20
    print("You are",lbs,"Pounds")
elif weight_type == 'l':
    kg = weight * 0.45
    print ("You are",kg,"Kilograms")