def builddictionary(filename):
	file = open(filename,"r")
	file.readline() #跳過第一行
	file.readline() #跳過第二行
	md = {}
	for line in file: #一行一行讀
		line = line.strip() #把換行符號拿掉
		data = line.split(",") #以逗號為分界變成一個list

		stoppoint = data[0].find("?") #將國家名稱格式改一下，只保留問號前的文字
		if(stoppoint != -1): #若找不到"?"的index，則data[0].find("?")會是-1
			country = data[0][:stoppoint]
		else:
			country = data[0]
		
		summertimes = int(data[1])
		s1 = int(data[2])
		s2 = int(data[3])
		s3 = int(data[4])
		s123 = int(data[5])
		wintertimes = int(data[6])
		w1 = int(data[7])
		w2 = int(data[8])
		w3 = int(data[9])
		w123 = int(data[10]) 
		combinetimes = int(data[11])
		c1 = int(data[12])
		c2 = int(data[13])
		c3 = int(data[14])
		c123 = int(data[15])
		alldata = [summertimes,s1,s2,s3,s123,wintertimes,w1,w2,w3,w123,combinetimes,c1,c2,c3,c123]
		md[country] = alldata
	file.close()
	return md

olympics = builddictionary("olympics.csv")
del olympics["Totals"]


##############2.(1)###############################
def answer21(d):
	maxcount = 0
	maxcountry = ""
	for i in d:
		if(d[i][1] > maxcount):
			maxcount = d[i][1]
			maxcountry = i
	return maxcountry
print(answer21(olympics))
##############2.(1)###############################



##############2.(2)###############################
def answer22(d):
	biggestdiff = 0
	biggestdiffcountry = ""
	for i in d:
		diff = abs(d[i][1]-d[i][6])
		if (diff > biggestdiff):
			biggestdiff = diff
			biggestdiffcountry = i
	return biggestdiffcountry
print(answer22(olympics))
##############2.(2)###############################


##############2.(3)###############################
def answer23(d):
	highestrate = 0
	highestratecountry = ""
	for i in d:
		if (d[i][1]>0 and d[i][6]>0):
			rate = (abs(d[i][1]-d[i][6]))/(d[i][1]+d[i][6])
			if(rate > highestrate):
				highestrate = rate
				highestratecountry = i
	return highestratecountry
print(answer23(olympics))
##############2.(3)###############################