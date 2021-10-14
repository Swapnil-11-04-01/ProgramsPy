#Write a program that creates a list of words by combining the words in two
# individual lists.

l1 = []
l2 = []
l3 = []

n = int(input("Enter common number of elements for both lists : "))

print("Enter elements for list 1 :")
for i in range(n):
    l1.append(input())
    
print("Enter elements for list 2 :")
for i in range(n):
    l2.append(input())
    
for i in range(n):
    l3.append(l1[i] + l2[i])
    
print(f"Final list : {l3}")