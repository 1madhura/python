

text="malayalam" [::-1]
print(text)
text="hello" [::-1]
print(text)



text=input("Practice makes man perfect")
print(text)[0:7]



text=input("Enter text:")
vowels = 0
for i in text:
      if(i=='a'or i=='e'or i=='i'or i=='o'or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
          vowels = vowels+1
print("Number of vowels are:\n")
print(vowels)



def isPalindrome(s):
    return s == s[::-1]
s = "MALAYALAM"
ans = isPalindrome(s)

if ans:
     print('YES')
else:
     print('NO')



def isPalindrome(s):
    return s == s[::-1]
s = "12321"
ans = isPalindrome(s)

if ans:
     print('YES')
else:
     print('NO')



def isPalindrome(s):
    return s == s[::-1]
s = "MADHURA"
ans = isPalindrome(s)

if ans:
     print('YES')
else:
     print('NO')     
