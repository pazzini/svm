#!/usr/bin/env python
# -*- coding: utf-8 -*-

import methods

class Tweet:
	text = None
	original_text = None
	status_created_at = None
	status_created_at_month = None
	status_created_at_day = None
	status_created_at_hour = None
	status_created_at_minute = None
	source = None
	in_reply_to_twitter_status_id = None
	in_reply_to_twitter_user_id = None
	in_reply_to_twitter_user_screen_name = None
	retweeted_twitter_status_id = None
	retweet_count = None
	retweet_count_class = None
	retweeted = None
	geo = None
	contributors = None
	name = None
	screen_name = None
	location = None
	description = None
	original_description = None
	url = None
	protected = None
	followers_count = None
	followers_count_classe = None
	friends_count = None
	friends_count_class = None
	favourites_count = None
	favourites_count_class = None
	user_created_at = None
	utc_offset = None
	time_zone = None
	geo_enabled = None
	statuses_count = None
	lang = None
	contributors_enabled = None
	listed_count = None
	is_translator = None
	favorited = None
	entity_user_mention = None
	entity_hashtag = None
	entity_url = None
	manual_classification = None
	probability = {"important":0.,"neutral":0.,"not-important":0.}
	
	def __init__(self, text = None, status_created_at = None, source = None, in_reply_to_twitter_status_id = None, in_reply_to_twitter_user_id = None, in_reply_to_twitter_user_screen_name = None, retweeted_twitter_status_id = None, retweet_count = None, retweeted = None, geo = None, contributors = None, name = None, screen_name = None, location = None, description = None, url = None, protected = None, followers_count = None, friends_count = None, favourites_count = None, user_created_at = None, utc_offset = None, time_zone = None, geo_enabled = None, statuses_count = None, lang = None, contributors_enabled = None, listed_count = None, is_translator = None, favorited = None, entity_user_mention = None, entity_hashtag = None, entity_url = None, manual_classification = None):
		self.text = text
		self.status_created_at = status_created_at
		self.source = source
		self.in_reply_to_twitter_status_id = in_reply_to_twitter_status_id
		self.in_reply_to_twitter_user_id = in_reply_to_twitter_user_id
		self.in_reply_to_twitter_user_screen_name = in_reply_to_twitter_user_screen_name
		self.retweeted_twitter_status_id = retweeted_twitter_status_id
		self.retweet_count = retweet_count
		self.retweeted = retweeted
		self.geo = geo
		self.contributors = contributors
		self.name = name
		self.screen_name = screen_name
		self.location = location
		self.description = description
		self.url = url
		self.protected = protected
		self.followers_count = followers_count
		self.friends_count = friends_count
		self.favourites_count = favourites_count
		self.user_created_at = user_created_at
		self.utc_offset = utc_offset
		self.time_zone = time_zone
		self.geo_enabled = geo_enabled
		self.statuses_count = statuses_count
		self.lang = lang
		self.contributors_enabled = contributors_enabled
		self.listed_count = listed_count
		self.is_translator = is_translator
		self.favorited = favorited
		self.entity_user_mention = entity_user_mention
		self.entity_hashtag = entity_hashtag
		self.entity_url = entity_url
		self.manual_classification = manual_classification
		self.original_text = self.text
		self.original_description = self.description.split()
		#if self.status_created_at != None:
		#	self.set_status_created_at()
		if self.text != None:
			self.text = self.split_text(self.text,3)
		if self.description != None:
			self.description = self.split_text(self.description,3)
		if self.entity_hashtag != None:
			self.set_entity_hashtag()
		if self.entity_user_mention != None:
			self.set_entity_user_mention()
	
	def split_text(self,text,min_tam_word):
		stop_words = methods.load_stop_words()
		filtered_text = text
		if filtered_text != None:
			temp = filtered_text.split()
			if min_tam_word > 0:
				filtered_text = []
				for word in temp:
					processed_word = methods.process_text(word,min_tam_word)
					if processed_word != "" and (processed_word not in stop_words):
						processed_word = methods.strip_accents(processed_word.decode("utf-8"))
						filtered_text.append(processed_word)
			else:
				filtered_text = temp
		return filtered_text
	
	def set_text(self,text):
		self.text = text

	def set_status_created_at(self):
		date = methods.split_date(self.status_created_at)
		self.status_created_at_month = date[0]
		self.status_created_at_day = date[1]
		self.status_created_at_hour = date[2]
		self.status_created_at_minute = date[3]
		
	def set_source(self,source):
		self.source = source
		
	def set_in_reply_to_twitter_status_id(self,in_reply_to_twitter_status_id):
		self.in_reply_to_twitter_status_id = in_reply_to_twitter_status_id
		
	def set_in_reply_to_twitter_user_id(self,in_reply_to_twitter_user_id):
		self.in_reply_to_twitter_user_id = in_reply_to_twitter_user_id
		
	def set_in_reply_to_twitter_screen_name(self,in_reply_to_twitter_user_screen_name):
		self.in_reply_to_twitter_user_screen_name = in_reply_to_twitter_user_screen_name
		
	def set_retweeted_twitter_status_id(self,retweeted_twitter_status_id):
		self.retweeted_twitter_status_id = retweeted_twitter_status_id
	
	def set_retweet_count(self,retweet_count):
		self.retweet_count = retweet_count
	
	def set_retweeted(self,retweeted):
		self.retweeted = retweeted
		
	def set_geo(self,geo):
		self.geo = geo
		
	def set_contributors(self,contributors):
		self.contributors = contributors
		
	def set_name(self,name):
		self.name = name
		
	def set_screen_name(self,screen_name):
		self.screen_name = screen_name
		
	def set_location(self,location):
		self.location = location
		
	def set_description(self,description):
		self.description = description
		
	def set_url(self,url):
		self.url = url
		
	def set_protected(self,protected):
		self.protected = protected
		
	def set_followers_count(self,followers_count):
		self.followers_count = followers_count
		
	def set_friends_count(self,friends_count):
		self.friends_count = friends_count
		
	def set_favourites_count(self,favourites_count):
		self.favourites_count = favourites_count
		
	def set_user_created_at(self,user_created_at):
		self.user_created_at = user_created_at
		
	def set_utc_offset(self,utc_offset):
		self.utc_offset = utc_offset
		
	def set_time_zone(self,time_zone):
		self.time_zone = time_zone
		
	def set_geo_enabled(self,geo_enabled):
		self.geo_enabled = geo_enabled
		
	def set_statuses_count(self,statuses_count):
		self.statuses_count = statuses_count
		
	def set_lang(self,lang):
		self.lang = lang
		
	def set_contributors_enabled(self,contributors_enabled):
		self.contributors_enabled = contributors_enabled
		
	def set_listed_count(self,listed_count):
		self.listed_count = listed_count
		
	def set_is_translator(self,is_translator):
		self.is_translator = is_translator
		
	def set_favorited(self,favorited):
		self.favorited = favorited
		
	def set_entity_user_mention(self):
		self.entity_user_mention = self.entity_user_mention.split(",")
		
	def set_entity_hashtag(self):
		self.entity_hashtag = self.entity_hashtag.split(",")
		
	def set_entity_url(self,entity_url):
		self.entity_url = entity_url
		
	def set_manual_classification(self,manual_classification):
		self.manual_classification = manual_classification
	
	def set_probability(self, probability):
		self.probability = probability
	
	def get_text(self):
		return self.text
	
	def get_original_text(self):
		return self.original_text
	
	def get_original_description(self):
		return self.original_description
	
	def get_status_created_at(self):
		return self.status_created_at
	
	def get_date(self):
		return self.date
	
	def get_source(self):
		return self.source
		
	def get_in_reply_to_twitter_status_id(self):
		return self.in_reply_to_twitter_status_id
		
	def get_in_reply_to_twitter_user_id(self):
		return self.in_reply_to_twitter_user_id
		
	def get_in_reply_to_twitter_screen_name(self):
		return self.in_reply_to_twitter_user_screen_name
		
	def get_retweeted_twitter_status_id(self):
		return self.retweeted_twitter_status_id
	
	def get_retweet_count(self,retweet_count = None):
		rc = retweet_count
		if retweet_count == None:
			rc = self.retweet_count
		return self.histogram_classification(rc, 0, 10, 12)
	
	def get_retweeted(self):
		return self.retweeted
		
	def get_geo(self):
		return self.geo
		
	def get_contributors(self):
		return self.contributors
		
	def get_name(self):
		return self.name
		
	def get_screen_name(self):
		return self.screen_name
		
	def get_location(self):
		return self.location
		
	def get_description(self):
		return self.description
		
	def get_url(self):
		return self.url
		
	def get_protected(self):
		return self.protected
		
	def get_followers_count(self,followers_count = None):
		fc = followers_count
		if followers_count == None:
			fc = self.followers_count
		return self.histogram_classification(fc, 0, 60000, 12)
		
	def get_friends_count(self,friends_count = None):
		fc = friends_count
		if friends_count == None:
			fc = self.friends_count
		return self.histogram_classification(fc, 0, 1250, 15)
		
	def get_favourites_count(self,favourites_count = None):
		fc = favourites_count
		if favourites_count == None:
			fc = self.favourites_count
		return self.histogram_classification(fc,0,1250,15)
		#return self.favourites_count
		
	def get_user_created_at(self):
		return self.user_created_at
		
	def get_utc_offset(self):
		return self.utc_offset
		
	def get_time_zone(self):
		return self.time_zone
		
	def get_geo_enabled(self):
		return self.geo_enabled
		
	def get_statuses_count(self,statuses_count = None):
		sc = statuses_count
		if statuses_count == None:
			sc = self.statuses_count
		return self.histogram_classification(sc, 0, 25000, 16)
		
	def get_lang(self):
		return self.lang
		
	def get_contributors_enabled(self):
		return self.contributors_enabled
		
	def get_listed_count(self,listed_count = None):
		lc = listed_count
		if listed_count == None:
			lc = self.listed_count
		return self.histogram_classification(lc, 0, 2500, 12)
		
	def get_is_translator(self):
		return self.is_translator
		
	def get_favorited(self):
		return self.favorited
		
	def get_entity_user_mention(self):
		return self.entity_user_mention
		
	def get_entity_hashtag(self):
		return self.entity_hashtag
		
	def get_entity_url(self):
		return self.entity_url
		
	def get_manual_classification(self):
		return self.manual_classification
		
	def set_probability(self, probability):
		self.probability = probability

	def get_probability(self):
		return self.probability
	
	def get_most_probably_target(self):
		p = "neutral"
		if self.probability["important"] > self.probability[p]:
			p = "important"
		if self.probability["not-important"] > self.probability[p]:
			p = "not-important"
		return p
	
	def histogram_classification(self, number, minimal, maximal, rangenum):
		division = {}
		interval = float(maximal+minimal) / float(rangenum)
		for iterator in range(rangenum+1):
			division[iterator] = minimal+iterator*interval
		for iterator in range(rangenum):
			if(iterator < (rangenum-1)):
				if (float(number) >= division[iterator]) and (float(number) < division[iterator+1]):
						result = iterator
						break
			else:
				result = iterator
		return result
	
	def equals(self,feature,value):
		if feature == "source":
			if self.get_source() == value:
				return True
			else:
				return False
		elif feature == "status_created_at_month":
			if self.status_created_at_month == value:
				return True
			else:
				return False
		elif feature == "status_created_at_day":
			if self.status_created_at_day == value:
				return True
			else:
				return False
		elif feature == "status_created_at_hour":
			if self.status_created_at_hour == value:
				return True
			else:
				return False
		elif feature == "status_created_at_minute":
			if self.status_created_at_minute == value:
				return True
			else:
				return False
		elif feature == "in_reply_to_twitter_status_id":
			if self.get_in_reply_to_twitter_status_id() == value:
				return True
			else:
				return False
		elif feature == "in_reply_to_twitter_user_id":
			if self.get_in_reply_to_twitter_user_id() == value:
				return True
			else:
				return False
		elif feature == "in_reply_to_twitter_user_screen_name":
			if self.get_in_reply_to_twitter_user_screen_name() == value:
				return True
			else:
				return False
		elif feature == "retweeted_twitter_status_id":
			if self.get_retweeted_twitter_status_id() == value:
				return True
			else:
				return False
		elif feature == "retweeted":
			if self.get_retweeted() == value:
				return True
			else:
				return False
		elif feature == "geo":
			if self.get_geo() == value:
				return True
			else:
				return False
		elif feature == "contributors":
			if self.get_contributors() == value:
				return True
			else:
				return False
		elif feature == "name":
			if self.get_name() == value:
				return True
			else:
				return False
		elif feature == "screen_name":
			if self.get_screen_name() == value:
				return True
			else:
				return False
		elif feature == "location":
			if self.get_location() == value:
				return True
			else:
				return False
		elif feature == "description":
			if self.get_description() == value:
				return True
			else:
				return False
		elif feature == "url":
			if self.get_url() == value:
				return True
			else:
				return False
		elif feature == "protected":
			if self.get_protected() == value:
				return True
			else:
				return False
		elif feature == "user_created_at":
			if self.get_user_created_at() == value:
				return True
			else:
				return False
		elif feature == "utc_offset":
			if self.get_utc_offset() == value:
				return True
			else:
				return False
		elif feature == "time_zone":
			if self.get_time_zone() == value:
				return True
			else:
				return False
		elif feature == "geo_enabled":
			if self.get_geo_enabled() == value:
				return True
			else:
				return False
		elif feature == "statuses_count":
			if self.get_statuses_count() == value:
				return True
			else:
				return False
		elif feature == "lang":
			if self.get_lang() == value:
				return True
			else:
				return False
		elif feature == "contributors_enabled":
			if self.get_contributors_enabled() == value:
				return True
			else:
				return False
		elif feature == "listed_count":
			if self.get_listed_count() == value:
				return True
			else:
				return False
		elif feature == "is_translator":
			if self.get_is_translator() == value:
				return True
			else:
				return False
		elif feature == "favorited":
			if self.get_favorited() == value:
				return True
			else:
				return False
		elif feature == "retweet_count":
			if self.get_retweet_count(value) == self.get_retweet_count():
				return True
			else:
				return False
		elif feature == "followers_count":
			if self.get_followers_count(value) == self.get_followers_count():
				return True
			else:
				return False
		elif feature == "friends_count":
			if self.get_friends_count(value) == self.get_friends_count():
				return True
			else:
				return False
		elif feature == "favourites_count":
			if self.get_favourites_count(value) == self.get_favourites_count():
				return True
			else:
				return False
		elif feature == "statuses_count":
			if self.get_statuses_count(value) == self.get_statuses_count():
				return True
			else:
				return False
		elif feature == "listed_count":
			if self.get_listed_count(value) == self.get_listed_count():
				return True
			else:
				return False
		else:
			print "WRONG FEATURE - method equals"
	
	def get(self,feature):
		if feature == "text":
			return self.get_text()
		elif feature == "original_text":
			return self.original_text
		elif feature ==	"status_created_at":
			return self.get_status_created_at()
		elif feature ==	"status_created_at_month":
			return self.status_created_at_month
		elif feature ==	"status_created_at_day":
			return self.status_created_at_day
		elif feature ==	"status_created_at_hour":
			return self.status_created_at_hour
		elif feature ==	"status_created_at_minute":
			return self.status_created_at_minute
		elif feature == "source":
			return self.get_source()
		elif feature == "in_reply_to_twitter_status_id":
			return self.get_in_reply_to_twitter_status_id()
		elif feature == "in_reply_to_twitter_user_id":
			return self.get_in_reply_to_twitter_status_id()
		elif feature == "in_reply_to_twitter_user_screen_name":
			return self.get_in_reply_to_twitter_screen_name()
		elif feature == "retweeted_twitter_status_id":
			return self.get_retweeted_twitter_status_id()
		elif feature == "retweet_count":
			return self.get_retweet_count()
		elif feature == "retweeted":
			return self.get_retweeted()
		elif feature == "geo":
			return self.get_geo()
		elif feature == "contributors":
			return self.get_contributors()
		elif feature == "name":
			return self.get_name()
		elif feature == "screen_name":
			return self.get_screen_name()
		elif feature == "location":
			return self.get_location()
		elif feature == "description":
			return self.get_description()
		elif feature == "original_description":
			return self.original_description
		elif feature == "url":
			return self.get_url()
		elif feature == "protected":
			return self.get_protected()
		elif feature == "followers_count":
			return self.get_followers_count()
		elif feature == "friends_count":
			return self.get_friends_count()
		elif feature == "favourites_count":
			return self.get_favourites_count()
		elif feature == "user_created_at":
			return self.get_user_created_at()
		elif feature == "utc_offset":
			return self.get_utc_offset()
		elif feature == "time_zone":
			return self.get_time_zone()
		elif feature == "geo_enabled":
			return self.get_geo_enabled()
		elif feature == "statuses_count":
			return self.get_statuses_count()
		elif feature == "lang":
			return self.get_lang()
		elif feature == "contributors_enabled":
			return self.get_contributors_enabled()
		elif feature == "listed_count":
			return self.get_listed_count()
		elif feature == "is_translator":
			return self.get_is_translator()
		elif feature == "favorited":
			return self.get_favorited()
		elif feature == "entity_user_mention":
			return self.get_entity_user_mention()
		elif feature == "entity_hashtag":
			return self.get_entity_hashtag()
		elif feature == "entity_url":
			return self.get_entity_url()
		elif feature == "manual_classification":
			return self.get_manual_classification()
		else:
			print "WRONG FEATURE - method get"

"""
class Date:
	month = None
	day = None
	hour = None
	minute = None
	
	def __init__(self, day = None, hour = None, month = None, minute = None):
		self.day = day
		self.hour = hour
		self.month = month
		self.minute = minute
	
	def set_month(self,month):
		self.month = month
	
	def set_day(self,day):
		self.day = day
	
	def set_hour(self,hour):
		self.hour = hour
		
	def set_minute(self,minute):
		self.minute = minute
	
	def get_month(self):
		return month
	
	def get_day(self):
		return day
	
	def get_hour(self):
		return hour
		
	def get_minute(self):
		return minute
"""
