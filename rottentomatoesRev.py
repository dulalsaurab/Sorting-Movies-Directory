
'''since rotten tomatos api returns multiple results, we need movies data to extract exact information 
thus those input movies having data on it will be porcessed otherwise it will be rejected

#http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey=ny97sdcpqetasj8a4v2na8va&q=Pain+&+Gain+2013

'''

from os import walk
import urllib.request
import requests 
import json
from guessit import guessit
import operator
import csv



def rottenTomatosMoviesDataAPI(moviesName):
	
	ListOfDictRT = list()
	for movies in moviesName:
		moviesTitle = guessit(movies)
		URL = "http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey=ny97sdcpqetasj8a4v2na8va&q="+moviesTitle['title']
		# print (URL)
		
		results = requests.get(URL)
		if results.status_code==200:
		
			intoJson = results.json()
		
			for items in intoJson["movies"]:
				if moviesTitle['title'].upper() == items['title'].upper():
					if moviesTitle['year'] == items['year']:
					
						items['ratings'].pop('critics_rating',None)
						items['ratings'].pop('audience_rating',None)
						items['ratings']['movieName'] = moviesTitle['title']
						print(items['ratings'])
						ListOfDictRT.append(items['ratings'])
					else:
						print("movies year not matched")
		else:
			print("no response from server for"+moviesTitle['title'])
	return ListOfDictRT
	
	# print (intoJson["movies"]["ratings"])

	