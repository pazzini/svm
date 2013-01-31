#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import math
import tweet_list
import methods
import sys
from svmutil import *
import time
import pdb

class svm:
	
	tweets = None
	dictionary = {}
	features = ["text", "status_created_at","source","in_reply_to_twitter_status_id","in_reply_to_twitter_user_id","in_reply_to_twitter_user_screen_name","retweeted_twitter_status_id",
			"retweet_count","retweeted","geo","contributors","name","screen_name","location","description","url","protected","followers_count","friends_count","favourites_count",
			"user_created_at","utc_offset","time_zone","geo_enabled","statuses_count","lang","contributors_enabled","listed_count","is_translator","favorited","entity_user_mention",
			"entity_hashtag","entity_url","manual_classification"]
	
	def __init__(self,tweets):
		self.tweets = tweets
		
	def create_dictionary(self,feature_to_do):
		self.dictionary = {}
		previously_searched = {}
		different_searched = {}
		
		stop_words = methods.load_stop_words()
		
		tweet_list = self.tweets.get_training_base()
		
		for i in feature_to_do:
			self.dictionary[self.features[i]] = set([])
			for tweet in tweet_list:
				values = tweet.get(self.features[i])
				if isinstance(values,list):
					for value in values:
						if value not in stop_words:
							if (self.features[i],value) not in previously_searched:
								previously_searched[(self.features[i],value)] = 0
							self.dictionary[self.features[i]].add(value)
							previously_searched[(self.features[i],value)] += 1
				else:
					if (self.features[i],values) not in previously_searched:
						previously_searched[(self.features[i],values)] = 0
					previously_searched[(self.features[i],values)] += 1
					self.dictionary[self.features[i]].add(values)
		self.tweets.set_previously_searched(dict(previously_searched))


	"""Cria a base de treinamento"""
	def create_training_base(self,feature_to_do):
		tl = self.tweets.get_training_base()
		label,value = self.create_base_list(tl,feature_to_do)
		return [label,value]

	"""Cria a base de teste"""
	def create_test_base(self,feature_to_do):
		tl = self.tweets.get_test_base()
		label,value = self.create_base_list(tl,feature_to_do)
		return [label,value]

	"""
	Metodo que 'transforma' os valores de um tweet, em números utilizando o
	metodo idf para realizar os calculos.
	O metodo retorna dois vetores, o primeiro contem os rótulos dos tweets
	e na posuição correspondente do segundo vetor esta contido um dicionário,
	esse dicionário corresponde aos atributos do tweet em formato numérico
	"""
	def create_base_list(self,tweet_list,feature_to_do):
		stop_words = methods.load_stop_words()
		label = []
		value = []
		for tweet in tweet_list:
			i = 0
			temp_label = 0
			temp_value = {}
			found = False
			for j in feature_to_do:
				values = tweet.get(self.features[j])
				
				for word in self.dictionary[self.features[j]]:
					if isinstance(values,list):
						p = 0
						if word in values:
							if not found:
								if tweet.get_manual_classification() == "important":
									temp_label = 1
								else:
									temp_label = -1
								found = True
							p = self.idf(self.tweets.get_training_base(),tweet,word,j)
							temp_value[i] = p
					else:
						if word == values:
							if not found:
								if tweet.get_manual_classification() == "important":
									temp_label = 1
								else:
									temp_label = -1
								found = True
							p = self.idf(self.tweets.get_training_base(),tweet,word,j)
							temp_value[i] = p
					i += 1
				
			if temp_label != 0:
				value.append(temp_value)
				label.append(temp_label)
		return label,value

	"""
	Metodo que transforma um atributo em um numero
	"""
	def idf(self,tweet_list,tweet,word,feat):
		x = 1
		values = tweet.get(self.features[feat])
		if isinstance(values,list):
			return values.count(word) * math.log(len(tweet_list) / (float(self.tweets.search(self.features[feat],word) + x)))
		else:
			return math.log(len(tweet_list) / (float(self.tweets.search(self.features[feat],word) + x)))

	"""
	Metodo salva todos os dicionarios criados cada um em um 
	arquivo com o nome do feature correspondente
	"""
	def save_dictionary(self,path="dics/"):
		for dic in dictionary:
			f = open(path + str(dic),"a")
			for word in dictionary[dic]:
				f.write(unicode(word).encode("utf-8") + "\n")
			f.write("\n" + "-" * 50 + "\n")
			f.close()

	def save_previously_searched(self,path = "dics/previously"):
		temp = self.tweets.get_previously_searched()
		f = open(path ,"a")
		for feature in temp:
			f.write(unicode(feature).encode("utf-8") + " : " + str(temp[feature]) + "\n")
		f.write("-" * 50 + "\n")
		f.close()
		
	def load_tweets(self,path):
		self.tweets.load_tweets(path)

	def load_tweets_test(self,path):
		self.tweets.load_tweets_test(path)

	def classification_division(self,p):
		self.tweets.classification_division(p)

