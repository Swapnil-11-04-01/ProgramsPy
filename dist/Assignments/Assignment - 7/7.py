# Python program to Count Total Number of Words in a String.

# Defining count function.
def count(s):
    S = s.split()
    return len(S)


# Main function.
def main():
    s1 = input(" Enter your String : ")  # Taking String input from user.

    n = count(s1)

    print(f" No. of words : {n}", end="\n .\n .\n")


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
