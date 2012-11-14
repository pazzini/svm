#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from operator import itemgetter

separator = "/"
enter = "\r\n"

#para verificar se o sistema operacional e windows ou linux, para escolher o separador e o enter adequado
if "win" in sys.platform:
	separator = "\\"
	enter = "\n"

#ele pega no arquivo saidas_users/media_users o ultimo resultado de cada usuario
#o ultimo resultado de cada usuario e o melhor resultado para aquele usuario
#ele bota a saida num arquivo chamado "filtered_results.txt"
def get_best_results():
	if len(sys.argv) < 2:
		print "Quantidade de parametros incorreta"
		return False
	else:
		if len(sys.argv) == 3:
			file_name_out = sys.arv[2]
		else:
			file_name_out = "filtered_results.txt"
		results = {}
		ws = {}
		f_in = open(sys.argv[1],"r")
		for line in f_in:
			user = line.split(":")[0]
			acc_pos = float(line.split("correto importante = ")[1].split("%")[0])
			acc_neg = float(line.split("correto nao-importante = ")[1].split("%")[0])
			if abs(acc_pos - acc_neg) < 10.:
				results[int(user.split("r")[1])] = line
				w_pos = line.split("w1 = ")[1].split()[0]
				w_neg = line.split("w-1 = ")[1].split()[0]
				ws[user.split("r")[1]+"_w"] = (w_pos,w_neg)
		f_in.close()
		f_out = open(file_name_out,"w")
		w = sorted(results.items(),key=itemgetter(0),reverse=False)
		for r in w:
			f_out.write(r[1])
		f_out.write("[")
		l = 1
		for i in range(1,185):
			if (str(i)+"_w") in ws:
				f_out.write("["+ws[str(i)+"_w"][0]+","+ws[str(i)+"_w"][1]+"]")
			else:
				f_out.write("[99.0,1.0]")
			if i != 184:
				f_out.write(",")
			if l == 10:
				f_out.write("\n")
				l = 0
			else:
				l += 1
		f_out.write("]")
		f_out.close()

get_best_results()
