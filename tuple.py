# tuple

tup1=(10,140,25,23,90,65,55,100,125,35,70,80)
list1=[]
for x in tup1:
    print(x)
    if x<100 and x%5==0 and x%7==0:
        list1.append(x)
print(tup1)
print("result is:",list1)
