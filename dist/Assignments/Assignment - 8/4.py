# Write a program that has a list of both positive and negative numbers. Create
# another list using filter () that has only positive values.

l1 = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]
print(f"Original list : {l1}")

l2 = list(filter(lambda i : i > 0, l1))   
print(f"Filtered list : {l2}")