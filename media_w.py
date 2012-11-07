import sys
from operator import itemgetter


separator = "/"
enter = "\r\n"

if "win" in sys.platform:
	separator = "\\"
	enter = "\n"

w = {}
count = {}
strings = set([])

arquivo = open(sys.argv[1])
for line in arquivo:
	split_line = line.split()
	
	if (split_line[1],split_line[3]) not in w:
		w[(split_line[1],split_line[3])] = [0,0,0,0]
	if (split_line[1],split_line[3]) not in w:
		w[(split_line[1],split_line[3])] = [0,0,0,0]
	
	if (split_line[1],split_line[3]) not in count:
		count[(split_line[1],split_line[3])] = [0,0,0,0]
	if (split_line[1],split_line[3]) not in count:
		count[(split_line[1],split_line[3])] = [0,0,0,0]
	
	if split_line[7].split("/")[1].split("(")[0] != "0":
		w[(split_line[1],split_line[3])][0] += float(split_line[7].split("(")[1].split("%")[0])
		count[(split_line[1],split_line[3])][0] += 1
	
	if split_line[12].split("/")[1].split("(")[0] != "0":
		w[(split_line[1],split_line[3])][1] += float(split_line[12].split("(")[1].split("%")[0])
		count[(split_line[1],split_line[3])][1] += 1
	
	w[(split_line[1],split_line[3])][2] += float(split_line[17].split("(")[1].split("%")[0])
	count[(split_line[1],split_line[3])][2] += 1
	
	w[(split_line[1],split_line[3])][3] += float(split_line[22].split("(")[1].split("%")[0])
	count[(split_line[1],split_line[3])][3] += 1
	

		
f = open(sys.argv[2], "a")
w = sorted(w.items(),key=itemgetter(0),reverse=True)
user = sys.argv[1].split(separator)[1]
for position in w:
	f.write(user + ": w1 = "+position[0][0]+" w-1 = "+position[0][1] +" | correto importante = "+ str("%.2f"%(position[1][0]/count[(position[0][0],position[0][1])][0])) +"% | correto nao-importante = "+str("%.2f"%(position[1][1]/count[(position[0][0],position[0][1])][1]))+"% | falso positivo = "+str("%.2f"%(position[1][2]/count[(position[0][0],position[0][1])][2]))+"% | falso negativo= "+str("%.2f"%(position[1][3]/count[(position[0][0],position[0][1])][3]))+"%\n")
