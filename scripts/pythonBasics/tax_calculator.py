# take input from user and calculate tax and total amount payable

amt = float(input('Enter your amount:'))
tax_rate = float(input('Enter tax rate:'))
tax = amt * tax_rate / 100
total = amt + tax
print('Amount payable by you is:' + str(total))
