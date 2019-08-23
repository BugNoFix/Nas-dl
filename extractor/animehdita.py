#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (c) 2018 games195. Under MIT License.

import requests, os, re, json
from utilies import OpenloadStreamangoCheck

# Load configs
CONFIG = json.load(open('setting.json'))

AnimeHDITA_VALID = r'http:\/\/www\.animehdita\.org.*'
base_url = 'http://www.animehdita.org/?s='

def AnimeHDITA(URL):
    page = requests.get(URL).text

    openload = re.search(r'src="(https?:\/\/(?:openload|oload)\..*\/(?:f|embed)\/.*)"/ scrolling="no"', str(page), re.IGNORECASE).group(1)
    if openload and OpenloadStreamangoCheck(openload):
        os.system('exe\\youtube-dl {0} -o "{1}/{2}"'.format(openload, CONFIG['Path'], '%(title)s.%(ext)s'))
'''
Sistemare re.findall
def AnimeHDITASearcher(anime):
	url_anime = []
	nome = []
	#encode url
	encode = urllib.parse.quote_plus(anime)
	url = base_url + encode
	#request
	page = requests.get(URL).text
	dati = re.findall(r'<a href="(.*)" title="Lista episodi (.*) Streaming"><img src="\/res\/img\/menu\.png"', str(page), re.IGNORECASE)
	for metadati in dati:
		url_anime.append(metadati[0])
		nome.append(metadati[1])
	return nome, url_anime
'''
