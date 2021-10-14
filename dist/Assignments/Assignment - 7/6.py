# Python Program to Count the Number of Vowels in a String

# Defining count function.
def count(s):
    c = 0

    for i in s:
        if i == 'a' or i == "e" or i == "i" or i == "o" or i == "u" or i == 'A' or i == "E" or i == "I" or i == "O" or i == "U":
            c += 1
    return c


# Main function.
def main():
    s1 = input(" Enter your String : ")  # Taking String input from user.

    n = count(s1)  # Calling replace function.

    print(f" No. of vowels : {n}", end="\n .\n .\n")


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
