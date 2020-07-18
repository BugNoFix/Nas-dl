#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (c) 2019 bugnofix. Under MIT License.

import requests, os, re, json, urllib.parse, cfscrape
from utilies import RemoveSpecialCharacter

# Load configs
CONFIG = json.load(open('setting.json'))

AnimeUnity_VALID = r'https:\/\/animeunity\.it\/.*'
base_url = 'https://www.animeunity.it/'

def AnimeUnity(URL):
	# Varibili
	a = 0

	# Cerco i dati
	sess = cfscrape.create_scraper(requests.session())
	page = (sess.get(URL).text)
	name = re.search(r'<h1 class="title">\s(.*)\s<\/h1>', str(page), re.IGNORECASE).group(1)
	eps = re.search(r'episodes="(.*)"', str(page), re.IGNORECASE).group(1)
	ep = re.findall(r'(https:\\\/\\\/www\.animeunityserver[0-9]*\.cloud\\\/DDL\\\/Anime\\\/[a-zA-Z0-9_.-]*\\\/[a-zA-Z0-9_.-]*_Ep_[0-9]*_SUB_ITA\.mp4)', str(eps), re.IGNORECASE)
	
	# Scarico tutti gli episodi
	for link in ep:
		a = a + 1
		if a < 10:
			finalname = name + ' ep 0' +  str(a)
		else:
			finalname = name + ' ep ' + str(a)
		link = link.replace("\\","")
		os.system('exe\\youtube-dl {0} -o "{1}/{2}/{3}"'.format(link, CONFIG['Path'], name, finalname + '.%(ext)s'))

def AnimeUnitySearcher(anime):

	url_anime = []
	nome = []
	headers={"query":anime}
	search_url = 'https://animeunity.it/anime.php?c=archive'

	# Cerco l'anime nel sito
	sess = cfscrape.create_scraper(requests.session())
	page = sess.post(search_url, headers)
	link_anime = re.findall(r'<a href="(.*)">\s*<img class="card-img archive-card-img" src=".*" alt="">\s*<\/a>\s*<\/div>\s*<\/div>\s*<div class="col-md-7 col-sm-7 archive-col" style="padding-left:0px">\s*<div class="card-block">\s*<br>\s*<h6 class="card-title"><b>(.*)<\/b><\/h6>', str(page.text), re.IGNORECASE)
	
	# Separo il nome dell'anime
	for metadati in link_anime:
		url_anime.append(base_url + metadati[0])
		nome.append(metadati[1])
	return nome, url_anime
