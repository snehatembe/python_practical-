#program for telephone 
dic={}
for i in range(10):
	n=str(input("Enter name:"))
	p=int(input("Enter phone number:"))
	dic[n]=p
print(dic)
#find
n1=str(input("Enter key:"))
if n1 in dic:
	print("It find")
	p2=int(input("Enter new phone no.:"))
	dic[n1]=p2 #replace
	print("Dicstionary after replacing phone no.:",dic)
#delete
del dic[n1]
print("Dictionary after deleting :",dic)


