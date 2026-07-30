list1 = []
for i in range(10):
    num = int(input(f"Enter number {i+1} in tuple1: "))
    list1.append(num)
tup1 = tuple(list1)
list1 = list(tup1)
n = len(list1)
for i in range(n):
    for j in range(0, n - i - 1):
        if list1[j] > list1[j + 1]:
            temp = list1[j]
            list1[j] = list1[j + 1]
            list1[j + 1] = temp
tup1 = tuple(list1)
print("The sorted tuple using bubble sort is: ", tup1)