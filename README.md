This was one of my very first Python projects and was created in March of 2023.

# Python-Web-Scraper
This is a web crawler designed to scrape Wikipedia.

# Crawler.py
This is a web scraper designed to store the HTML files of Wikipedia pages. This program first creates a SQLite (database) file to store the information of the pages it scrapes. The program starts on a given URL and gets the HTML of the page using URLlib. It then uses BeautifulSoup to parse the HTML and sort out the links, headers, and titles on the page. It saves all of these to the previously created SQLite file. Due to using a database, the program can be stopped and started again with minimal loss of data. 

# Analisys.py
This program was designed to use the previously collected data from the crawler.py file. This program was designed to draw conclusions from the data in the SQLite file. Currently, these files look through the HTML files stored and finds pages that have headers with the title of 'History'. This program will then display the most common headers in the SQLite database.
