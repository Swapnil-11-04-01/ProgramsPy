# Write a program to multiply two matrices (using nested lists).

l1, l2, l3 = [], [], [[0, 0], [0, 0]]


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


print("\nAfter multiplication new Matrix C :")
for i in range(len(l1)):
    for j in range(len(l1[0])):
        for k in range(len(l1)):
            l3[i][j] += l1[i][k][0] * l2[k][j][0]

for i in l3:
    print(i)