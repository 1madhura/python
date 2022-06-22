# Get user input as comma seperated numbers and then multiply the numbers

txt=input("enter comma seperated numbers:")
value=txt.split(",")
print("the numbers entered are:",value)
product=1
for num in value:
    product=product*int(num)
print("the product of all the numbers entered is:",product)
