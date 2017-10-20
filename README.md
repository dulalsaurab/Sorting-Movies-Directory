# Sorting Movies Directory(IMDB and Rotten Tomatos score)

This project reads the movies names
from a given directory and generates a csv file sorting the movies according it's imdb and rottentomatoes rating. 

Note: This script find details of movies listed on IMDB and on rottentomatoes only. It won't work for those movies which are not listed on either IMDB or on Rotten Tomatos

**Dependencies**


    
**General steps followed**
      
      Read movies from the directory 
      
      Trim movies name to obtain required title using guessit library 
      
      Use imdb API to obtain movies detail 
      
      Use rottentomatoes api to obtain movies details
      
      Write to csv file sorting movies according to imdb rating, please view an example output present in this repo
      
    finally, watch movie having highest imdb rating, dont waste your time searching good movies from your movies collection 
    cheers, 
