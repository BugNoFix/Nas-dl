#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (c) 2019 bugnofix. Under MIT License.

import requests, os, re, json, urllib.parse
from utilies import RemoveSpecialCharacter

# Load configs
CONFIG = json.load(open('setting.json'))

AnimeUnity_VALID = r'https:\/\/animeunity\.it\/.*'
base_url = 'https://animeunity.it/'

def AnimeUnity(URL):
	# Varibili
	a = 0

	# Cerco i dati
	page = requests.get(URL).text
	name = re.search(r'<p>\s*<b>TITOLO: <\/b>(.*)											<\/p>', str(page), re.IGNORECASE).group(1)
	ep = re.findall(r'<div class="ep-box col-lg-1 col-sm-1" style="width:19%">\s*<a href="(anime\.php\?id=.*)" ', str(page), re.IGNORECASE)
	
	# Scarico tutti gli episodi
	for link in ep:
		a = a + 1
		url = 'https://animeunity.it/'+ link
		page = requests.get(url).text
		video = re.search(r'<source src="(.*)" type="video\/.*">\s*<\/video>', str(page), re.IGNORECASE).group(1)
		os.system('exe\\youtube-dl {0} -o "{1}/{2}/{3}"'.format(video, CONFIG['Path'],name ,name + ' ep ' + str(a) + '.%(ext)s'))

def AnimeUnitySearcher(anime):

	url_anime = []
	nome = []
	headers={"query":anime}
	search_url = 'https://animeunity.it/anime.php?c=archive'

	# Cerco l'anime nel sito
	page = requests.post(search_url, headers)
	link_anime = re.findall(r'<a href="(.*)">\s*<img class="card-img archive-card-img" src=".*" alt="">\s*<\/a>\s*<\/div>\s*<\/div>\s*<div class="col-md-7 col-sm-7 archive-col" style="padding-left:0px">\s*<div class="card-block">\s*<br>\s*<h6 class="card-title"><b>(.*)<\/b><\/h6>', str(page.text), re.IGNORECASE)
	
	# Separo il nome dell'anime
	for metadati in link_anime:
		url_anime.append(base_url + metadati[0])
		nome.append(metadati[1])
	return nome, url_anime
