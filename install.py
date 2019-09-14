#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (c) 2019 bugnofix. Under MIT License.


import os, re, glob, shutil, zipfile, time, sys
# Controllo le libreria mancanti e le installo
try:
	try:
		import requests
	except:
		os.system('pip install requests')
		import requests
	try:
		import cfscrape
	except:
		os.system('pip install cfscrape')
		import cfscrape
	module = True
except:
	module = False


def youtube_dl():
	
	print('download youtube-dl..')
	url = 'https://yt-dl.org/downloads/2019.08.13/youtube-dl.exe'
	r = requests.get(url)
	
	# Scarico l'eseguibile youtube-dl
	with open(r'exe\\youtube-dl.exe', 'wb') as f:
		f.write(r.content)
	
	# Aggiorno youtube-dl
	os.system('exe\\youtube-dl.exe -U')

def phantom_js():
	
	print('download phantom-js..')
	url = 'https://phantomjs.org/download.html'
	page = requests.get(url).text

	# Cerco l'ultima versione di phantom-js
	r = re.search(r'<a href="(.*)">phantomjs.*windows\.zip<\/a>', str(page), re.IGNORECASE).group(1)
	file = requests.get(r)

	# Scarico il file zip di phantom-js
	with open(r'temp.zip', 'wb') as f:
		f.write(file.content)

	# Estraggo il file zip
	with zipfile.ZipFile('temp.zip', 'r') as zip_ref:
		zip_ref.extractall('temp1')
	lista = glob.glob('temp1/phantomjs-*-windows/bin/phantomjs.exe')
	for dire in lista:
		os.rename(dire, 'exe\\phantomjs.exe')

	# Elimino i file inutili
	os.remove('temp.zip')
	shutil.rmtree('temp1')

def ffmpeg_ffprobe():

	print('download FFmpeg e FFprobe..')
	url = 'https://ffmpeg.zeranoe.com/builds/win64/static/'
	page = requests.get(url).text

	# Cerco l'ultima versione di ffmpeg
	r = re.search(r'<a href="(ffmpeg-.*-win64-static\.zip)" title="ffmpeg-.*-static\.zip">', str(page), re.IGNORECASE).group(1)
	file = requests.get(url + r)

	# Scarico il file zip
	with open(r'temp.zip', 'wb') as f:
		f.write(file.content)
	with zipfile.ZipFile('temp.zip', 'r') as zip_ref:
		zip_ref.extractall('temp1')

	# Cerco ffmpeg e lo inserisco nella cartella exe
	if not os.path.isfile('./ffmpeg.exe'):
		lista = glob.glob('temp1/ffmpeg-*-win64-static/bin/ffmpeg.exe')
		for dire in lista:
			os.rename(dire, 'exe\\ffmpeg.exe')

	# Cerco ffprobe e lo inserisco nella cartella exe
	if not os.path.isfile('./ffprobe.exe'):
		lista = glob.glob('temp1/ffmpeg-*-win64-static/bin/ffprobe.exe')
		for dire in lista:
			os.rename(dire, 'exe\\ffprobe.exe')

	# Elimino i file inutili
	os.remove('temp.zip')
	shutil.rmtree('temp1')

if __name__ == '__main__':
	
	# Variabili
	ok = '[\033[1;32;40mok\033[1;37;40m] '
	non_ok = '[\033[1;31;40mX\033[1;37;40m] '

	# Controllo se i moduli sono stati instalalti correttamente
	os.system('cls')
	if module:
		print(ok + 'I moduli sono installati')
	else:
		print(non_ok + 'I moduli non sono installati')

	# Creo la directory exe
	if not os.path.exists('./exe'):
		os.system('mkdir exe')

	# Installo youtube-dl
	try:
		if not os.path.isfile('./youtube-dl.exe'):
			youtube_dl()
		print(ok + "Youtube-dl è installato")
	except:
		print(non_ok + 'Youtube-dl non è installato')

	# Installo phantomjs
	try:
		if not os.path.isfile('./phantomjs.exe'):
			phantom_js()
		print(ok + "Phantom-js è installato")
	except:
		print(non_ok + 'Phantom-js non è installato')

	# Installo ffmpeg e ffprobe
	try:
		if not os.path.isfile('./ffmpeg.exe') or not os.path.isfile('./ffprobe.exe'):
			ffmpeg_ffprobe()
		print(ok + "FFmpeg è FFprobe sono installati")
	except:
		print(non_ok + 'FFmpeg è FFprobe non sono installati')


