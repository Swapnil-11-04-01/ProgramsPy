# Write a program to find largest value in a list using reduce () function.
import functools

l = [int(input(f"Enter {i} index element for your list : ")) for i in range(5)]

a = functools.reduce(lambda x, y: x if x > y else y, l)
print(f"\nLargest elent is {a}")