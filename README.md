# Sorting Movies Directory by IMDB and Rotten Tomatoes score

This project is just for fun. Usually, I watch movies during the weekend and mostly I get stuck to decide which one to watch from the list of movies that are in my drive. Because I want to watch a good movie with fairly good IMDB ratings and good critical feedback, I have to google the names to find out about them. To remove this hassle, I scripted simple python and almost solved the issue. 

Thus, these scripts read movies names
from a given directory and it generates a CSV file sorting the movies according to it's IMDB and rotten tomatoes rating. 

**Note: This script finds details of movies listed on IMDB and on rotten tomatoes only. It won't work for those movies which are not listed on either IMDB or on Rotten Tomatoes**

## Dependent Libraries

Development Date: February 21, 2016 

Developed on Windows 7 machine 

python 3.x +

- urllib
- json
- guessit
- operator
- csv 
- ftplib 

you can use pip to install these libraries or, you can compile the binaries.  
    
## Steps followed 
      
- Read movies from the given directory 
      
- Trim movies name to obtain required title using guessit library 
      
- Use imdb API to obtain movies detail 
      
- Use rottentomatoes api to obtain movies details
      
- Write to csv file sorting movies according to imdb rating, please view an example output present in this repo

- Finally, watch movie having highest rating. Don't waste your time searching good movies from your movies collection 
    

## Limitations
- Depends on lots of libraries
- Need to specify directory path on the code itself
    - directory = *'/directory/to/your/movies/folder/'* on the file **readingFoldersFile.py**
- It uses web-scraping, so the codes are time dependent and needs manual configuration and changes at later time
- Need to know basic programming syntax 


    

