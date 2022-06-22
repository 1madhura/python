# create a dict having the values as list. iterate and find the sum,max,min,avg

dict1={100:[56,129],250:[56,67,78,90],350:[32,10,8,5]}
list1=[]
for key in dict1:
    valuestr=""
    for value in dict1[key]:
        valuestr=valuestr+str(value)+" "
    print(key," ",valuestr)
    list1.extend(dict1[key])
print("total:",sum(list1))
print("maximum:",max(list1))
print("minimum:",min(list1))
print("average:",sum(list1)/len(list1))
