# Python Program to Form a New String where the First Character and the Last Character have been Exchanged.


# Defining update function.
def update(s):
    n = len(s)
    S = s[-1]+s[1:n-1]+s[0]

    return S


# Main function.
def main():
    s1 = input(" Enter your String : ")  # Taking String input from user.

    s2 = update(s1)  # Calling replace function.

    print(f" .\n .\n Original String : {s1}")
    print(f" New String : {s2}", end="\n .\n .\n")


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
