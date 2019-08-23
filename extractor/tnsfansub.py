#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (c) 2018 bugnofix. Under MIT License.

import requests, os, re, json, urllib.parse
#from utilies import RemoveSpecialCharacter

# Load configs
CONFIG = json.load(open('setting.json'))

Tns_VALID = r'https:\/\/tnsfansub\.com\/.*'
base_url = 'https://tnsfansub.com/?s='

def Tns(URL):
	a = 0
	page = requests.get(URL).text
	name = re.search(r'<b>Titolo: <\/b>(.*)<br \/>', str(page), re.IGNORECASE).group(1)
	ep = re.findall(r'<a href="(https:\/\/tnsfansub\.com\/downloads\/.*)">', str(page), re.IGNORECASE)
	dire = CONFIG['Path'] + '/' + name + '/'
	print('mkdir '+ dire)
	os.system('mkdir '+ '"' +dire.replace('/', '\\') + '"')
	for link in ep:
		print('scaricando..')
		a = a + 1
		r = requests.get(link, headers={"Referer":"https://tnsfansub.com/"})
		with open(dire + r'Episodio ' + str(a), 'wb') as f:
			f.write(r.content)

#def TnsSearcher(anime):
