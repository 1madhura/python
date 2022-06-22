'''
tax calculation
get anuual income from user
calculate tax based on income
upto 250000 no tax
240000 to 500000 --> 5%
500000 to 1000000 --> 20%
1000000 and above --> 30%
'''


annincome=int(input("enter annual income:"))
tax=0
tax30=0
tax20=0
tax5=0
if(annincome>1000000):
    tax30=(annincome-1000000)*0.3
    tax20=500000*0.2
    tax5=250000*0.05
elif(annincome>500000):
    tax20=(annincome-500000)*0.2
    tax5=250000*0.05
elif(annincome>250000):
    tax5=(annincome-250000)*0.05
else:
    print("you have  no tax this year")
tax=tax30+tax20+tax5
print("total tax is:",tax)
 
