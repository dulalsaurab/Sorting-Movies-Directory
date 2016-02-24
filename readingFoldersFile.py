'''
Created on Feb 21, 2016

@author: Saurab Dulal
Sorting Movies Directory

'''
#this file extracts movies name from ftp server 
from ftplib import FTP
import os # allows me to use os.chdir
from os import walk

port=21
ip="FTP_IP_ADDRESS"
password='FTP_PASSWORD'
directory = '/directory/to/your/movies/folder/'

#you can use one of the two function below, either read from ftp server or from your local movie directory

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
	#examplePath = '/media/django/TOSHIBA EXT/ALLMedia/movies/HOLLYWOOD'
	mypath = '/directory/to/your/movies/folder/'
	print(mypath)
	files = []
	for (dirpath, dirnames, filesname) in walk(mypath):
		files.extend(dirnames)
		files.extend(filesname)
		break
	return files	
#function getting files from local server ends
