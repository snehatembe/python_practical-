#Program to find the length of list
def leng(b):
	if not b:
		return 0	
	return 1 + leng(b[1::2])+leng(b[2::2])
a=[1,2,3,5,6,78,9]
print("Length of list is: ",leng(a))
	

