Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
score=10
type(score)
<class 'int'>
score=19.99
type(score)
<class 'float'>
markIsAvailable=False
type(markIsAvailable)
<class 'bool'>
print(12)
12
print(12>8)
True
print(12<8)
False
print(12==8)
False
print(12==12)
True
a=12
b=8
type(a>b)
<class 'bool'>
bool(4)
True
bool(1)
True
bool(-4)
True
bool(0)
False
bool(19.99)
True
bool("hi")
True
bool("hello")
True
bool("")
False
score(none)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    score(none)
NameError: name 'none' is not defined. Did you mean: 'None'?
score(None)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    score(None)
TypeError: 'float' object is not callable
Score=None
type(None)
<class 'NoneType'>
bool(None)
False
bool(False)
False
bool(0)
False
bool({})
False
bool({})
False
bool(())
False
OPERATORS
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    OPERATORS
NameError: name 'OPERATORS' is not defined
x=10
y=2
print(x+y)
12
print(x-y)
8
print(x*y)
20
print(x/y)
5.0
type(x/y)
<class 'float'>
print(x%y)
0
print(11%2)
1
print(x**y)
100
print(6**4)
1296
print(x//y)
5
print(22//7)
3
short hand operators
SyntaxError: invalid syntax
x+=6
print(x)
16
x=x+6
print(x)
22
x-=6
print(x)
16


