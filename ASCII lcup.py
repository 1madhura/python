# To generate all lower case and upper case alphabets using ASCII values

print("the following are the ASCII codes generated lower case alphabets\n")
for temp in range(97,123):
    print(chr(temp),end=' ')
print("\nthe following are the ASCII codes generated upper case alphabets\n")
for temp in range(65,91):
    print(chr(temp),end=' ')
