#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (c) 2018 games195, BugNoFix. Under MIT License.

import requests, json, os, re

# Load configs
CONFIG = json.load(open('setting.json'))

VVVVID_VALID = r'https?:\/\/www.vvvvid.it\/(#!show|show)\/(.*)'

def vvvvid(URL):
    Input = input('Cosa vuoi scaricare?\n[1] Stagione\n[2] Episodio\nOpzione: ').title()

    show_id, season_id = re.match(VVVVID_VALID, URL).groups()

    # Download all episodes.
    if Input in ['1', 'Stagione']:
        # Get `conn_id`.
        #data = json.loads(requests.get('https://www.vvvvid.it/user/login', headers={'User-Agent': CONFIG['UserAgent']}).text)
        #conn_id = data['data']['conn_id']
        sess = requests.session()
        url = 'https://www.vvvvid.it/login'
        values = {'username': 'safsaf@asfsa.asf',
                  'password': '1Q2w3e4r5t'}

        r = sess.post(url, data=values)
        print(r.content)
        # Get JSON Playlist.
        #JSON_Link = 'https://www.vvvvid.it/vvvvid/ondemand/{}/season/{}?conn_id={}'.format(show_id, season_id, conn_id)
        JSON_Link = sess.get("https://www.vvvvid.it/show/780/tokyo-ghoulre")
        JSON = json.loads(sess.get(JSON_Link, headers={'User-Agent': CONFIG['UserAgent']}).text)

        # Get number of episodes.
        Num_Ep = len(JSON['data'])

        for x in range(Num_Ep):
            URL = 'https://www.vvvvid.it/#!show/{}/useless/{}/{}/useless'.format(show_id, season_id, JSON['data'][x]['video_id'])
            os.system('youtube-dl {} -o {}/{}'.format(URL, CONFIG['Path'], '%(series)s/%(episode_number)s.%(ext)s'))

    # Download single episodes.
    elif Input in ['2', 'Episodio']:
        os.system('youtube-dl {} -o {}/{}'.format(URL, CONFIG['Path'], '%(series)s/%(episode_number)s.%(ext)s'))
