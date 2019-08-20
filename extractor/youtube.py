#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (c) 2018 games195. Under MIT License.

import os, json, sys

# Load configs
CONFIG = json.load(open('setting.json'))

YouTube_VALID = r'https?:\/\/www.youtube.com\/(?:watch|playlist)\?(?:v|list)\=.*'

def YouTube(URL):
    print('Cosa vuoi scaricare?\n[1] Musica\n[2] Video')
    Input = input().title()
    if Input in ['1', 'Musica']:
        cmd = '--extract-audio --audio-format mp3'
        Path = CONFIG['MusicPath']
    elif Input in ['2', 'Video']:
        # cmd = ''
        # Path = CONFIG['VideoPath']
        sys.exit('\nOpzione in WIP')
    else:
        sys.exit('[/**\] Input non valido!')
    os.system('exe\\youtube-dl {0} -o "{1}/{2}" {3}'.format(URL, Path, '%(title)s.%(ext)s', cmd))
