#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (c) 2018 games195, BugNoFix. Under MIT License.

import requests, os, re, json, cfscrape, threading, time
from utilies import RemoveSpecialCharacter
from threading import Thread

# Load configs
CONFIG = json.load(open('setting.json'))

Dreamsub_VALID = r'https?:\/\/www.dreamsub\.(co|online|stream)\/.*'

def Dreamsub(URL):
    sess = cfscrape.create_scraper(requests.session())
    page = (sess.get(URL).text)
    name = re.search(r'<h1>(.*) Streaming.*<\/h1>', page, re.IGNORECASE).group(1)
    ep = re.search(r'<b>Episodi<\/b>: ([0-9]*)(?:\+)?<br>', page, re.IGNORECASE).group(1)
    for n in range(0, int(ep) + 1):
        print("boh")
        sess = cfscrape.create_scraper(requests.session())
        page = sess.get('{}/{}/'.format(URL, n)).text
        keepem = re.search(r'https?:\/\/keepem.online\/(?:f|embed)\/...........', page, re.IGNORECASE)
        if keepem:
            os.system('youtube-dl {0} -o "{1}/{2}/{3}"'.format(keepem.group(), CONFIG['Path'], RemoveSpecialCharacter(name), '%(title)s.%(ext)s'))

