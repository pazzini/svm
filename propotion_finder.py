#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from xml.dom.minidom import parse

separator = "/"

if "win" in sys.platform:
	separator = "\\"

targets_total = {"important":0.,"not-important":0.}	

if os.path.exists("saidas_users\\media_users".replace("\\",separator)):
	f = open("saidas_users\\media_users".replace("\\",separator))
	saida = ""
	for i in f:
		targets_total["important"] = 0
		targets_total["not-important"] = 0
		line = i.split(" ")
		#pegar o userx pra saber de qual user se trata
		user = line[0].split(":")[0]
		w1 =  line[3]
		file_user_path = parse(("users\\"+user+".xml").replace("\\",separator))
		tables = file_user_path.getElementsByTagName("table")
		for item in tables:
			colum = item.getElementsByTagName("column")
			if colum.item(33).childNodes[0].nodeValue == "important":
				targets_total["important"] += 1
			else:
				targets_total["not-important"] += 1
		#print user + " | important: "+str(targets_total["important"])+" | not-important: " + str(targets_total["not-important"])
		saida += user + " | important: "+str(targets_total["important"]) +"("+str("%.2f"%(100*(targets_total["important"] / float(targets_total["important"] + targets_total["not-important"])))) +"%)"+ " | w1: " + w1 + " | total: " + str(targets_total["important"] + targets_total["not-important"])+"\n"
	file_saida = open("propotion_finder.txt", "w")
	file_saida.write(saida)
	
else:
	print "arquivo media_users nao encontrado"
