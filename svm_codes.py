#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import math
import tweet_list
import methods
import sys
from svmutil import *
import svm_class
import time
import pdb

separator = "/"
del_command = "rm"

if "win" in sys.platform:
	separator = "\\"
	del_command = "del"


#lista de todos os features presentes em um tweet
features = ["text", "status_created_at","source","in_reply_to_twitter_status_id","in_reply_to_twitter_user_id","in_reply_to_twitter_user_screen_name","retweeted_twitter_status_id",
			"retweet_count","retweeted","geo","contributors","name","screen_name","location","description","url","protected","followers_count","friends_count","favourites_count",
			"user_created_at","utc_offset","time_zone","geo_enabled","statuses_count","lang","contributors_enabled","listed_count","is_translator","favorited","entity_user_mention",
			"entity_hashtag","entity_url","manual_classification"]

"""inicialização de todas as variaveis
-Dictionary é um dicionario de dicionarios, ele contem
os valores de todos os features, separadamente, presentes
na base de treinamento.
-ws é um vetor com os melhores valores para o parametros weight
utilizado pelo libsvm, para os nove usuários principais.
-target conjunto de labels que um tweet pode receber
-proportion valor padrao para divisão da proporsão de tweets em
base de treinamento e de teste, valor normal 70% treinamenteo
30% teste.
-fold: numero de conjuntos utilizado no cross-validation
-repetition é o numero de repetições que o algoritmo fara mudando
o valor do parametro w, o w é alterado segundo o parametro change
-change valor de alteração do w
-repetition_no_changing é o numero de vezes que o codigo vai rodar
sem mudar o w, usado para ter varios resultados sobre a mesma base
30 vezes é um bom valor para tirar média
-find é parametro para ativar metodo de busca pelo parametro weight
que de resultados aceitaveis.
-list_results é usado pelo metodo find para manter os ultimos
resultados encontrados
-fast_mode usa metodo do libsvm par fazer cross-validation
"""
dictionary = {}
feature_to_do = [0,2,7,8,12,13,14,17,18,19,22,25,27,29,30,31]
#ws = [[99.57,0.43],[99.75,0.25],[98.25,1.75],[99.43,0.57],[99.92,0.08],[99.97,0.03],[99.5,0.5],[99.17,0.83],[97.04,2.96]]
ws = [[96.0,4.0],[98.0,2.0],[92.0,8.0],[97.0,3.0],[99.375,0.625],[99.5625,0.4375],[97.5,2.5],[97.0,3.0],[96.0,4.0],[92.0,8.0],
	[99.859375,0.140625],[99.625,0.375],[99.75,0.25],[99.78125,0.21875],[99.25,0.75],[99.59375,0.40625],[99.625,0.375],[99.6875,0.3125],[99.90625,0.09375],[99.59375,0.40625],[99.0,1.0],
	[99.75,0.25],[99.6875,0.3125],[99.25,0.75],[99.25,0.75],[99.78125,0.21875],[98.0,2.0],[99.25,0.75],[99.8671875,0.1328125],[99.875,0.125],[99.8125,0.1875],[99.78125,0.21875],
	[99.6875,0.3125],[99.625,0.375],[99.703125,0.296875],[99.75,0.25],[98.0,2.0],[99.8125,0.1875],[99.625,0.375],[98.0,2.0],[99.25,0.75],[99.75,0.25],[99.625,0.375],
	[99.90625,0.09375],[99.25,0.75],[99.71875,0.28125],[99.5,0.5],[99.4375,0.5625],[99.4375,0.5625],[99.59375,0.40625],[99.6875,0.3125],[99.46875,0.53125],[99.25,0.75],[99.0,1.0],
	[99.0,1.0],[99.25,0.75],[99.625,0.375],[99.5,0.5],[99.71875,0.28125],[99.0,1.0],[99.71875,0.28125],[99.75,0.25],[99.4375,0.5625],[99.0,1.0],[99.375,0.625],
	[99.7890625,0.2109375],[99.71875,0.28125],[99.0,1.0],[99.8984375,0.1015625],[98.0,2.0],[99.75,0.25],[99.0,1.0],[99.875,0.125],[99.5,0.5],[99.625,0.375],[99.0,1.0],
	[99.9453125,0.0546875],[99.75,0.25],[99.5,0.5],[99.5,0.5],[99.875,0.125],[99.90625,0.09375],[99.5,0.5],[99.5625,0.4375],[98.5,1.5],[99.71875,0.28125],[99.75,0.25],
	[99.5625,0.4375],[99.78125,0.21875],[99.75,0.25],[99.4375,0.5625],[99.71875,0.28125],[99.5,0.5],[99.734375,0.265625],[99.6875,0.3125],[99.375,0.625],[99.71875,0.28125],[99.5625,0.4375],
	[99.0,1.0],[99.75,0.25],[99.71875,0.28125],[99.25,0.75],[99.703125,0.296875],[99.859375,0.140625],[99.78125,0.21875],[99.5625,0.4375],[99.0,1.0],[99.921875,0.078125],[99.625,0.375],
	[99.75,0.25],[99.75,0.25],[99.890625,0.109375],[99.65625,0.34375],[99.59375,0.40625],[99.375,0.625],[99.859375,0.140625],[99.5,0.5],[99.65625,0.34375],[99.125,0.875],[99.0,1.0],
	[99.0,1.0],[99.0,1.0],[99.375,0.625],[99.5,0.5],[99.75,0.25],[99.75,0.25],[99.5,0.5],[99.5,0.5],[99.75,0.25],[99.5,0.5],[99.859375,0.140625],
	[99.65625,0.34375],[99.75,0.25],[98.0,2.0],[99.25,0.75],[99.0,1.0],[99.796875,0.203125],[99.375,0.625],[99.25,0.75],[99.86328125,0.13671875],[99.5,0.5],[99.625,0.375],
	[99.75,0.25],[99.0,1.0],[99.0,1.0],[99.625,0.375],[99.0,1.0],[99.25,0.75],[99.375,0.625],[99.375,0.625],[99.625,0.375],[99.7734375,0.2265625],[99.0,1.0],
	[99.625,0.375],[99.0,1.0],[99.828125,0.171875],[99.375,0.625],[99.92578125,0.07421875],[99.625,0.375],[99.703125,0.296875],[99.5,0.5],[99.75,0.25],[99.5625,0.4375],[99.0,1.0],
	[99.875,0.125],[99.0,1.0],[99.5625,0.4375],[99.5625,0.4375],[99.0,1.0],[99.5,0.5],[99.71875,0.28125],[99.75,0.25],[99.890625,0.109375],[99.90625,0.09375],[98.75,1.25],
	[99.375,0.625],[99.8515625,0.1484375],[99.375,0.625],[99.0,1.0],[99.59375,0.40625],[99.765625,0.234375],[99.78125,0.21875],[99.625,0.375],[99.78125,0.21875]]

proportion = 70
fold = 0
repetition = 1
change = 0.01
repetition_no_changing = 1
find = False
list_results = []
fast_mode = False
fm_training_base = None
file_test = ""
precision = 10
zeros = {}

"""
Metodo utilizado para fazer o cross-validation
o parametro -q é para que o libsvm realize menos impressões
"""
def train_predict_fold(tam = 10,parameter = "-q "):
	global fm_training_base
	pos = 0
	previous_times = []
	for k in range(5):
		previous_times.append(20.0)
	
	for i in range(tam):
		
		t1 = time.time()
		
		if fast_mode:
			
			if (fm_training_base == None):
				tweets.set_training_base(tweets.get_documents_list())
				svm.create_dictionary(feature_to_do)
				l_training,v_training = svm.create_base_list(tweets.get_documents_list(),feature_to_do)
				fm_training_base = [l_training,v_training]
				
			train_predict(fm_training_base,[],parameter + " -v " + str(tam))
			
			if not find:
				fm_training_base = None
			
			print "Duration: %.3f s"%(time.time() - t1)
			break
		else:
			temp_training_base = []
			temp_test_base = []
			temp_training_base = tweets.get_documents_list()
			set_tam = int(tweets.get_documents_list_tam() // tam)
			for k in range(set_tam):
				temp_test_base.append(temp_training_base[(i*set_tam)])
				del temp_training_base[(i*set_tam)]
			tweets.set_training_base(temp_training_base)
			
			svm.create_dictionary(feature_to_do)
			#save_previously_searched()

			l_training,v_training = svm.create_base_list(temp_training_base,feature_to_do)
			training_base = [l_training,v_training]
			tweets.set_test_base(temp_test_base)
			l_test,v_test = svm.create_base_list(temp_test_base,feature_to_do)
			
			if len(l_test) != 0:
				test_base = [l_test,v_test]
				train_predict(training_base,test_base,parameter)
			
		#save_previously_searched()
		
		t2 = time.time() - t1
		previous_times[pos] = t2
		pos += 1
		if pos == 5: pos = 0
		et = (tam - i) * (sum(previous_times) / 5.)
		horas = int(et // 3600)
		minutos = int((et % 3600) // 60)
		segundos = int((et % 3600) % 60)
		print "Duration: %.3f s"%(time.time() - t1)
		print i+1, "/", tam, "ET:", str(horas) + ":" + str(minutos) + ":" + str(segundos)

"""
Metodo que cria o modelo treinado com os tweets da base de treinamento
e testa o modelo utilizando os tweets da base de teste, chama o metodo
accuracy para detalhar melhor a divisão dos resultados encontrados.
"""
def train_predict(train_base,test_base,parameter):
	prob  = svm_problem(train_base[0], train_base[1])
	param = svm_parameter(parameter)
	m = svm_train(prob, param)
	if fast_mode:
		write_acc(m,parameter)
	else:
		p_label, p_acc, p_val = svm_predict(test_base[0], test_base[1], m, '')
		accuracy([1,-1],test_base[0],p_label,parameter)

"""Metodo que escreve em arquivo os resultados obtidos de cada teste
realizado, no formato utilizado pelo media_w
"""
def write_acc(acc,parameter):
	list_results.append([acc[1],acc[-1]])
	
	if not os.path.exists("saidas_users"):
		os.system("mkdir saidas_users")
	if not os.path.exists("saidas_users\\user".replace("\\",separator) + str(user)):
		os.system("mkdir saidas_users\\user".replace("\\",separator) + str(user))
	
	acc_important_perc = acc[1]
	total_important = int(acc["1total"])
	acc_important_num = int(acc_important_perc / 100. * total_important)
	acc_not_important_perc = acc[-1]
	total_not_important = int(acc["-1total"])
	acc_not_important_num = int(acc_not_important_perc / 100. * total_not_important)
	false_positive_perc = 100. - acc_not_important_perc
	false_positive_num = int(total_not_important - acc_not_important_num)
	false_negative_perc = 100. - acc_important_perc
	false_negative_num = int(total_important - acc_important_num)
	
	if find:
		f = open(("saidas_users\\user" + str(user) + "\\find_percentage.out").replace("\\",separator), 'a')
	else:
		f = open(("saidas_users\\user" + str(user) + "\\percentage.out").replace("\\",separator), 'a')
		
	f.write(parameter[3:].split(" -v")[0] + " correto importante = " + str(acc_important_num) + "/" + str(total_important)+"("+str("%.2f"%acc_important_perc)+"%) ")
	f.write("| correto nao-importante = " + str(acc_not_important_num) + "/" + str(total_not_important)+"("+str("%.2f"%acc_not_important_perc)+"%) ")
	f.write("| falso positivo = " + str(false_positive_num) + "/" + str(total_not_important) + "(" + str("%.2f"%false_positive_perc)+"%) ")
	f.write("| falso negativo = " + str(false_negative_num) + "/" + str(total_important) + "(" + str("%.2f"%false_negative_perc)+"%)\n")
	f.close()

"""
Metodo que recebe as possiveis classes de um tweet (labels), os reais
labels dos tweets contidos na base de teste e os labels preditos pelo
modelo, utiliza esses valores para indicar qual foi a precisão do modelo
ao predizer cada classe, e os escreve em um arquivo chamado percentage.out
na pasta do respectivo usuário.
"""
def accuracy(classes,base_test,predicted,parameter):
	acc = {}
	global list_results,zeros

	for c in classes:
		acc[c] = 0.
		zeros[c] = 0
		acc[str(c) + "total"] = 0

	for i in range(len(base_test)):
		if base_test[i] == predicted[i]:
			acc[base_test[i]] += 1.
		acc[str(base_test[i])+"total"] += 1

	for c in classes:
		if acc[str(c)+"total"] != 0:
			acc[c] *= (100. / acc[str(c)+"total"])
		else:
			#acc[c] = 100.
			acc[c] = 0.
			zeros[c] += 1
		print "class[" + str(c) + "] : "+ str("%.0f"%(acc[c]/100. * acc[str(c)+"total"])) + "(" + str("%.2f"%acc[c]) + "%)"
	if fold == 0: print "----------------------------------------"
	list_results.append([acc[1],acc[-1]])
	
	write_acc(acc,parameter)

"""
Deleta as saidas criadas
"""
def delete():
	del_command = "del"
	if "linux" in sys.platform:
		del_command = "rm"
	if os.path.exists(("saidas_users\\user" + str(user) + "\\model").replace("\\",separator)):
		os.system((del_command + " saidas_users\\user" + str(user) + "\\model").replace("\\",separator))
	if os.path.exists(("saidas_users\\user" + str(user) + "\\saida").replace("\\",separator)):
		os.system((del_command + " saidas_users\\user" + str(user) + "\\saida").replace("\\",separator))
	if os.path.exists(("saidas_users\\user" + str(user) + "\\percentage.out").replace("\\",separator)):
		os.system((del_command + " saidas_users\\user" + str(user) + "\\percentage.out").replace("\\",separator))
	#if os.path.exists(("saidas_users\\user" + str(user) + "\\media_user" + str(user)).replace("\\",separator)):
	#	os.system((del_command + " saidas_users\\user" + str(user) + "\\media_user" + str(user)).replace("\\",separator))

"""
Metodo que roda ate encontrar um parametro weight aceitavel
"""
def find_good_parameter(user):
	global list_results,repetition,repetition_no_changing,fast_mode
	mean = first_result = []
	while (user + 1) > len(first_result):
		first_result.append([0.,0.])
	ws[user][0] = 99.0
	ws[user][1] = 1.0
	change = 1.
	temp_fold = fold

	while True:
		fifteen = False
		ws[user][0] -= change
		ws[user][1] += change
		mean.append([0.,0.])
		if fold != 0:
			train_predict_fold(temp_fold,("-q -w1 " + str(ws[user][0]) + " -w-1 " + str(ws[user][1])))
			if fast_mode:
				mean[-1][0] = list_results[-1][0]
				mean[-1][1] = list_results[-1][1]
			else:
				for j in range(int(fold)):
					mean[-1][0] += list_results[-1*(1+j)][0]
					mean[-1][1] += list_results[-1*(1+j)][1]
				mean[-1][0] /= (temp_fold - zeros[1])
				mean[-1][1] /= (temp_fold - zeros[-1])
		elif fold == 0:
			svm.classification_division(proportion)
			train_predict(create_training_base(feature_to_do),create_test_base(feature_to_do),"-q -w1 " + str(ws[user][0]) + " -w-1 " + str(ws[user][1]))
			mean[-1][0] = list_results[-1][0]
			mean[-1][1] = list_results[-1][1]
		
		if first_result[user] == [0.,0.]:
			first_result[user] = list_results[0]

		if abs(mean[-1][0] - mean[-1][1]) < precision or abs(change) <= 1e-10:
			break
			
		if change > 0 and (mean[-1][1] > mean[-1][0]):
			change *= -1/2.
		
		if change < 0 and (mean[-1][1] < mean[-1][0]):
			change *= -1/2.
			
		print "rate: %.4f"%change,", weight: [%.3f,%.3f]"%(ws[user][0],ws[user][1]),", mean: [%.3f,%.3f]"%(mean[-1][0],mean[-1][1]),", diff: %.3f"%abs(mean[-1][0] - mean[-1][1])
		print "-----------------------------------"
	print "rate: %.4f"%change,", weight: [%.3f,%.3f]"%(ws[user][0],ws[user][1]),", mean: [%.3f,%.3f]"%(mean[-1][0],mean[-1][1]),", diff: %.3f"%abs(mean[-1][0] - mean[-1][1])
	print "-----------------------------------"
	os.system(("python media_w.py saidas_users\\user" + str(user+1) + "\\find_percentage.out " + "saidas_users\\user" + str(user+1) + "\\find_media_user"+str(user+1)).replace("\\",separator))
	delete()
	repetition = 1
	repetition_no_changing = 1
	fast_mode = False

"""
PARAMETERS
-f: features to be done
-p: proportion of data division. Example: -p 50, half of data will
be used on learning and half on tests
-v: cross validation. Create v parts of data of same size and use v-1
on train and test on last one, all parts are tested one time. -v max use
the size of data, training with data -1 and testing on the last one.
-t: number of times the process will be done
-r: the change of w on each time of process
-w1: the initial value of w1
-w-1: the initial value of w-1
-d: delete all files of input user
-fm: run the fast mode of cross-validation
-ft: load the first db as training base and the second db as test base,
if that methos is being used the cross-validation methos can't be used.
"""

#Main
try:
	filename = sys.argv[1]
except:
	print "No input file."
user = int(((filename.split(separator)[1]).split(".")[0])[4:])

while user > len(ws):
	ws.append([100.,0.])

for p in sys.argv:
	if p == "-f":
		feature_to_do = []
		try:
			for number in sys.argv[sys.argv.index(p)+1].split(","):
				if int(number) not in feature_to_do:
					feature_to_do.append(int(number))
		except:
			print "Parameter -f error."
			sys.exit(0)
	elif p == "-p":
		try:
			proportion = float(sys.argv[sys.argv.index(p)+1])
		except:
			print "Parameter -p error."
			sys.exit(0)
	elif p == "-v":
		try:
			if sys.argv[sys.argv.index(p)+1] == "max":
				fold = "max"
			else:
				fold = int(sys.argv[sys.argv.index(p)+1])
		except:
			print "Parameter -v error."
			sys.exit(0)
	elif p == "-t":
		try:
			repetition = int(sys.argv[sys.argv.index(p)+1])
		except:
			print "Parameter -t error."
			sys.exit(0)
	elif p == "-w1":
		try:
			ws[user-1][0] = float(sys.argv[sys.argv.index(p)+1])
		except:
			print "Parameter -w1 error."
			sys.exit(0)
	elif p == "-w-1":
		try:
			ws[user-1][1] = float(sys.argv[sys.argv.index(p)+1])
		except:
			print "Parameter -w-1 error."
			sys.exit(0)
	elif p == "-r":
		try:
			change = float(sys.argv[sys.argv.index(p)+1])
		except:
			print "Parameter -r error."
			sys.exit(0)
	elif p == "-t2":
		try:
			repetition_no_changing = int(sys.argv[sys.argv.index(p)+1])
		except:
			print "Parameter -t2 error."
			sys.exit(0)
	elif  p == "-file2":
		file_base_2 = sys.argv[sys.argv.index(p)+1]
	elif p == "-d":
		delete()
	elif p == "-find":
		find = True
	elif p == "-fm":
		fast_mode = True
	elif p == "-ft":
		file_test = sys.argv[sys.argv.index(p)+1]
		if not os.path.exists(file_test.replace("\\",separator)):
			print("Parameter file_test error")
	elif p == "-a":
		try:
			precision = float(sys.argv[sys.argv.index(p)+1])
		except:
			print "Parameter -a error."
			sys.exit(0)

tweets = tweet_list.tweet_list()
svm = svm_class.svm(tweets)
svm.load_tweets(filename)

#pdb.set_trace()

if fold == "max":
	fold = tweets.get_documents_list_tam()

if fast_mode and fold == 0:
	fast_mode = False
	print "Fast Mode desatived, missing fold value"

if tweets.get_important_tam() < 10:
	print "quantidade de tweets importantes muita baixa:",tweets.get_important_tam()
else:
	print "user" + str(user)
	if find:
		find_good_parameter(user-1)
		find = False
		#sys.exit(0)
	for i in range(repetition):
		for j in range(repetition_no_changing):
			
			if file_test != "":
				svm.load_tweets_test(file_test)
				
			if fold != 0:
				train_predict_fold(fold,("-q -w1 " + str(ws[user-1][0]) + " -w-1 " + str(ws[user-1][1])))
			elif fold == 0:
				if file_test == "":
					svm.classification_division(proportion)
				print "Proportion:",str(proportion) + "%,","training:",str(tweets.get_training_base_tam()) + ","," test:",str(tweets.get_test_base_tam())
				svm.create_dictionary(feature_to_do)
				train_predict(svm.create_training_base(feature_to_do),svm.create_test_base(feature_to_do),"-q -w1 " + str(ws[user-1][0]) + " -w-1 " + str(ws[user-1][1]))
			
		ws[user-1][0] -= change
		ws[user-1][1] += change
		#if os.path.exists(("saidas_users\\user" + str(user) + "\\media_user" + str(user)).replace("\\",separator)):
		#	os.system((del_command + " saidas_users\\user" + str(user) + "\\media_user" + str(user)).replace("\\",separator))
		os.system(("python media_w.py saidas_users\\user" + str(user) + "\\percentage.out " + "saidas_users\\user" + str(user) + "\\media_user"+str(user)).replace("\\",separator))
		os.system(("python media_w.py saidas_users\\user" + str(user) + "\\percentage.out " + "saidas_users\\media_users").replace("\\",separator))

