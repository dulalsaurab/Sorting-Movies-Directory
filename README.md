# Sorting Movies Directory(IMDB and Rotten Tomatoes score)

This project is just for fun. Usually, I watch movies during the weekend and mostly I stuck to decide which one to watch from the list of movies that are in my drive. Because I want to watch a good movie with fairly good IMDB ratings and along with good critical feedback, I have to google the names and find out a good one. To remove this hassle, I scripted some python and solved the issue. 

Thus, these scripts read movies names
from a given directory and it generates a CSV file sorting the movies according to it's IMDB and rotten tomatoes rating. 

Note: This script finds details of movies listed on IMDB and on rotten tomatoes only. It won't work for those movies which are not listed on either IMDB or on Rotten Tomatoes

**Dependent Libraries**

Developed on Windows 7 mechine 

python 3.x +

- import urllib.request
- json
- guessit
- operator
- csv 
- ftplib 

you can use pip to install these libraries or, you can compile the binaries.  
    
**General steps followed**
      
- Read movies from the directory 
      
- Trim movies name to obtain required title using guessit library 
      
- Use imdb API to obtain movies detail 
      
- Use rottentomatoes api to obtain movies details
      
- Write to csv file sorting movies according to imdb rating, please view an example output present in this repo
      
    
Finally, watch movie having highest imdb rating, dont waste your time searching good movies from your movies collection 
    cheers, 
