tup = (12,19,10,8,51,93,55,43,23,14)
print("Original tuple:", tup)
for i in range(len(tup)):
    print(f"Element {i+1}:", tup[i])
li=list(tup)
print("List created from tuple for adding elements:", li)
li[3]=67
tup=(tuple)(li)
print("Tuple after modification:", tup)
li=list(tup)
print("List created from modified tuple for deleting elements:", li)
del li[5]
tup=(tuple)(li)
print("Tuple after deleting an element:", tup)