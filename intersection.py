def intersection(li1,li2):
	li3=[value for value in li1 if value in li2]
	return li3
li1=[]
a=int(input("Enter the length of the list ="))
print("Enter the list:")
for i in range(a):
	b=int(input())
	li1.append(b)
li2=[]
c=int(input("Enter the length of the list ="))
print("Enter the list:")
for i in range(c):
	d=int(input())
	li2.append(d)
print("Intersection of two list is:",intersection(li1,li2))
