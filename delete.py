#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

#deleta as saidas dos usuarios de forma automatica, os arquivos percentage.out e media_userx dentro
#das respectivas pastas dos usuarios na pasta saidas_users
for i in range(60):
	if os.path.exists("saidas_users\\user" + str(i+1) + "\\model"):
		os.system("del saidas_users\\user" + str(i+1) + "\\model")
	if os.path.exists("saidas_users\\user" + str(i+1) + "\\saida"):
		os.system("del saidas_users\\user" + str(i+1) + "\\saida")
	if os.path.exists("saidas_users\\user" + str(i+1) + "\\percentage.out"):
		os.system("del saidas_users\\user" + str(i+1) + "\\percentage.out")
	if os.path.exists("saidas_users\\user" + str(i+1) + "\\media_user" + str(i+1)):
		os.system("del saidas_users\\user" + str(i+1) + "\\media_user" + str(i+1))
