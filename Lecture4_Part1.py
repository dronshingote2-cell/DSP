set1 = {10,20,30,40}
for i in set1:
    print(i)
set1.add(50)
print("After adding 50:", set1)
set1.update([65,75])
print("After updating with [65,75]:", set1)
set1.remove(40)
print("After removing 40:", set1)
del set1
print("Set deleted.")
set_a={10,20,30,40}
print("Set A:", set_a)
set_b={30,40,50,60}
print("Set B:", set_b)
for i in set_a:
    if i in set_b:
        print(i, "is present in both sets.")
    else:
        print(i, "is not present in set B.")
set_c=set_a.union(set_b)
print("Set C (union of A and B):", set_c)
set_d=set_a.intersection(set_b)
print("Set D (intersection of A and B):", set_d)
set_e=set_a.difference(set_b)
print("Set E (difference of A and B):", set_e)