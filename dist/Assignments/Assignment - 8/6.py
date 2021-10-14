# Write a program using map () function to create a list of squares of numbers
# in the range 1-10.

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Initial list : {l1}")

l2 = list(map(lambda x : x ** 2, l1))
print(f"Updated list : {l2}")