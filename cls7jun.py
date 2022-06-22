Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
age=input("enter your age:\n")
enter your age:
25
type(age)
<class 'str'>
age=int(input("enter your age:\n"))
enter your age:
45
type(age)
<class 'int'>
age=float(input("enter your age:\n"))
enter your age:
65
type(age)
<class 'float'>
print("the age you entered:",age)
the age you entered: 65.0
age=bool(input("enter your age:\n"))
enter your age:
34
type(age)
<class 'bool'>
print(age)
True
mathsscore,sciencescore= float(input("enter your maths score\n")),float("enter your science score\n"))
SyntaxError: unmatched ')'
mathsscore,sciencescore= float(input("enter your maths score\n")),float(input("enter your science score\n"))
enter your maths score
67
enter your science score
78
text="hello world"
text.count('o')
2
text.count('a')
0
text.find('world')
6
text.removesuffix('world')
'hello '
print(text)
hello world
text.rstrip()
'hello world'
text='work hard.you can achieve anything'
text.split("  ")
['work hard.you can achieve anything']
text=text.split(".")
text='work hard.\n you can achieve anything\n'
print(text)
work hard.
 you can achieve anything

text.replace("hard","smart")
'work smart.\n you can achieve anything\n'
print(text)
work hard.
 you can achieve anything

text=text.replace("hard","smart")
text.replace("hard","smart")
'work smart.\n you can achieve anything\n'
text='work hard.you can achieve anything'
text.split(",")
['work hard.you can achieve anything']
text.split(" ")
['work', 'hard.you', 'can', 'achieve', 'anything']
text.split(".")
['work hard', 'you can achieve anything']
