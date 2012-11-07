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
		f_in = open(sys.argv[1],"r")
		for line in f_in:
			user = line.split(":")[0]
			results[int(user.split("r")[1])] = line
		f_in.close()
		f_out = open(file_name_out,"w")
		w = sorted(results.items(),key=itemgetter(0),reverse=False)
		for r in w:
			f_out.write(r[1])
		f_out.close()

get_best_results()
