# Program to check whether the string is Palindrome or not.


# Defining a function to check string for being a Palindrome
def palindrome():
    s1 = input("Enter a String : ")
    s2 = s1.lower()
    s3 = ""
    n = len(s1)

    for i in range(n - 1, -1, -1):
        s3 = s3 + s2[i]

    if s3 == s2:
        print(f"String ( {s1} ) is a Palindrome.", end="\n.\n.\n")
    else:
        print(f"String ( {s1} ) is not a Palindrome.", end="\n.\n.\n")


# Calling function.
palindrome()

# Creating loop for running program multiple times.
while True:
    action = input("Want to try another String ? (y,n) : ")
    if action == 'y':
        print("\n.\n.\n")
        palindrome()
    elif action == 'n':
        print("\n.\n.\n")
        print("!!THANK YOU!!\nHave a nice day :)")
        break
    else:
        print(".\n.\nPlease reply 'y' for Yes and 'n' for No.")
        continue
