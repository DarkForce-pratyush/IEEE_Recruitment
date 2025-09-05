#inputting two lists from the user
list1=[]
list2=[]
n1= int(input("Enter number of elements of list 1: "))
n2= int(input("Enter number of elements of list 2: "))

print("Enter elements of list 1: ")
for i in range(n1):
    list1.append(int(input()))

print("Enter elemnets of list 2: ")   
for i in range(n2):
    list2.append(int(input()))

# Find the intersection without duplicates using set intersection
intersection = list(set(list1) & set(list2))

print(intersection)
