Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
5+2*3
11
(5+2)*3
21
score=90.5
score>90 and score<100
True
score>96 and score<100
False
scoreIsAvailable=True
print(scoreIsAvailable and (not scoreIsAvailable))
False
score>92 or score<100
True
score==85 or score<90
False
print("your score has been published:\n",scoreIsAvailable,"and your score is:")
your score has been published:
 True and your score is:
name=input("enter the name:\n")
enter the name:
Madhura
type(name)
<class 'str'>
print(name)
Madhura
print("the name that you have entered:")
the name that you have entered:
print("the name that you have entered:",name)
the name that you have entered: Madhura
location=input("enter the city and the state seperated by\n")
enter the city and the state seperated by
Banglore,KA
print(location)
Banglore,KA
location.split(",")
['Banglore', 'KA']
splitLocation=location.split(",")
type(splitLocation)
<class 'list'>
score=input("enter the score\n")
enter the score
97
type(score)
<class 'str'>
location=input("enter the city and the state seperated by\n\n\n\n\n")
enter the city and the state seperated by




enter the city and the state seperated by
name=malayalam
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    name=malayalam
NameError: name 'malayalam' is not defined
palindrom
name=input("enter the name\n")
enter the name
malayalam
palindrome(name)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    palindrome(name)
NameError: name 'palindrome' is not defined
