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
uni=list(set().union(li1,li2))
print("the union of two lists is =",uni)
