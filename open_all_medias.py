#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

for i in range(9):
	if os.path.exists("saidas_users\\user" + str(i+1) + "\\media_user" + str(i+1)):
		os.system("\"C:\\Program Files (x86)\\Geany\\bin\\Geany.exe\" saidas_users\\user" + str(i+1) + "\\media_user" + str(i+1))
