#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (c) 2018 games195, BugNoFix. Under MIT License.

import requests, os, re, json
from utilies import RemoveSpecialCharacter

# Load configs
CONFIG = json.load(open('setting.json'))

CB01_VALID = r'https?:\/\/(?:www\.)?cb01\.zone\/.*'

def CB01(URL):
    page = requests.get(URL).text
    swzz = re.search(r'<a href="(http:\/\/swzz\.xyz\/link\/.*)" target="_blank" rel="noopener noreferrer">Openload<\/a>', str(page), re.IGNORECASE).group(1)
    if swzz:
        page = requests.get(swzz).text
        openload = re.search(r'<a href="(https?:\/\/(?:openload|oload)\..*\/(?:f|embed)\/.*)" class="', str(page), re.IGNORECASE)
        os.system('exe\\youtube-dl {0} -o "{1}/{2}"'.format(openload.group(1), CONFIG['Path'], '%(title)s.%(ext)s'))
