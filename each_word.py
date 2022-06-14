def word_count(string):
	c=dict()
	word=string.split()
	for i in word:
		if i in c:
			c[i] +=1
		else:
			c[i]=1
	return c
string=input("enter the string:")
print("Word and how many times they occure:",word_count(string))

