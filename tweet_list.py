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

	tam_important = None
	
	#documents = lista dos tweets da base de treinamento
	#test = lista dos tweets da base de teste
	documents = []
	training_base = []
	test = []
	test_base = []
	
	#lista de tweets importantes, neutros e nao-importantes
	important_list = []
	neutral_list = []
	not_important_list = []
	
	#valores buscados previamente, funciona tipo uma especie de cache
	#ajuda a acelerar o processamento
	previously_searched = {}
	previously_different = {}
	
	#variaveis que contem a quantidade te cada tipo de tweet em cada lista de tweets
	#base de teste, base de treino e todal
	count_target_test = {"important":0.,"neutral":0.,"not-important":0.}
	count_target_learn = {"important":0.,"neutral":0.,"not-important":0.}
	targets_total = {"important":0.,"neutral":0.,"not-important":0.}	
	
	#metodo para limpar todas as variaveis da classe, zera-las
	def clean_classification(self):
		self.training_base = []
		self.test_base = []
		self.important_list = []
		self.neutral_list = []
		self.not_important_list = []
		self.previously_searched = {}
		self.previously_different = {}
		self.count_target_test = {"important":0.,"neutral":0.,"not-important":0.}
		self.count_target_learn = {"important":0.,"neutral":0.,"not-important":0.}
	
	def clean_load(self):
		self.tam_important = None
		self.documents = []
		self.training_base = []
		self.test_base = []
		self.important_list = []
		self.neutral_list = []
		self.not_important_list = []
		self.previously_searched = {}
		self.previously_different = {}
		self.count_target_test = {"important":0.,"neutral":0.,"not-important":0.}
		self.count_target_learn = {"important":0.,"neutral":0.,"not-important":0.}
		self.targets_total = {"important":0.,"neutral":0.,"not-important":0.}	
		
	#metodo para deletar a classe(possivelmente para liberar memoria de classe que nao serao mais usadas)
	def delete(self):
		del self
	
	#metodo que divide os tweets obtidos em uma lista de tweets importantes, neutros, nao-importantes
	#tambem conta a quantidade de tweets importantes, neutros e nao-importantes
	#cria um tweet da classe tweet com seus respectivos atributos e
	#os aloca de acordo com a variavel train_percent, entre base de teste e de treinamento
	#file_path contem o caminho do arquivo .xml com a base de dados do tweet
	#train_percent e a porcentagem da base de treinamento
	#ex: train_percent=70, 70% dos tweets serao alocados na base de treinamento e 30% dos tweets na base de teste
	#nao ha nenhuma garantia de que uma base havera no minimo um de cada tipo de tweet
	def load_tweets_test(self, file_path):
		#self.clean_all()
		self.test_base = []
		self.file_test_path = parse(file_path)
		self.tables_test = self.file_test_path.getElementsByTagName("table")
		for item in self.tables_test:
			colum = item.getElementsByTagName("column")
			if colum.item(33).childNodes[0].nodeValue == "important":
				self.targets_total["important"] += 1
			elif colum.item(33).childNodes[0].nodeValue == "neutral":
				self.targets_total["neutral"] += 1
				#self.targets_total["not-important"] += 1
			else:
				self.targets_total["not-important"] += 1
		
		for item in self.tables_test:
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
			self.test_base.append(temp)
	
	def load_tweets(self, file_path):
		self.clean_load()
		self.file_path = parse(file_path)
		self.tables = self.file_path.getElementsByTagName("table")
		for item in self.tables:
			colum = item.getElementsByTagName("column")
			if colum.item(33).childNodes[0].nodeValue == "important":
				self.targets_total["important"] += 1
			elif colum.item(33).childNodes[0].nodeValue == "neutral":
				self.targets_total["neutral"] += 1
				#self.targets_total["not-important"] += 1
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
			self.documents.append(temp)
		self.training_base = list(self.documents)
		if temp.get_manual_classification() == "not-important":
			self.not_important_list.append(temp)
		elif temp.get_manual_classification() == "important":
			self.important_list.append(temp)
		elif temp.get_manual_classification() == "neutral":
			self.neutral_list.append(temp)
	
	def classification_division(self,train_percent):
		self.clean_classification()
		temp_train = []
		temp_test = []
		for tweet in self.documents:
			if random.randint(0,100) <= (100 - train_percent):
				target = tweet.get("manual_classification")
				if self.count_target_test[target] / self.targets_total[target] <= ((100. - train_percent) / 100.):
					temp_test.append(tweet)
					self.count_target_test[target] += 1
				else:
					temp_train.append(tweet)
					if tweet.get("manual_classification") == "important":
						self.important_list.append(tweet)
					elif tweet.get("manual_classification") == "neutral":
						self.neutral_list.append(tweet)
					else:
						self.not_important_list.append(tweet)
					self.count_target_learn[target] += 1
			else:
				target = tweet.get("manual_classification")
				if self.count_target_learn[target] / self.targets_total[target] <= (train_percent / 100.):
					temp_train.append(tweet)
					if tweet.get("manual_classification") == "important":
						self.important_list.append(tweet)
					elif tweet.get("manual_classification") == "neutral":
						self.neutral_list.append(tweet)
					else:
						self.not_important_list.append(tweet)
					self.count_target_learn[target] += 1
				else:
					temp_test.append(tweet)
					self.count_target_test[target] += 1
		self.training_base = list(temp_train)
		self.test_base = list(temp_test)

	#Busca que retorna a quantidade de diferentes valores de um feature
	#Caso somente o feature seja passado como parametro, retorna a quantidade de valores diferentes para aquele feature
	#caso um target tambem seja passado como parametro, retorna a quantidade de valores diferentes para aquele feature de um targed especifico(importante, nao-importante, neutro)
	#Retorna o valor salvo no array de valores ja pesquisado caso um determinado valor ja tenha sido pesquisado previamente
	def different_values(self,feature,target = None):
		set_temp = set([])
		if (target,feature) not in self.previously_different:
			if(target == "not-important"):
				temp_list = self.not_important_list
			elif(target == "important"):
				temp_list = self.important_list
			elif(target == "neutral"):
				temp_list = self.neutral_list
			else:
				temp_list = self.documents
			for tweet in temp_list:
				if isinstance(tweet.get(feature),list):
					for value in tweet.get(feature):
						set_temp.add(value)
				else:
					set_temp.add(tweet.get(feature))
			self.previously_different[(target,feature)] = float(len(set_temp))
			return len(set_temp)
		else:
			return self.previously_different[(target,feature)]
	
	#retorna o metodo search para todos os targers de um feature
	def search_values_all_targets(self,feature):
		temp = self.search("important",feature)
		temp += self.search("neutral",feature)
		temp += self.search("not-important",feature)
		return float(temp)

	def search(self, feature=None, value = None):
		if value == None:
			i = 0.
			if(feature) not in self.previously_searched:
				temp_list = self.training_base
				for tweet_data in temp_list:
					if isinstance(tweet_data.get(feature), list):
						i += len(tweet_data.get(feature))
					else:
						if tweet_data.get(feature) != "NULL":
							i += 1.
				self.previously_searched[feature] = float(i)
				return float(i)
			else:
				return float(self.previously_searched[feature])
		else:
			i = 0.
			otimization = 0.
			if (feature, value) not in self.previously_searched:
				temp_list = self.training_base
				for tweet_data in temp_list:
					if isinstance(tweet_data.get(feature), list):
						for list_data in tweet_data.get(feature):
							otimization += 1.
							if list_data == value:
								i += 1.
					else:
						otimization += 1.
						if(tweet_data.equals(feature,value)):
							i += 1.
				self.previously_searched[(feature, value)] = float(i)
				self.previously_searched[feature] = float(otimization)
				return float(i)
			else:
				return float(self.previously_searched[(feature, value)])
			#return 3 * total #3x é para manter os resultados, se removido necessario gerar novos resultados
	
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

	#retorna quantidade de tweets da base de treinamento
	def get_documents_list_tam(self):
		return len(self.documents)

	#retorna a lista com os tweets da base de treinamento
	def get_documents_list(self):
		return list(self.documents)
		
	#retorna a lista dos atuais tweets na base de treinamento
	def get_training_base(self):
		return list(self.training_base)
		
	def get_training_base_tam(self):
		return len(self.training_base)	
	
	#retorna a lista do atuais tweets na base de teste
	def get_test_base(self):
		return list(self.test_base)	

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
