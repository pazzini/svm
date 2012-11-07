# -*- coding: utf-8 -*-

import tweet_list

list_tweet = tweet_list.tweet_list()
f_out = open("propotion.txt","w")

#conta a quantidade de tweets tem na base do usuário, dividios entre importantes e não importantes
#o numero dentro do for i in range(x) define a quantidade de usuarios para o qual ira fazer
#coloca a saida em um arquivo chamado "propotion.txt"
for i in range(9):
	list_tweet.load_tweets("users/user" + str(i+1) + ".xml")
	temp = list_tweet.get_documents_list()
	#temp.extend(list_tweet.get_test_list())
	important = 0.
	not_important = 0.
	for tweet in temp:
		if tweet.get_manual_classification() == "important":
			important += 1.
		else:
			not_important += 1.
	f_out.write("user" + str(i+1) + " = ")
	f_out.write("important: " + str(important) + "(" + str("%.2f"%((important*100.)/(important + not_important))) + "%)" + " | ")
	f_out.write("not important: " + str(not_important) + "(" + str("%.2f"%((not_important*100.)/(important + not_important))) + "%)" + "\n")

f_out.close()
