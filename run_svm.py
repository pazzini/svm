#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time
from threading import Thread

conj = []
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

separator = "/"

if "win" in sys.platform:
	separator = "\\"

#text description source screen_name location time_zone 
#conj = [[0],[2],[7],[8],[12],[13],[14],[17],[18],[22],[24],[25],[27],[29],[30],[31],[0,14,2,12,13,22]]
#conj = [[0],[2],[7],[8],[12],[13],[14],[17],[18],[22],[24],[25],[27],[29],[30],[31]]
#conj = [[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33]]
#conj = [[0,14,7]]
conj = [[0,2,7,8,12,13,14,17,18,22,25,27,29,30,31]]
#conj = [[0]]

#textual = [[0]]
#textual + mencoes = [[0,1,7,8]]
#geografico = [[0,2,4,5,6,14]]
#social = [[0,3,9,11,12,13]]

#users = [1,2,3,4,5,6,7,8,9]
users = [2]


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
		#s = ("python svm_codes.py users\\user" + str(i) + ".xml -f " + s + " -d -w1 99.99 -w-1 0.01 -t 100 -t2 1 -r 0.02").replace("\\",separator)
		#s = ("python svm_codes.py users\\user" + str(i) + ".xml -f " + s + " -d -w1 98.89 -w-1 1.11 -r 0.02 -t2 30 -v max").replace("\\",separator)
		#s = ("python svm_codes.py users\\user" + str(i) + ".xml -d -ft users\\user2.xml -f " + s + " -w1 98.9 -w-1 1.1 -r 0.1 -t 10").replace("\\",separator)
		s = ("python svm_codes.py users\\user" + str(i) + ".xml -f " + s + " -d -w1 98.2 -w-1 1.8 -r 0.1 -t 1 -v max -fm").replace("\\",separator)
		time_ini = time.time()
		os.system(s,)
		count += 1
		print str("%.2f"%((count / ((float(len(conj)))*len(users)))*100)) + "% ",str(count)+"/"+str((float(len(conj)))*len(users)),"time: %.2f"%(time.time()-time_ini),"s"
		print ""
#for i in users:
#	os.system("media_w.py saidas_users\\user" + str(i) + "\\percentage.out " + "saidas_users\\user" + str(i) + "\\media_user"+str(i))
