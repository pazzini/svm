#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

separator = "/"
enter = "\r\n"

if "win" in sys.platform:
	separator = "\\"
	enter = "\n"
	
filename = "find_percentage.out"

for i in range(1,185):
	os.system(("python media_w.py saidas_users\\user" + str(i) + "\\" + filename + " saidas_users\\media_users").replace("\\",separator))
	if os.path.exists(("saidas_users\\user" + str(i) + "\\media_user" + str(i)).replace("\\",separator)):
		os.system(("del saidas_users\\user" + str(i) + "\\media_user" + str(i)).replace("\\",separator))
	os.system(("python media_w.py saidas_users\\user" + str(i) + "\\" + filename + " saidas_users\\user" + str(i) + "\\media_user"+str(i)).replace("\\",separator))
