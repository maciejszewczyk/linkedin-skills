#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import time
import json

URL = "https://www.linkedin.com/ta/skill?query="

first_letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'w', 'v', 'x', 'y', 'z']

def get_skill(query_prefix):
	nl = []
	json_skills = urllib.urlopen(URL + query_prefix).read()
	dictionary_skills = json.loads(json_skills)

	for skill in dictionary_skills["resultList"]:
		z = skill["displayName"]
		nl.append(z)
	return nl

for l in first_letter:
	for i in first_letter:
		for j in first_letter:
			time.sleep(0.1)
			ret = get_skill(l+i+j)
			if ret is not None:
				for key in ret:
					file_object = open('linkedin_skills.txt', 'a')
					file_object.write(key+"\n")
					file_object.close( )
