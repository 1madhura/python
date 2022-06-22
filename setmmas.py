#set mmsa
print("starting set:")
list1=[45,5,67,89,124]
list2=[3,78,23,12]
myset=set()
myset.update(list1,list2)
print("set is:",myset)
print("minimum number:",min(myset))
print("maximum number:",max(myset))
print("sum of the numbers:",sum(myset))
print("average:",sum(myset)/len(myset))
print("the sorted set:",sorted(myset,reverse=True))

