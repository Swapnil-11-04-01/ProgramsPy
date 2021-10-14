# finding total money

n = int(input('How many 10 rupees coin do you have? '))
m = int(input('How many 5 rupees coin do you have? '))
o = int(input('How many 2 rupees coin do you have? '))
p = int(input('How many 1 rupees coin do you have? '))

total_amount = n*10+m*5+2*o+1*p
print(f"Total Money = {total_amount}")