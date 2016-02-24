('''
@author 'Saurab Dulal'

This scripts reads your movies name from your movies directory and generates a csv file sorting movies according its imdb rating and 
some minor movies description

    Note: This script find details of movies listed on IMDB only, dont try some iliwood movies :D

    reads movies from directory 
    trim movies name to obtain required title using guessit library 
    uses imdb API to obtain movies detail 
    write to csv file sorting movies according to imdb rating
    finally, watch movie having highest imdb rating, dont waste your time searching good movies from your database
    cheers, 

''')


#----------------list of probable library used ---------------------

from os import walk
import urllib.request
import requests
import json
from guessit import guessit
import operator
import csv

#------------------------------------------------


#reading movies name from movies directory

def IMDBscrapingAPI():

	mypath = 'path/to/your/movies/directory/'
	print(mypath)
	files = []
	for (dirpath, dirnames, filesname) in walk(mypath):
		files.extend(dirnames)
		files.extend(filesname)
		break
	return files


#obtaining movies detail from imdb

def ScrapingFromIMDB(nameList):

	moviesDataDict = []
	print (len(nameList))
	for names in nameList:
		# now we will use guessit library to extract movie title from complete name
		nameDict = guessit(names)
		movieName = nameDict['title']
		arg = movieName
		results = requests.get("http://www.omdbapi.com/?t="+arg)
		intoJson = results.json()
		#print(intoJson['Response'])
		if(intoJson['Response'] == 'False'):
			continue
		else:
			intoJson.pop('Response',None)
			intoJson.pop('Response',None)
			intoJson.pop('Poster',None)
			intoJson.pop('Type',None)
			intoJson.pop('Rated',None)
			intoJson.pop('imdbID',None)
			moviesDataDict.append(intoJson)
		#moviesDataDict.update(results.json())
	moviesDataDict.pop()
	moviesDataDict.sort(key=operator.itemgetter('imdbRating'),reverse=True)

	for idx,val in enumerate(moviesDataDict):

		print(moviesDataDict[idx]['Title']+' , Imdb Rating '+moviesDataDict[idx]['imdbRating'])

	WriteToCSV(moviesDataDict)


# writing movies detail with sorted list to a csv file

def WriteToCSV(listOfDictonary):

	keys = listOfDictonary[0].keys()
	with open('completeMoviesInfo.csv', 'w') as output_file:
		dict_writer = csv.DictWriter(output_file, keys)
		dict_writer.writeheader()
		dict_writer.writerows(listOfDictonary)


def main():
	fileLists = IMDBscrapingAPI()
	ScrapingFromIMDB(fileLists)

if __name__ == "__main__":
    main()
