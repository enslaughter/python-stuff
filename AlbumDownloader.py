import urllib.request
import sys
import os.path
from bs4 import BeautifulSoup

album_page = sys.argv[1]
save_path = sys.argv[2]

page = urllib.request.urlopen(album_page)

soup = BeautifulSoup(page, 'html.parser')
songno = 0
		
tdlist = soup.find_all("td", class_="playlistDownloadSong")

def mp3_writer(url, songno):
	mp3path = urllib.request.urlopen(url)
	mp3data = mp3path.read()
	grabbedname = "Album Download -%s.mp3" %(songno)
	filename = os.path.join(save_path, grabbedname)
	f = open(filename, "wb+")
	f.write(mp3data)
	f.close()

for td in tdlist:
	songno = songno+1
	songurl = td.find("a").attrs['href']
	trueurl = "https://downloads.khinsider.com/" + songurl
	
	liburl = urllib.request.urlopen(trueurl)
	loopsoup = BeautifulSoup(liburl, 'html.parser')
	
	songid = loopsoup.find("audio")
	funcurl = songid.attrs['src']
	print(funcurl)
	mp3_writer(funcurl, songno)

input('Press ENTER to Exit')