#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (c) 2018 games195, BugNoFix. Under MIT License.
import requests, json, os, re, unidecode


# Load configs
CONFIG = json.load(open('setting.json'))
'''
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
'''
VVVVID_VALID = r'https:\/\/www\.vvvvid\.it\/show\/(.*)\/.*'

def vvvvidSeasonDownloader(URL):
    #variabili
    season_id=[]
    nome = []
    video_id = []
    
    #get show-id
    show_id= re.match(VVVVID_VALID, URL).group(1)

    #get connection id
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
        'Content-Type':'application/json',
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Origin':'https://www.vvvvid.it',
        'X-Requested-With':'XMLHttpRequest',
        'Sec-Fetch-Mode':'cors',
        'Sec-Fetch-Site':'same-origin'
    }
    raw_data = '{"action":"login","email":"safsaf@asfsa.asf","password":"1Q2w3e4r5t","facebookParams":"","isIframe":false,"mobile":false,"hls":true,"dash":true,"flash":false,"webm":true,"wv+mp4":true,"wv+webm":true,"pr+mp4":false,"pr+webm":false,"fp+mp4":false,"login_type":"force","reminder":true}'
    sess = requests.session()
    r = sess.post('https://www.vvvvid.it/user/login', data=raw_data, headers=headers)
    DATI = json.loads(r.content.decode('utf-8'))
    conn_id = DATI['data']['conn_id']

    #get season-id, name for url and video-id
    user = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
    info = sess.get('https://www.vvvvid.it/vvvvid/ondemand/{0}/seasons/?conn_id={1}'.format(show_id, conn_id), headers=user)
    DATI = json.loads(info.content.decode('utf-8'))
    for i in range(0,len(DATI['data'][0]['episodes'])):
        season_id.append(DATI['data'][0]['episodes'][i]['season_id'])
        video_id.append(DATI['data'][0]['episodes'][i]['video_id'])
        temp = DATI['data'][0]['episodes'][i]['title']
        temp = unidecode.unidecode(temp)
        temp = temp.replace("\'"," ")
        temp = temp.replace(" ","-")
        nome.append(temp)

    #download
    for a in range(0,len(nome)):
        url = '{0}/{1}/{2}/{2}'.format(URL, season_id[a], video_id[a], nome[a])
        os.system('exe\\youtube-dl {} -o {}/{}'.format(url, CONFIG['Path'], '%(series)s/%(episode_number)s.%(ext)s'))

def vvvvid(URL):
    
    Input = input('Cosa vuoi scaricare?\n[1] Stagione\n[2] Episodio\nOpzione: ').title()

    # Download all episodes.
    if Input in ['1', 'Stagione']:
        vvvvidSeasonDownloader(URL)
        


