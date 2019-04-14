input = open("candy_input1.txt","r")
#input = open("candy_input2.txt","r")
candy = input.readlines()
input.close()
mycandy = []
for i in range(len(candy)):
	mycandy.append(candy[i].split(','))

for j in range(len(mycandy)):
	mycandy[j][len(mycandy[0])-1] = mycandy[j][len(mycandy[0])-1].strip()
key = True
while key:
	m = 0
	lol = []
	#檢查橫的
	while  m < (len(mycandy)):
		n = 0
		while n < (len(mycandy[0])-2):
			if (mycandy[m][n] != "0") and (mycandy[m][n] == mycandy[m][n+1] == mycandy[m][n+2]):
				lol.append([m,n])
				lol.append([m,n+1])
				lol.append([m,n+2])
			n = n + 1
		m = m + 1
	#檢查直的
	n = 0
	while  n < (len(mycandy[0])):
		m = 0
		while m < (len(mycandy)-2):
			if (mycandy[m][n] != "0") and (mycandy[m][n] == mycandy[m+1][n] == mycandy[m+2][n]):
				lol.append([m,n])
				lol.append([m+1,n])
				lol.append([m+2,n])
			m = m + 1
		n = n + 1
	if len(lol)==0:
		key = False
		break
	#刪掉重複的
	aoa = sorted(lol)
	now = aoa[0]
	k = 1
	while k < len(aoa):
		if aoa[k] == now:
			lol.remove(aoa[k])
		else:
			now = aoa[k]
		k = k + 1
	aoa = sorted(lol)
	#要消掉的變-1
	for x in aoa:
		mycandy[x[0]][x[1]] = "-1"
	#算補0的個數
	p = 0
	ss = [] #每行要消除的個數
	while p < len(mycandy[0]):
		q = 0
		count = 0
		while q < len(mycandy):
			if mycandy[q][p] == "-1":
				count = count + 1
			q = q + 1
		ss.append(count)
		p = p + 1
	#要消掉的位置照行排
	pop = []
	for h in range(len(mycandy[0])):
		for g in aoa:
			if g[1] == h:
				pop.append(g) 
	#crush
	r = 0
	while r < len(mycandy[0]):
		if ss[r] > 0:
			kk = []
			for s in pop:
				if s[1] == r:
					kk.append(s) #某一行要消除的座標
			t = 0
			while t < ss[r]:
				target = kk[t]
				u = target[0]
				while u > 0:
					mycandy[u][r] = mycandy[u-1][r]
					u = u - 1
				t = t + 1
			v = 0
			while v < ss[r]:
				mycandy[v][r] = "0"
				v = v + 1
		r = r + 1
print(mycandy)
file_name = "candy_output1.txt"
#file_name = "candy_output2.txt"
myfile = open(file_name,"w")
myformate="%s,%s,%s,%s,%s\n"
z=0
while z < len(mycandy):
	myfile.writelines(myformate%(mycandy[z][0],mycandy[z][1],mycandy[z][2],mycandy[z][3],mycandy[z][4]))
	z+=1