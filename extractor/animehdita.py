#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (c) 2018 games195. Under MIT License.

import requests, os, re, json
from utilies import OpenloadStreamangoCheck

# Load configs
CONFIG = json.load(open('setting.json'))

AnimeHDITA_VALID = r'http:\/\/www\.animehdita\.org.*'

def AnimeHDITA(URL):
    page = requests.get(URL).text

    openload = re.search(r'src="(https?:\/\/(?:openload|oload)\..*\/(?:f|embed)\/.*)"/ scrolling="no"', str(page), re.IGNORECASE).group(1)
    if openload and OpenloadStreamangoCheck(openload):
        os.system('youtube-dl {0} -o "{1}/{2}"'.format(openload, CONFIG['Path'], '%(title)s.%(ext)s'))
