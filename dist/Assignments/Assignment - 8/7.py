# Write a program to combine values in two lists using list comprehension.
# Combine only those values of a list that are multiples of values in the first
# list.

l1 = [input(f"Enter {i} index element for list 1 : ") for i in range(5)]
print()
l2 = [input(f"Enter {i} index element for list 2 : ") for i in range(5)]


def comb(x):
    for i in l1:
        if int(x) % int(i) == 0:
            return True


l3 = l1 + list(filter(comb, l2))
print(f"\nNew list : {l3}")
