# Python Program to Replace all Occurrences of ‘a’ with '$' in a String using function.


# Defining replace function.
def replace(s):
    return s.replace('a', '$')


# Main function.
def main():
    s1 = input(" Enter your String : ")  # Taking String input from user.

    s2 = replace(s1)  # Calling replace function.

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
