#program to sort the dictionary according to key and value
dic={1:"u",3:"e",4:"p",2:"o"}
print("Sort according to keys:")
for i in sorted (dic):
	print((i,dic[i]),end=" ")
print("sort acording to vlues:")
print(sorted(dic.items(),key=lambda x:(x[1],x[0])))

