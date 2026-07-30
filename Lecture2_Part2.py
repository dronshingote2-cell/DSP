list1=[20,45,12,"Apple", "Banana", 34, 56]
list2=[1,2,3,4,5,6,7,8,9]
list3=["Cherry", "Water", "Grapes", "Pear", "Mango"]
list4=[]
print("Enter 10 items in list4 :")
for i in range(10):
    item = input(f"Enter item {i+1}: ")
    list4.append(item)
print("First Item of List:", list2[0])
print("Last Item of List:", list2[-1])
print("Second Item of List:", list2[1])
print("Item at Index 4 in list:", list2[4])
print("Items from Index 2 to 5 in list:", list2[2:6])
print("Displaying all items from list using loops :")
for i in range(len(list2)):
    print(list2[i])
print("Enter the first and last item which needs to be changed from list :")
x=int(input("Enter the first item to change: "))
y=int(input("Enter the last item to change: "))
list2[0]=x
list2[-1]=y
print("List after changing first and last item:", list2)
r=int(input("Enter the  item you want to change in list at index 3: "))
list2[3]=r
print("List after changing item at index 3:", list2)
print("Updating 2 Items using slice in list:")
list2[1:3]=[11, 22]
print("List after updating 2 items using slice:", list2)
index_of_item_change = int(input("Enter the index of item you want to change in list: "))
new_value = int(input("Enter the new value: "))
list2[index_of_item_change] = new_value
print("List after changing item at index", index_of_item_change, ":", list2)
print("Deleting first, last and item at index 2 in list:")
del list2[0]
del list2[-1]
del list2[2]
print("List after deletion:", list2)
print("Deleting items from index 3 to 5 in list:")
del list2[3:6]
print("List after deletion:", list2)
print("Length of list:", len(list2))
print("Finding the if a value is present in list:")
value = int(input("Enter a value to search for: "))
if value in list2:
    print(f"{value} is present in list")
else:
    print(f"{value} is not present in list")
print("Counting how many times a value is repeated in list:")
value = int(input("Enter a value to count: "))
count = list2.count(value)
print(f"{value} is repeated {count} times in list")
print("Reversing the list:")
list2.reverse()
print("List after reversing:", list2)
print("Sorting the list:")
list2.sort()
print("List after sorting:", list2)