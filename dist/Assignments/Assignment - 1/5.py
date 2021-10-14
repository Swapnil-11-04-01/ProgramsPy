n=int(input('Enter 1st number : '))
m=int(input('Enter 2nd number : '))

print(f'Before swapping, the value of 1st number = {n} and 2nd number ={m}')

n=n+m
m=n-m
n=n-m

print(f'After swapping, the value of 1st number = {n} and 2nd number ={m}')
