#python programtofind tuples which have allelements divisible by k
t=((1,4,7),(8,45,35,89,97),(90,24,67,68))
k=2
ans=[]
for i in t:
	for i1 in i:
		if i1%k==0:
			ans.append(i1)
print(ans)
