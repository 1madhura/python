#adding items into shopping cart

print("shopping cart")
item_list=[]
while(True):
    item=input("enter the item name:")
    qty=int(input("enter quantity:"))
    each_item=[]
    each_item.append(item)
    each_item.append(qty)
    item_list.append(each_item)
    more=input("do you want to continue(yes/no):")
    if(more=="no"):
        break
print("you have purchased:",item_list)
