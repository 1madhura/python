#Program to find largest number in the given numbers
num1 = 25
num2 = 15
num3 = 12
if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3
print("the largest number is:",largest)
