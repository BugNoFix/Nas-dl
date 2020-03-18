#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (c) 2018 games195. Under MIT License.

import requests, re, os, subprocess, json, shlex
from utilies import RemoveSpecialCharacter

# Load configs
CONFIG = json.load(open('setting.json'))

def DownloadAnime(url):
    page = str((requests.get(url=url, headers={'User-Agent': CONFIG['UserAgent']})).text)

    # Parsing informations
    JSON = json.loads(re.search(r'vilos\.config\.media = ({.*});', page, re.IGNORECASE).group(1))
    
    # Normal ep
    try:
        data = re.search(r'<title>(.*) Episodio ([0-9]*), .*, - Guardalo su Crunchyroll<\/title>', page)
        episode = data.group(2) 
        if int(episode) < 10:
            episode = "0" + episode
    # Extra
    except:
        data = re.search(r'<title>(.*) (Episodio .*), .*, - Guardalo su Crunchyroll<\/title>', page, re.IGNORECASE)
        episode = data.group(2) 
    
    # Set data
    name = RemoveSpecialCharacter(data.group(1))

    for streams in JSON['streams']:
        if streams['hardsub_lang'] == CONFIG['Crunchyroll']['Lang']:
            m3u8 = streams['url']
            break

    os.system('exe\\youtube-dl "{0}" -o "{1}/{2}/{3} {4}"'.format(m3u8, CONFIG['Path'], name, name, episode + ".mp4"))

def Playlist(url):
    page = str((requests.get(url=url, headers={'User-Agent': CONFIG['UserAgent']})).text)
    links = []
    for link in re.findall(r'<a href="(.*)" title=".*"', page):
        links.append('http://www.crunchyroll.com/' + link)

    num = len(links) - 1
    while num >= 0:
        DownloadAnime(links[num])
        num -= 1

    print('[CrunchyRipper] All downloads are done.')

def crunchyroll(URL):
    if re.compile(r'https?:\/\/www.crunchyroll.com\/it\/(?:.*\/.*|media)-([0-9]*)').match(URL):
        print('[CrunchyRipper] Found a single episode...')
        DownloadAnime(URL)
    elif re.compile(r'https?:\/\/www.crunchyroll.com\/it\/.*').match(URL):
        print('[CrunchyRipper] Found a playlist...')
        Playlist(URL)
