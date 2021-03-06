#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (c) 2018 games195, BugNoFix. Under MIT License.

#non funziona https://www.dreamsub.stream/anime/kenja-no-mago
import requests, os, re, json, cfscrape, threading, time, urllib.parse
from utilies import RemoveSpecialCharacter
from threading import Thread

# Load configs
CONFIG = json.load(open('setting.json'))

# Variabili
Dreamsub_VALID = r'https?:\/\/www.dreamsub\.(co|online|stream)\/.*'
basesearch_url = 'https://www.dreamsub.stream/search/'
base_url = 'https://www.dreamsub.stream/'
non_ok = '\033[1;37;40m[\033[1;31;40mX\033[1;37;40m] '
ok = '\033[1;37;40m[\033[1;32;40mok\033[1;37;40m] '
color_reset = '\033[0;38;40m'

def Dreamsub(URL):
	# Cerco i dati
	sess = cfscrape.create_scraper(requests.session())
	page = (sess.get(URL).text)
	name = re.search(r'<h1>(.*) Streaming.*<\/h1>', page, re.IGNORECASE).group(1)
	ep = re.search(r'<b>Episodi<\/b>: ([0-9]*)(?:\+)?<br>', page, re.IGNORECASE).group(1)

	# Scarico tutti gli episodi
	for n in range(1, int(ep) + 1):
		sess = cfscrape.create_scraper(requests.session())
		page = sess.get('{}/{}/'.format(URL, n))
		link = re.search(r'<b>LINK STREAMING<\/b>: <a rel="nofollow" target="_blank" href="(https:\/\/cdn5?\.dreamsub\.(stream|org)\/.*)" title="Guarda l\'episodio in streaming su Server">Server\s*1?<\/a>', page.text, re.IGNORECASE).group(1)
		title = name + ' ' + str(n)
		os.system('exe\\youtube-dl {0} -o "{1}/{2}/{3}"'.format(link, CONFIG['Path'], RemoveSpecialCharacter(name), title + '.%(ext)s'))
		print(ok + "Episodio scaricato " + str(n) + color_reset)


def DreamsubSearcher(anime):
	url_anime = []
	nome = []
	#encode url
	encode = urllib.parse.quote_plus(anime)
	url = basesearch_url + encode
	#request
	sess = cfscrape.create_scraper(requests.session())
	page = (sess.get(url).text)
	dati = re.findall(r'<a href="/(.*)" title="Lista episodi (.*) Streaming"><img src="\/res\/img\/menu\.png"', str(page), re.IGNORECASE)
	for metadati in dati:
		url_anime.append(base_url + metadati[0])
		nome.append(metadati[1])
	return nome, url_anime
