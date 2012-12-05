#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time
from threading import Thread

separator = "/"

if "win" in sys.platform:
	separator = "\\"

#conj = [[19]]
conj = [[0,2,7,8,12,13,14,17,18,22,25,27,29,30,31]]

#users = [1,2,3,4,5,6,7,8,9]
#users = [2]
users = range(1,10)
#users = range(143,185)

count = 0
for i in users:
	for c in conj:
		s = ""
		threads = []
		for n in range(len(c)):
			if n < (len(c) - 1):
				s += (str(c[n]) + ",")
			else:
				s += (str(c[n]))
		s = ("python svm_codes.py users\\user" + str(i) + ".xml -f " + s + " -d -v 10 -find -fm").replace("\\",separator)
		time_ini = time.time()
		os.system(s,)
		count += 1
		print str("%.2f"%((count / ((float(len(conj)))*len(users)))*100)) + "% ",str(count)+"/"+str((float(len(conj)))*len(users)),"time: %.2f"%(time.time()-time_ini),"s"
		print ""


""""text", #0
"status_created_at", #1
"source", #2
"in_reply_to_twitter_status_id", #3
"in_reply_to_twitter_user_id", #4
"in_reply_to_twitter_user_screen_name", #5
"retweeted_twitter_status_id", #6
"retweet_count", #7
"retweeted", #8
"geo", #9
"contributors", #10
"name", #11
"screen_name", #12
"location", #13
"description", #14
"url",15
"protected", #16
"followers_count", #17
"friends_count", #18
"favourites_count", #19
"user_created_at", #20
"utc_offset", #21
"time_zone", #22
"geo_enabled", #23
"statuses_count", #24
"lang", #25
"contributors_enabled", #26
"listed_count", #27
"is_translator", #28
"favorited", #29
"entity_user_mention", #30
"entity_hashtag", #31
"entity_url", #32
"manual_classification" #33"""
