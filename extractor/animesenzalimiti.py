#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (c) 2018 games195, BugNoFix. Under MIT License.

import requests, os, re, json
from utilies import RemoveSpecialCharacter, OpenloadStreamangoCheck

# Load configs
CONFIG = json.load(open('setting.json'))

AnimeSenzaLimiti_VALID = r'https?:\/\/animesenzalimiti\.(net|co)\/.*'

def AnimeSenzaLimiti(URL):
    page = requests.get(URL).text
    name = re.search(r'<h1 class="entry-title">(.*)<\/h1>', str(page), re.IGNORECASE).group(1)
    ep = re.search(r'<a href=".*"><span class="pagelink">(.*)<\/span></a>', page).group(1)

    for ep in range(1, int(ep) + 1):
        pageURL = '{}{}/'.format(URL, ep)
        page = requests.get(pageURL).text

        openload = re.search(r'src="(https?:\/\/(?:openload|oload)\..*\/(?:f|embed)\/.*)" scrolling="no"', str(page), re.IGNORECASE).group(1)
        if openload and OpenloadStreamangoCheck(openload):
            os.system('exe\\youtube-dl {0} -o "{1}/{2}/{3}"'.format(openload, CONFIG['Path'], RemoveSpecialCharacter(name), '%(title)s.%(ext)s'))
            continue

        streamango = re.search(r'src="(https?:\/\/streamango\.com\/embed\/.*)" scrolling="no"', str(page), re.IGNORECASE).group(1)
        if streamango and OpenloadStreamangoCheck(streamango):
            os.system('exe\\youtube-dl {0} -o "{1}/{2}/{3}"'.format(streamango, CONFIG['Path'], RemoveSpecialCharacter(name), '%(title)s.%(ext)s'))
            continue

        # Else
        if not OpenloadStreamangoCheck(openload) and not OpenloadStreamangoCheck(streamango):
            print('[NAS-DL] Non trovo nessun link valido nella pagina {}.'.format(pageURL))
