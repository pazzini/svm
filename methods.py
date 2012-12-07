#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Stemmer
import unicodedata

stop_words = []
stop_words_path = ""

def process_text(word,tam=3):
	word = strip_accents(word)
	try:
		word = word.decode("utf-8")
		characters = [u".",u":",u";",u"\'",u"\"",u"!",u")",u"(",u"{",u"}",u"[",u"]",u"*",u",",u"<",u">",u"?",u"=",u"+",u"-",u"\\",u"/",u"_",u"¿",u"“",u"`",u"\""]
		#characters = [".",":",";","\'","\"","!",")","(","{","}","[","]","*",",","<",">","?","=","+","-","\\","/"]
		while word[-1] in characters:
			word = word[:-1]
		while word[:1] in characters:
			word = word[1:]
		word = stem_word(word)
		#stop_words = load_stop_words()
		#if word_condition(word,tam) and (word not in stop_words):
		if word_condition(word,tam):
			return unicode(word.lower())
		else:
			return u""
	except:
		return u""

def word_condition(text,tam=3):
	if len(text) > tam and text.find("http:") == -1:
		return True
	else:
		return False
		
def load_stop_words(file_path = "stop_words.txt"):
	global stop_words_path,stop_words
	if stop_words_path != file_path:
		stop_words = []
		f = open(file_path,"r")
		for word in f:
			word_filtered = process_text((word.strip('\n')).decode('utf-8'))
			stop_words.append(word_filtered)
		f.close()
		stop_words_path = file_path
	return stop_words

def stem_word(word):
	stemmer_pt = Stemmer.Stemmer('portuguese')
	stemmer_en = Stemmer.Stemmer('english')
	word_pt = stemmer_pt.stemWord(word)
	word_en = stemmer_en.stemWord(word)
	if len(word_pt) < len(word_en):
		return word_pt.encode('utf-8')
	else:
		return word_en.encode('utf-8')

def split_date(status_created_at):
	date_splited = []
	date_splited.append(status_created_at.split()[1])
	date_splited.append(status_created_at.split()[0])
	hour = (status_created_at.split()[3]).split(":")[0]
	if hour[0] == "0":
		hour = hour[1:]
	minute = (status_created_at.split()[3]).split(":")[1]
	if minute[0] == "0":
		minute = minute[1:]
	date_splited.append(hour)
	date_splited.append(minute)
	return date_splited

def strip_accents(s):
   return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))
