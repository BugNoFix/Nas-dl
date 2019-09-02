#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (c) 2018 games195, BugNoFix. Under MIT License.

from extractor import *
import re, argparse, os, json

# Load configs
CONFIG = json.load(open('setting.json'))

def NASDL(URL):
	# AnimeSenzaLimiti.net
	if re.compile(AnimeSenzaLimiti_VALID).match(URL):
		AnimeSenzaLimiti(URL)
	# AnimePerTutti
	if re.compile(AnimePerTutti_VALID).match(URL):
		AnimePerTutti(URL)
	# Crunchyroll
	elif re.compile(r'https?:\/\/www.crunchyroll.com\/.*').match(URL):
		crunchyroll(URL)
	# VVVVID
	elif re.compile(VVVVID_VALID).match(URL):
		vvvvid(URL)
	# Dreamsub
	elif re.compile(Dreamsub_VALID).match(URL):
		Dreamsub(URL)
	# YouTube
	elif re.compile(YouTube_VALID).match(URL):
		YouTube(URL)
	# CB01
	elif re.compile(CB01_VALID).match(URL):
		CB01(URL)
	# AnimeForce
	elif re.compile(AnimeForce_VALID).match(URL):
		AnimeForce(URL)
	# AnimeHDITA
	elif re.compile(AnimeHDITA_VALID).match(URL):
		AnimeHDITA(URL)
	# HentaiHaven
	elif re.compile(HentaiHaven_VALID).match(URL):
		HentaiHaven(URL)
	# FairyTailItalia
	elif re.compile(FairyTailItalia_VALID).match(URL):
		FairyTailItalia(URL)
	# Tns
	elif re.compile(Tns_VALID).match(URL):
		Tns(URL)
	# AnimeUnity
	elif re.compile(AnimeUnity_VALID).match(URL):
		AnimeUnity(URL)
	# Openlaod
	elif re.compile(r'https?:\/\/(?:openload|oload)\..*\/(?:f|embed)\/.*').match(URL):
		os.system('youtube-dl {0} -o "{1}/{2}"'.format(URL, CONFIG['Path'], '%(title)s.%(ext)s'))
	# Streamango
	elif re.compile(r'https?:\/\/streamango\..*\/(?:f|embed)\/.*').match(URL):
		os.system('youtube-dl {0} -o "{1}/{2}"'.format(URL, CONFIG['Path'], '%(title)s.%(ext)s'))
	else:
		print('[NAS-DL] URL non valido! [ {} ]'.format(URL))
		pass

def searcher(Anime):
	# Variabili
	url_anime = []
	nome = []
	Nsito = False
	a = 1

	# Dreamsub
	temp1, temp2 = DreamsubSearcher(Anime)
	# Verifico che temp1 abbia risultati
	if len(temp1) != 0:
		nome.append(temp1)
		url_anime.append(temp2)
		# La grammatica è importante
		if len(temp1) == 1:
			risultato = ' risultato'
		else:
			risultato = ' risultati'
		print('['+ str(len(nome)) + '] ' + 'Dreamsub ha '+ str(len(temp1)) + risultato)
	
	# Tns
	temp1, temp2 = TnsSearcher(Anime)
	#verifico che temp1 abbia risultati
	if len(temp1) != 0:
		nome.append(temp1)
		url_anime.append(temp2)
		#La grammatica è importante
		if len(temp1) == 1:
			risultato = ' risultato'
		else:
			risultato = ' risultati'
		print('['+ str(len(nome)) + '] ' + 'TnsFansub ha '+ str(len(temp1)) + risultato)

	while not Nsito:
		sito = input('\nInserisci il numero del sito[n] che vuoi usare: ')
		if not int(sito) > len(nome):
			Nsito = True
		else:
			print('Inserisci un numero valido di un sito')
	for dati1, dati2 in zip(nome[int(sito)-1], url_anime[int(sito)-1]):
		print('[' + str(a) + ']' + dati1)
		a = a + 1

parser = argparse.ArgumentParser(description='Script per facilitare il download di contenuti dal web.')
parser.add_argument('Input', type=str, help='URL o percorso di un file .txt o nome dell\'anime.')
parser.add_argument('-r', '--ricerca', help='Ricerca in modo automatico gli url dell\' anime desiderato.', action='store_true')

args = parser.parse_args()

if args.ricerca:
	searcher(args.Input)
elif re.compile('https?:\/\/.*').match(args.Input):
	NASDL(args.Input)
else:
	lines = open(args.Input).read().splitlines()
	for url in lines:
		NASDL(url)