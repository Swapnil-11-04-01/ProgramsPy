# Write a program that converts strings of all uppercase characters into strings
# of all lowercase characters using the map () function.

s1 = "Hello This Amazing World!"
print(f"Initial string : {s1}")

s2 =" ".join(list(map(lambda s : s.lower(), s1.split())))

print(f"Updated string : {s2}")