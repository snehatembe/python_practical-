String=input("Enter the string:")
word=input("Enter the word:")
a=[]
c=0
a=String.split(" ")
for i in range(0,len(a)):
	if(word==a[i]):
		c=c+1
print("The word repeat ",c,"times")
