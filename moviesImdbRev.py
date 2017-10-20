'''('''
@author 'Saurab Dulal'

This script reads movies name from a given movie directory and generates a csv file sorting movies according it's imdb rating and 
some minor movies description

    Note: This script only find details of movies listed on IMDB only, it will not work for movies not listed withing IMDB DB

    Read movies from a given directory 
    trim movies name to obtain required title using guessit library 
    uses imdb API to obtain movies detail 
    write to csv file sorting movies according to imdb rating
    finally, watch movie having highest imdb rating, dont waste your time searching good movies from your movie directory
    cheers, 

''')


#----------------list of probable library used ---------------------'''

from os import walk
import urllib.request
import requests 
import json
from guessit import guessit
import operator
import csv
from rottentomatoesRev import rottenTomatosMoviesDataAPI 
from readingFoldersFile import readFilesFromServer
from readingFoldersFile import readLocalFiles


def ScrapingFromIMDB(nameList):
	
	moviesDataDict = []
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
			#rejecting some of the elements from json returned through api,comment those element you dont want to reject
			intoJson.pop('Response',None)	
			intoJson.pop('Response',None)
			intoJson.pop('Poster',None)
			intoJson.pop('Type',None)
			intoJson.pop('Rated',None)
			intoJson.pop('imdbID',None)
			intoJson.pop('Language',None)
			intoJson.pop('Plot',None)
			intoJson.pop('Runtime',None)
			intoJson.pop('Genre',None)
			intoJson.pop('Writer',None)
			intoJson.pop('Country',None)
			intoJson.pop('Awards',None)
			moviesDataDict.append(intoJson)
		#moviesDataDict.update(results.json())
	try:
		moviesDataDict.pop()
	except Exception as e:
		print (e);
		return False
		
	moviesDataDict.sort(key=operator.itemgetter('imdbRating'),reverse=True)

	for idx,val in enumerate(moviesDataDict):
		
		print(moviesDataDict[idx]['Title']+' , Imdb Rating '+moviesDataDict[idx]['imdbRating'])

	return moviesDataDict
	# WriteToCSV(moviesDataDict)

#------------------------------------------------------------------------------------------------------------------
# Writing final result to csv file 

def WriteToCSV(listOfDictonary):

	keys = listOfDictonary[0].keys()
	print(keys)
	with open('completeMoviesInfo.csv', 'w') as output_file:
		dict_writer = csv.DictWriter(output_file, keys)
		dict_writer.writeheader()
		dict_writer.writerows(listOfDictonary)

#------------------------------------------------------------------------------------------------------------------
def main():
	#fileLists = readLocalFiles()
	fileLists = readFilesFromServer()
	moviesDataDictIMDB = ScrapingFromIMDB(fileLists)
	moviesDataDictRT = rottenTomatosMoviesDataAPI(fileLists)
	finalResults = list()
	
	for moviesfromIMDB in moviesDataDictIMDB:
		flag = False
		for moviesfromRT in moviesDataDictRT:
			if moviesfromIMDB['Title'].upper() == moviesfromRT['movieName'].upper():
				print("Inside merger")
		#print(moviesDataDictIMDB[i])
		#print(moviesDataDictRT[i])
				tempA = moviesfromIMDB.copy() 
				tempA.update(moviesfromRT)
				#print(temp)
				finalResults.append(tempA)
				flag = True
				print(tempA)
				break
				
		if flag == False:		
			tempB = moviesfromIMDB.copy() 
			empty = {'critics_score':'', 'audience_score':'', 'movieName':''}
			tempB.update(empty)
			finalResults.append(tempB)
			print(tempB)
	#print (finalDict)
	
	
	WriteToCSV(finalResults)
if __name__ == "__main__":
    main()
