string1 = input("Enter string: ")
if string1 == 'Spathiphyllum':
    print("Yes - Spathiphyllum is the best plant ever!")
elif string1 == 'spathiphyllum':
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not " + string1 + '!')

# tax calculator

income = float(input("Enter the annual income: "))
if income < 85528:
    tax = (income * 18)/100 - 556.2
else:
    tax = 14839.2 + ((income - 85528)*32)/100

tax = round(tax, 0)
if tax < 0:
    tax = 0.0
print("The tax is:", tax, "thalers")