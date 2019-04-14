def builddictionary(filename):
	file = open(filename,"r")
	file.readline() #跳過第一行
	md = {}
	for line in file:
		line = line.strip() #把換行符號拿掉
		data = line.split(",") #以逗號為分界變成一個list
		if data[0]=="040": #summary level="040"代表的是state，非county，所以那一列的資料會是所有county的相加
			continue
		else:
			countyname = data[6]
			statename = data[5]
			countyid = (statename,countyname) #因為county名稱會重複，所以要將州名加進來當各county的unique id
			countypop = int(data[7])
			level= data[0]
			popest2010 = int(data[9])
			popest2011 = int(data[10])
			popest2012 = int(data[11])
			popest2013 = int(data[12])
			popest2014 = int(data[13])
			popest2015 = int(data[14])
			alldata = [level,countypop,popest2010,popest2011,popest2012,popest2013,popest2014,popest2015]
			md[countyid] = alldata
	file.close()
	return md
census = builddictionary("census.csv")

def statelist(md): #產生所有state名的的list
	state = []
	for k in md:
		statename = k[0]
		if statename in state:
			continue
		else:
			state.append(statename)
	return state
state = statelist(census)


###################################3.(1)#############################################
def answer31(md):	
	outcome1=[]
	for s in state:
		count = 0
		for d in md:
			if d[0] == s:
				count+=1
		outcome1.append([count,s])
	outcome1.sort(reverse = True) #各state的county數由大排到小
	return outcome1[0][1] #取出有最多county的state，也就是outcome1的第一個list，回傳該list的state名稱
answer3_1 = answer31(census)
print(answer3_1)
###################################3.(1)#############################################

###################################3.(2)#############################################
def answer32(md):
	statetop3populous = {} #該dictionary的key是state，value是人口前三高的county名稱和人口數
	for s in state:
		outcome2=[] #存放各state人口前三高的county名稱和人口數
		for i in range(3): #找出每個state前三個人口最高的county
			highest = 0
			highestcounty = ()
			for d in md:
				if d[0] == s:
					if [d,md[d][1]] in outcome2: #若該county已在名單內則跳過
						continue
					elif md[d][1]>highest:
						highest = md[d][1]
						highestcounty = d
			outcome2.append([highestcounty,highest])
		statetop3populous[s] = outcome2

	usatop3populous = {} #該dictionary的key是state，value是人口前三高的county的總人口數
	for s in statetop3populous:
		top3poptotal = 0
		top3poptotal = statetop3populous[s][0][1]+statetop3populous[s][1][1]+statetop3populous[s][2][1]
		usatop3populous[s] = top3poptotal

	want = [] #存放只考慮各state前三多county人口數的情況下，人口最多的前三state
	higheststate = ""
	for i in range(3):
		higheststatepop = 0
		for s in usatop3populous:
			if s in want:
				continue
			elif usatop3populous[s] > higheststatepop:
				higheststatepop = usatop3populous[s]
				higheststate = s
		want.append(higheststate)
	return want
answer3_2 = answer32(census)
print(answer3_2)
###################################3.(2)#############################################

###################################3.(3)#############################################
def answer33(md):
	bigdiff = 0
	bigdiffcounty = ()
	for d in md:
		popest6y = [md[d][2],md[d][3],md[d][4],md[d][5],md[d][6],md[d][7]]
		diff = max(popest6y) - min(popest6y)
		if diff > bigdiff:
			bigdiff = diff
			bigdiffcounty = d
	return bigdiffcounty  
answer3_3 = answer33(census)
print(answer3_3[0],answer3_3[1])
###################################3.(3)#############################################
