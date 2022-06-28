#program to convert two list into a dictionary
l1=[9,46,23,90,12]
l2=["a","b","m","p","o"]
dic={l1[i]:l2[i] for i in range(len(l1))}
print(dic)
