#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (c) 2018 games195. Under MIT License.

import requests, os, re, json
from utilies import RemoveSpecialCharacter

# Load configs
CONFIG = json.load(open('setting.json'))

HentaiHaven_VALID = r'https?:\/\/hentaihaven\.org\/.*'
HentaiHaven_SERIES= r'https?:\/\/hentaihaven\.org\/series\/.*'


def HentaiHaven(URL):
    def download(link):
        page = requests.get(link).text
        name = re.search(r'<title>(.*) - Episode .*\|.*\|.*<\/title>', str(page), re.IGNORECASE).group(1)
        AnimeLink = re.search(r'res="720p"  label="720p" src="(.*)" type=\'video/mp4\'  data-res="720"\/>', str(page), re.IGNORECASE).group(1)
        os.system('exe\\youtube-dl {0} -o "{1}/{2}/{3}"'.format(AnimeLink, CONFIG['Path'], RemoveSpecialCharacter(name), '%(title)s.%(ext)s'))

    def series(link):
        page = requests.get(URL).text
        for link in re.findall(r'class="brick-title" href="(.*)">.*<\/a><\/h3>', str(page)):
            download(link)

    if re.compile(HentaiHaven_SERIES).match(URL):
        series(URL)
    else:
        download(URL)
