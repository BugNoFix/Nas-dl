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
    name = re.search(r'{"id":.*,"collection_id":.*,"group_id":.*,"name":"(.*)","duration":.*,"tags":.*};', page, re.IGNORECASE).group(1)
    serie_name = re.search(r'(.*) - .* - .*', name, re.IGNORECASE).group(1)
    episode = re.search(r'.* - Episode (.*) - .*', name, re.IGNORECASE).group(1)

    for streams in JSON['streams']:
        if streams['hardsub_lang'] == CONFIG['Crunchyroll']['Lang']:
            m3u8 = streams['url']

    print('[CrunchyRipper] Downloading {} episode...'.format(episode))

    # file_name = ('[Raws195] {} [Sub {}].{}').format(name, CONFIG['Crunchyroll']['Lang'], CONFIG['Crunchyroll']['FileExtension'])
    file_name = ('{}.{}').format(episode, CONFIG['Crunchyroll']['FileExtension'])
    file_name = RemoveSpecialCharacter(file_name)
    serie_name = RemoveSpecialCharacter(serie_name)

    OutputPath = CONFIG['Path'] + '/' + serie_name + '/'
    FilePath = OutputPath + file_name

    if not os.path.exists(OutputPath):
        os.makedirs(OutputPath)
    if not os.path.isfile(FilePath):
        ffmpeg_command = ('ffmpeg -loglevel panic -i "{}" -c copy -bsf:a aac_adtstoasc "{}{}"').format(m3u8, OutputPath, file_name)
        subprocess.check_call(shlex.split(ffmpeg_command))
        print('[CrunchyRipper] Download finished.')
    else:
        print('[CrunchyRipper] Existing file. Skipping...')

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
