# Write a program that forms a list of first character of every word in another
# list.

l1 = []
l2 = []

n = int(input("Enter number of elements for list : "))

print("Enter elements : ")
for i in range(n):
    l1.append(input())

for i in l1:
    l2.append(i[0])

print(f"Final list is : {l2}")
