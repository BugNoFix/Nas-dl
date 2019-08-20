#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (c) 2018 games195. Under MIT License.

import requests, os, re, json
from utilies import RemoveSpecialCharacter

# Load configs
CONFIG = json.load(open('setting.json'))

AnimeForce_VALID = r'https?:\/\/ww(w|1).animeforce\.org\/.*'

def AnimeForce(URL):
    page = requests.get(URL).text
    name = re.search(r'<title>(.*) - AnimeForce<\/title>', str(page), re.IGNORECASE).group(1)
    for link in re.findall(r'<a href="(.*)" target="_blank"(?: rel="noopener noreferrer")?><img src="\/DDL\/download\.png"', str(page)):
        if not link.startswith('http'):
            URL = 'https:' + link
        else:
            URL = link
        page = requests.get(URL).text
        AnimeLink = re.search(r'<a href="(.*)" target="_blank">Download<\/a>', str(page), re.IGNORECASE).group(1)
        os.system('exe\\youtube-dl {0} -o "{1}/{2}/{3}"'.format(AnimeLink, CONFIG['Path'], RemoveSpecialCharacter(name), '%(title)s.%(ext)s'))
