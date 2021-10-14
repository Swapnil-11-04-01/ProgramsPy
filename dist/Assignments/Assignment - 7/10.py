# Python program to extract mail domain from given mail id.


# Defining domain function to extract domain through String slicing.
def domain(s):
    i = s.find("@")
    S = s[i + 1:]
    return S


# Main function
def main():
    s1 = input(" Enter your complete Email address : ")  # Taking String input from user.

    d = domain(s1)  # Calling domain function.

    print(f"\n Your mail domain is : {d}")


# Calling main function
main()

# Creating loop for running program multiple times.
while True:
    action = input(" Want to try another Email id ? (y,n) : ")
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
