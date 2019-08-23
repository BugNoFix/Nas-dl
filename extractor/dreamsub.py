#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (c) 2018 games195, BugNoFix. Under MIT License.

import requests, os, re, json, cfscrape, threading, time, urllib.parse
from utilies import RemoveSpecialCharacter
from threading import Thread

# Load configs
CONFIG = json.load(open('setting.json'))

Dreamsub_VALID = r'https?:\/\/www.dreamsub\.(co|online|stream)\/.*'
base_url = 'https://www.dreamsub.stream/search/'

def Dreamsub(URL):
	sess = cfscrape.create_scraper(requests.session())
	page = (sess.get(URL).text)
	name = re.search(r'<h1>(.*) Streaming.*<\/h1>', page, re.IGNORECASE).group(1)
	ep = re.search(r'<b>Episodi<\/b>: ([0-9]*)(?:\+)?<br>', page, re.IGNORECASE).group(1)
	for n in range(0, int(ep) + 1):
		print("boh")
		sess = cfscrape.create_scraper(requests.session())
		page = sess.get('{}/{}/'.format(URL, n)).text
		keepem = re.search(r'https?:\/\/keepem.online\/(?:f|embed)\/...........', page, re.IGNORECASE)
		if keepem:
			os.system('exe\\youtube-dl {0} -o "{1}/{2}/{3}"'.format(keepem.group(), CONFIG['Path'], RemoveSpecialCharacter(name), '%(title)s.%(ext)s'))

def DreamsubSearcher(anime):
	url_anime = []
	nome = []
	#encode url
	encode = urllib.parse.quote_plus(anime)
	url = base_url + encode
	#request
	sess = cfscrape.create_scraper(requests.session())
	page = (sess.get(url).text)
	dati = re.findall(r'<a href="(.*)" title="Lista episodi (.*) Streaming"><img src="\/res\/img\/menu\.png"', str(page), re.IGNORECASE)
	for metadati in dati:
		url_anime.append(metadati[0])
		nome.append(metadati[1])
	return nome, url_anime
