#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (c) 2019 bugnofix. Under MIT License.

import requests, os, re, json, urllib.parse
from utilies import RemoveSpecialCharacter

# Load configs
CONFIG = json.load(open('setting.json'))

Tns_VALID = r'https:\/\/tnsfansub\.com\/.*'
base_url = 'https://tnsfansub.com/?s='

def Tns(URL):
    # Cerco i dati
	a = 0
	page = requests.get(URL).text
	name = re.search(r'<b>Titolo: <\/b>(.*)<br \/>', str(page), re.IGNORECASE).group(1)
	ep = re.findall(r'<a href="(https:\/\/tnsfansub\.com\/downloads\/.*)">', str(page), re.IGNORECASE)
	dire = CONFIG['Path'] + '/' + name + '/'
	os.system('mkdir '+ '"' +dire.replace('/', '\\') + '"')

	# Scarico tutti gli episodi
	for link in ep:
		a = a + 1
		print('Scarico l\'episodio numero: ' + str(a))
		r = requests.get(link, headers={"Referer":"https://tnsfansub.com/"})
		with open(dire + r'Episodio ' + str(a), 'wb') as f:
			f.write(r.content)

def TnsSearcher(anime):
	# Variabili
	url_anime = []
	nome = []
	link_anime = []

	# Encodo url
	encode = urllib.parse.quote_plus(anime)
	url = base_url + encode
	
	# Richieste web
	page = requests.get(url).text
	dati = re.findall(r'<a href="(https:\/\/tnsfansub\.com\/.*\/)" rel="bookmark">(.*)\s[0-9][0-9]*.*<\/a><\/h1>', str(page), re.IGNORECASE)
	for metadati in dati:
		trovato = False
		# Controllo se il nuovo nome c'è gia
		for temp in nome:
			if temp == metadati[1]:
				trovato = True
		if not trovato:
			url_anime.append(metadati[0])
			nome.append(metadati[1])

	# Acquisisco i veri link
	for temp1 in url_anime:
		page = requests.get(temp1).text
		link = re.search(r'<a href="(.*)"><img class=".*"', str(page), re.IGNORECASE).group(1)
		link_anime.append(link)
	return nome, link_anime
