# Python Program to Calculate the Number of Upper Case Letters and Lower Case Letters in a String.


# Defining count function.
def count(s):
    u = l = 0

    for i in s:
        if i.isupper():
            u += 1
        if i.islower():
            l += 1
    return u, l


# Main function.
def main():
    s1 = input(" Enter your String : ")  # Taking String input from user.

    u, l = count(s1)  # Calling replace function.

    print(f" .\n .\n No. of upper case letters : {u}")
    print(f" No. of lower case letters : {l}", end="\n .\n .\n")


# Calling main function
main()

# Creating loop for running program multiple times.
while True:
    action = input(" Want to try another String ? (y,n) : ")
    if action == 'y':
        print("\n .\n .\n")
        main()
    elif action == 'n':
        print("\n .\n .\n")
        print(" !!THANK YOU!!\n Have a nice day :)")
        break
    else:
        print(" .\n .\n Please reply 'y' for Yes and 'n' for No.")
        continue
