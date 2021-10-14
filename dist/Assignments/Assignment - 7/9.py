# Python program to demonstrate the use of split() and join() function in a string.


# Defining a demonstrate use of split() and join() function.
def main():
    s = input(" Enter a String : ")

    print(f" Your String is : {s}", end="\n .\n .\n")

    while True:
        sp = input(" Type 'S' to split your String from blank spaces : ")
        if sp == 'S':
            s1 = s.split()
            break
        else:
            print(" !!Wrong input!!", end="\n .\n .\n")

    while True:
        print(f"\n Your distorted string is : {s1}")
        jn = input(" Type 'J' to join your distorted string : ")
        if jn == 'J':
            j = input(" Chose the character with which you would like to join your string ex; \".\" , \",\" , \"-\" , "
                      " etc (press blank space to join by blank spaces) : ")
            global s2
            s2 = j.join(s1)
            break
        else:
            print(" !!Wrong input!!", end="\n .\n .")

    print(f" Your new String formed after joining is : {s2}", end="\n .\n .\n")


# Calling function.
main()


# Creating loop for running program multiple times.
while True:
    action = input(" Want to try another String ? (y,n) : ")
    if action == 'y':
        print("\n .\n .\n")
        main()
    elif action == 'n':
        print("\n .\n .\n")
        print(" !!THANK YOU!!\nHave a nice day :)")
        break
    else:
        print(" .\n .\n Please reply 'y' for Yes and 'n' for No.")
        continue
