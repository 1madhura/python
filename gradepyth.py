'''
# enter the marks as user input
if the marks entered is b/w 90 to 100 --> A+
if the marks entered is b/w 80 to 90 --> A
if the marks entered is b/w 70 to 80 --> B+
if the marks entered is b/w 60 to 70 --> B
if the marks entered is b/w 50 to 60 --> C
otherwise the grade is "F"
'''

grade=" "
marks=int(input("enter the marks:"))
if(marks>=90 and marks<=100):
    grade="A+"
elif(marks>=80 and marks<=90):
    grade="A"
elif(marks>=70 and marks<=80):
    grade="B+"
elif(marks>=60 and marks<=70):
    grade="B"
elif(marks>=50 and marks<=60):
    grade="C"
else:
    grade="F"
print("the grade obtained is:",grade)
