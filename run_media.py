#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

for i in range(1,185):
	os.system("media_w.py saidas_users\\user" + str(i) + "\\percentage.out " + "saidas_users\\media_users")
	if os.path.exists("saidas_users\\user" + str(i) + "\\media_user" + str(i)):
		os.system("del saidas_users\\user" + str(i) + "\\media_user" + str(i))
	os.system("media_w.py saidas_users\\user" + str(i) + "\\percentage.out " + "saidas_users\\user" + str(i) + "\\media_user"+str(i))
