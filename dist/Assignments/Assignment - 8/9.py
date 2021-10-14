# Write a program to add two matrices (using nested lists).

l1, l2, l3 = [], [], []



print("Matrix A (2 x 2)")
for i in range(2):
    l1.append(list([int(input(f"Enter ({i},{j}) element for Matrix A : "))] for j in range(2)))

print("\nMatrix B (2 x 2)")
for i in range(2):
    l2.append(list([int(input(f"Enter ({i},{j}) element for Matrix B : "))] for j in range(2)))


print("\nMAtrix A :")
for i in l1:
    print(i)

print("\nMAtrix B :")
for i in l2:
    print(i)


print("\nAfter addition new Matrix C :")
l3 = [[l1[i][j][0] + l2[i][j][0] for j in range(2)] for i in range(2)]

for i in l3:
    print(i)