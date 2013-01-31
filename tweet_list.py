#!/usr/bin/env python
# -*- coding: utf-8 -*-

from xml.dom.minidom import parse
import random
import sys
import time
import tweet

#classe que contem a lista com todos os tweets, tanto da base de treinamento
#como da base de teste
class tweet_list:
	
	#documents = lista dos tweets
	#training_base = lista dos tweets na base de treinamento
	#test_base = lista dos tweets da base de teste
	documents = []
	training_base = []
	test_base = []
	
	#valores buscados previamente, uma cache que
	#ajuda a acelerar o processamento
	#Alterado, valores passados pelo metodo create_dictionary (acelerou)
	previously_searched = {}
	previously_different = {}
	
	#variaveis que contem a quantidade de cada tipo de tweet no total
	targets_total = {"important":0.,"neutral":0.,"not-important":0.}	
	
	def clean_load(self):
		self.documents = []
		self.training_base = []
		self.test_base = []
		self.previously_searched = {}
		self.previously_different = {}
		self.targets_total = {"important":0.,"neutral":0.,"not-important":0.}	
	
	#usado para utilizar diferentes bases, uma para teste
	#e uma para treinamento.
	def load_tweets_test(self,fp):
		self.test_base = []
		self.load(fp)
	
	#carrega na lista documents e na base de treinamento(default)
	#os tweets contigos no .xml passado
	def load_tweets(self,fp):
		self.clean_load()
		self.load(fp)
		self.set_training_base(self.documents)
		
	def load(self, fp):
		temp_list = []
		file_path = parse(fp)
		self.tables = file_path.getElementsByTagName("table")
		for item in self.tables:
			colum = item.getElementsByTagName("column")
			if colum.item(33).childNodes[0].nodeValue == "important":
				self.targets_total["important"] += 1
			elif colum.item(33).childNodes[0].nodeValue == "neutral":
				self.targets_total["neutral"] += 1
			else:
				self.targets_total["not-important"] += 1
		
		for item in self.tables:
			colum = item.getElementsByTagName("column")
			temp = tweet.Tweet(colum.item(0).childNodes[0].nodeValue,
				colum.item(1).childNodes[0].nodeValue,
				colum.item(2).childNodes[0].nodeValue,
				colum.item(3).childNodes[0].nodeValue,
				colum.item(4).childNodes[0].nodeValue,
				colum.item(5).childNodes[0].nodeValue,
				colum.item(6).childNodes[0].nodeValue,
				colum.item(7).childNodes[0].nodeValue,
				colum.item(8).childNodes[0].nodeValue,
				colum.item(9).childNodes[0].nodeValue,
				colum.item(10).childNodes[0].nodeValue,
				colum.item(11).childNodes[0].nodeValue,
				colum.item(12).childNodes[0].nodeValue,
				colum.item(13).childNodes[0].nodeValue,
				colum.item(14).childNodes[0].nodeValue,
				colum.item(15).childNodes[0].nodeValue,
				colum.item(16).childNodes[0].nodeValue,
				colum.item(17).childNodes[0].nodeValue,
				colum.item(18).childNodes[0].nodeValue,
				colum.item(19).childNodes[0].nodeValue,
				colum.item(20).childNodes[0].nodeValue,
				colum.item(21).childNodes[0].nodeValue,
				colum.item(22).childNodes[0].nodeValue,
				colum.item(23).childNodes[0].nodeValue,
				colum.item(24).childNodes[0].nodeValue,
				colum.item(25).childNodes[0].nodeValue,
				colum.item(26).childNodes[0].nodeValue,
				colum.item(27).childNodes[0].nodeValue,
				colum.item(28).childNodes[0].nodeValue,
				colum.item(29).childNodes[0].nodeValue,
				colum.item(30).childNodes[0].nodeValue,
				colum.item(31).childNodes[0].nodeValue,
				colum.item(32).childNodes[0].nodeValue,
				colum.item(33).childNodes[0].nodeValue)
			temp_list.append(temp)
			self.documents.append(temp)
		return temp_list
	
	def classification_division(self,train_percent):
		self.training_base = []
		self.test_base = []
		count_target_test = {"important":0.,"neutral":0.,"not-important":0.}
		count_target_learn = {"important":0.,"neutral":0.,"not-important":0.}
		
		temp_train = []
		temp_test = []
		for tweet in self.documents:
			if random.randint(0,100) <= (100 - train_percent):
				target = tweet.get("manual_classification")
				if count_target_test[target] / self.targets_total[target] <= ((100. - train_percent) / 100.):
					temp_test.append(tweet)
					count_target_test[target] += 1
				else:
					temp_train.append(tweet)
					count_target_learn[target] += 1
			else:
				target = tweet.get("manual_classification")
				if count_target_learn[target] / self.targets_total[target] <= (train_percent / 100.):
					temp_train.append(tweet)
					count_target_learn[target] += 1
				else:
					temp_test.append(tweet)
					count_target_test[target] += 1
		self.set_training_base(temp_train)
		self.set_test_base(temp_test)

	#Busca que retorna a quantidade de diferentes valores de um feature
	#Caso somente o feature seja passado como parametro, retorna a quantidade de valores diferentes para aquele feature
	#caso um target tambem seja passado como parametro, retorna a quantidade de valores diferentes para aquele feature de um targed especifico(importante, nao-importante, neutro)
	#Retorna o valor salvo no array de valores ja pesquisado caso um determinado valor ja tenha sido pesquisado previamente
	def different_values(self,feature,target = None):
		return self.previously_different[feature]
	
	#Retorna a quantidade de vezes que a palavra aparece na base de treinamento
	def search(self, feature=None, value = None):
		if value == None:
			return float(self.previously_searched[feature])
		else:
			return float(self.previously_searched[(feature, value)])
	
	#retorna a quantidade de tweets de um determinado target(importante, neutro, nao-importante			
	def get_target_tam(self,target):
		if target == "important":
			return float(len(self.important_list))
		elif target == "neutral":
			return float(len(self.neutral_list))
		elif target == "not-important":
			return float(len(self.not_important_list))
		else:
			print "WRONG TARGET"
			
	def set_previously_searched(self,p):
		self.previously_searched = p
		
	def get_previously_searched(self):
		return dict(self.previously_searched)
		
	def set_different_searched(self,p):
		self.previously_different = p
		
	def get_different_searched(self):
		return dict(self.previously_different)

	#retorna lista de tweets importantes
	def get_importants(self):
		return list(self.important_list)
	
	#retorna a lista com tweets neutros	
	def get_neutrals(self):
		return list(self.neutral_list)
	
	#retorna a lista com tweets nao_importantes	
	def get_not_important_list(self):
		return list(self.not_important_list)
	
	#retorna tamanho da lista de tweets nao_importantes
	def get_not_important_tam(self):
		#return len(self.not_important_list)
		return int(self.targets_total["not-important"])
	
	#retorna tamanho da lista de tweets importantes	
	def get_important_tam(self):
		#return len(self.important_list)
		return int(self.targets_total["important"])
	
	#retorna tamanho da lista de tweets neutros	
	def get_neutral_tam(self):
		#return len(self.neutral_list)
		return int(self.targets_total["neutral"])

	#retorna quantidade de tweets total
	def get_documents_list_tam(self):
		return len(self.documents)

	#retorna a lista com os tweets total
	def get_documents_list(self):
		return list(self.documents)
		
	#retorna a lista dos atuais tweets na base de treinamento
	def get_training_base(self):
		return list(self.training_base)
	
	#retorna a quantidade de tweets na base de treinamento	
	def get_training_base_tam(self):
		return len(self.training_base)	
	
	#retorna a lista do atuais tweets na base de teste
	def get_test_base(self):
		return list(self.test_base)	

	#retorna a quantidade de tweets na base de teste
	def get_test_base_tam(self):
		return len(self.test_base)	
	
	#Modifica a atual lista de tweets na base de treinamento
	def set_training_base(self,lt):
		self.previously_searched = {}
		self.previously_different = {}
		self.training_base = list(lt)
	
	#Modifica a atual lista de tweets na base de teste
	def set_test_base(self,lt):
		self.test_base = lt
