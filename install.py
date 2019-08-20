import os, re, glob, shutil, zipfile, time, sys
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
	print('installing youtube-dl..')
	url = 'https://yt-dl.org/downloads/2019.08.13/youtube-dl.exe'
	r = requests.get(url)
	with open(r'exe\\youtube-dl.exe', 'wb') as f:
		f.write(r.content)
	# install last version of youtube-dl
	os.system('exe\\youtube-dl.exe -U')

def phantom_js():
	print('installing phantom-js..')
	url = 'https://phantomjs.org/download.html'
	page = requests.get(url).text
	r = re.search(r'<a href="(https:\/\/bitbucket\.org\/ariya\/phantomjs\/downloads\/phantomjs-2\.1\.1-windows\.zip)">phantomjs.*windows\.zip<\/a>', str(page), re.IGNORECASE).group(1)
	file = requests.get(r)
	with open(r'temp.zip', 'wb') as f:
		f.write(file.content)
	with zipfile.ZipFile('temp.zip', 'r') as zip_ref:
		zip_ref.extractall('temp1')

	lista = glob.glob('temp1/phantomjs-*-windows/bin/phantomjs.exe')
	for dire in lista:
		os.rename(dire, 'exe\\phantomjs.exe')
	os.remove('temp.zip')
	shutil.rmtree('temp1')

def ffmpeg_ffprobe():
	print('installing FFmpeg e FFprobe..')
	url = 'https://ffmpeg.zeranoe.com/builds/win64/static/'
	page = requests.get(url).text
	r = re.search(r'<a href="(ffmpeg-.*-win64-static\.zip)" title="ffmpeg-.*-static\.zip">', str(page), re.IGNORECASE).group(1)
	file = requests.get(url + r)
	with open(r'temp.zip', 'wb') as f:
		f.write(file.content)
	with zipfile.ZipFile('temp.zip', 'r') as zip_ref:
		zip_ref.extractall('temp1')
	if not os.path.isfile('./ffmpeg.exe'):
		lista = glob.glob('temp1/ffmpeg-*-win64-static/bin/ffmpeg.exe')
		for dire in lista:
			os.rename(dire, 'exe\\ffmpeg.exe')
	if not os.path.isfile('./ffprobe.exe'):
		lista = glob.glob('temp1/ffmpeg-*-win64-static/bin/ffprobe.exe')
		for dire in lista:
			os.rename(dire, 'exe\\ffprobe.exe')
	os.remove('temp.zip')
	shutil.rmtree('temp1')


ok = '[\033[1;32;40mok\033[1;37;40m] '
non_ok = '[\033[1;31;40mX\033[1;37;40m] '
os.system('cls')
if module:
	print(ok + 'All modules are installed')
else:
	print(non_ok + 'The modules are not installed')
# install youtube-dl
try:
	if not os.path.isfile('./youtube-dl.exe'):
		youtube_dl()
	print(ok + "Youtube-dl is installed")
except:
	print(non_ok + 'Youtube-dl is not installed')

# install phantomjs
try:
	if not os.path.isfile('./phantomjs.exe'):
		phantom_js()
	print(ok + "Phantom-js is installed")
except:
	print(non_ok + 'Phantom-js is not installed')

# install ffmpeg and ffprobe
try:
	if not os.path.isfile('./ffmpeg.exe') or not os.path.isfile('./ffprobe.exe'):
		ffmpeg_ffprobe()
	print(ok + "FFmpeg and FFprobe are installed")
except:
	print(non_ok + 'Ffmpeg and ffprobe are not installed')


