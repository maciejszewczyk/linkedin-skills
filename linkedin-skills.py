#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import time
import json
from string import ascii_lowercase
from itertools import product

URL = "https://www.linkedin.com/ta/skill?query="

def get_skills(query_suffix):
	json_skills = urllib.urlopen(URL + query_suffix).read()
	dictionary_skills = json.loads(json_skills)
	return [skill['displayName'] for skill in dictionary_skills['resultList']]

with open('linkedin_skills.txt', 'w') as file:
	for triple in product(*(ascii_lowercase,)*3):
		time.sleep(0.1)
		ret = get_skills(''.join(triple))
		file.write('\n'.join(ret) + '\n')
