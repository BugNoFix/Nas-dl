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
	# Openlaod
	elif re.compile(r'https?:\/\/(?:openload|oload)\..*\/(?:f|embed)\/.*').match(URL):
		os.system('youtube-dl {0} -o "{1}/{2}"'.format(URL, CONFIG['Path'], '%(title)s.%(ext)s'))
	# Streamango
	elif re.compile(r'https?:\/\/streamango\..*\/(?:f|embed)\/.*').match(URL):
		os.system('youtube-dl {0} -o "{1}/{2}"'.format(URL, CONFIG['Path'], '%(title)s.%(ext)s'))
	else:
		print('[NAS-DL] URL non valido! [ {} ]'.format(URL))
		pass

parser = argparse.ArgumentParser(description='Script per facilitare il download di contenuti dal web.')
parser.add_argument('URL', type=str, help='URL o percorso di un file .txt.')
args = parser.parse_args().URL

if re.compile('https?:\/\/.*').match(args):
	NASDL(args)
else:
	lines = open(args).read().splitlines()
	for url in lines:
		NASDL(url)

url_anime = []
nome = []
anime = input("Dimmi il nome da cercare: ")
#Dreamsub
temp1, temp2 = DreamsubSearcher(anime)
nome.append(temp1)
url_anime.append(temp2)
if len(nome) > 0:
	print('['+ str(len(nome)-1) + '] ' + 'Dreamsub ha '+ str(len(temp1)) + ' risultati')
#altri


a = 0
sito = input('Inserisci il numero del sito[n] che vuoi usare: ')
for dati1, dati2 in zip(nome[int(sito)], url_anime[int(sito)]):
	print('[' + str(a) + ']' + dati1)
	a = a + 1