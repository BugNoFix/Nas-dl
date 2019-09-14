#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (c) 2018 bugnofix, games195. Under MIT License.

import requests, os, re, json, urllib.parse
from utilies import RemoveSpecialCharacter

# Load configs
CONFIG = json.load(open('setting.json'))

AnimeForce_VALID = r'https?:\/\/ww(w|1).animeforce\.org\/.*'
base_url = 'https://ww1.animeforce.org/?s='

def AnimeForce(URL):
    # Cerco i dati
    page = requests.get(URL).text
    name = re.search(r'<title>(.*) Sub Ita Download &amp; Streaming - AnimeForce<\/title>', str(page), re.IGNORECASE).group(1)
    
    # Scarico tutti gli episodi
    for link in re.findall(r'<a href="(.*)" target="_blank"(?: rel="noopener noreferrer")?><img src="\/DDL\/download\.png"', str(page)):
        if not link.startswith('http'):
            URL = 'https:' + link
        else:
            URL = link
        page = requests.get(URL).text
        AnimeLink = re.search(r'<a href="(.*)" target="_blank">Download<\/a>', str(page), re.IGNORECASE).group(1)
        os.system('exe\\youtube-dl {0} -o "{1}/{2}/{3}"'.format(AnimeLink, CONFIG['Path'], RemoveSpecialCharacter(name), '%(title)s.%(ext)s'))
'''
def AnimeForceSearcher():
    anime = input("Dimmi il nome da cercare: ")
    # Encodo url
    encode = urllib.parse.quote_plus(anime)
    url = base_url + encode
    # Richiesta
    page = requests.get(url).text
    dati = re.findall(r'<a href="(https:\/\/ww1\.animeforce\.org\/.*-sub-ita-download-streaming\/)"', str(page), re.IGNORECASE).group(1)
    #print(dati)
'''
