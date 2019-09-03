#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (c) 2019 bugnofix. Under MIT License.

import requests, os, re, json, urllib.parse
from utilies import RemoveSpecialCharacter

# Load configs
CONFIG = json.load(open('setting.json'))

AnimeUnity_VALID = r'https:\/\/animeunity\.it\/.*'
base_url = 'https://animeunity.it/anime.php?c='

def AnimeUnity(URL):
	page = requests.get(URL).text
	name = re.search(r'<p>\s*<b>TITOLO: <\/b>(.*)											<\/p>', str(page), re.IGNORECASE).group(1)
	ep = re.findall(r'<div class="ep-box col-lg-1 col-sm-1" style="width:19%">\s*<a href="(anime\.php\?id=.*)" ', str(page), re.IGNORECASE)
	for link in ep:
		url = 'https://animeunity.it/'+ link
		print('exe\\youtube-dl {0} -o "{1}/{2}/{3}"'.format(url, CONFIG['Path'], RemoveSpecialCharacter(name), 'nome.%(ext)s'))