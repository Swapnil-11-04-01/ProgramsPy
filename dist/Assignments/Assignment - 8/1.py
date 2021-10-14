l = []
n = int(input("Enter number of elements of your list : "))
print("Enter elements : ")
for i in range(n):
    l.append(input())


def index(a, l):
    x = []
    for i in range(len(l)):
        if l[i] == a:
            x.append(i)
    return x


a = input("Enter element whose index is to be found : \n")
I = index(a, l)
print(f"Number of times {a} is found is : {l.count(a)}\nIndex of {a} is/are : {I}")