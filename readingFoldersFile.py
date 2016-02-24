#this file extracts movies name from ftp server 

from ftplib import FTP
import os # allows me to use os.chdir
from os import walk

port=21
ip="192.168.50.22"
password='rdw@2011'
directory = '/RDW/Media/Movies/HOLLYWOOD'

#changes the active dir - this is where downloaded files will be saved to
def readFilesFromServer():

	ftp = FTP(ip)
	ftp.login('rdw',password)
	#set directory 
	ftp.cwd(directory)
	#list all files
	files = ftp.nlst()
	
	for filename in files:
		print(filename)
	return files 

	
#this function is for reading files from local env
def readLocalFiles():
	#mypath = '/media/django/TOSHIBA EXT/ALLMedia/movies/HOLLYWOOD'
	mypath = 'D:/Saurab Dulal/buffer/IMDB A/moviesName'
	print(mypath)
	files = []
	for (dirpath, dirnames, filesname) in walk(mypath):
		files.extend(dirnames)
		files.extend(filesname)
		break
	return files	
#function getting files from local server ends
