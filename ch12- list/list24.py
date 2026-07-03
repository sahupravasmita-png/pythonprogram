mark =[0,0,0,0]
for i in range(len(mark)):
	print(f"enter mark{i+1}")
	mark[i]=int(input())
tot=0
for i in range(len(mark)):
	print(f"mark{i+1}={mark[i]}")
	tot+=mark[i]
print("total mark=",tot)
print("avg mark=",tot/len(mark))