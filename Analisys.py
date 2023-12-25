# Libraries that deal with the database
import sqlite3 
import urllib.error
import ssl
# Libraries that deal with gathering the data
from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib.request import urlopen
# Libraries that deal with reading the data
import collections
collections.Callable = collections.abc.Callable
from bs4 import BeautifulSoup
import random
import json
import ast

# Sets up the data base
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

conn = sqlite3.connect('web-cralwer.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS words
    (id INTEGER PRIMARY KEY, word TEXT UNIQUE, count TEXT)''')

ph = []
counts = {}

s = input('how many: ')
g = 0
history_coutn = 0
listh = []
while True:
    g = g+1
    try:
        # Retres data from the database
        cur.execute('SELECT title,headers FROM Pages WHERE headers is not NULL and got is NULL ORDER BY RANDOM() LIMIT 1')

        
        data = cur.fetchone()
        

        if data != None:
            cur.execute('UPDATE pages SET got=? WHERE title=?', (1, str(data[0])) )
        else:
            print('done')
            break
        string = data[1]

        h = ast.literal_eval(string)

        print(str(g) + ": " +data[0])
        #print(h)

        #print(type(h))

        # look through data
        for i in h:
            counts[i] = counts.get(i, 0) + 1
            if str(i).find('history'): 
                history_coutn = history_coutn + 1
                if str(data[0]) in listh:
                        pass
                else: listh.append(str(data[0]))
                
        #print(counts)
    except KeyboardInterrupt:
        print('')
        cur.execute('UPDATE pages SET got=Null')
        print('Program interrupted by user...')
        break
#print(counts)
print('')
print('')
print('')
v = 0


for w in sorted(counts, key=counts.get, reverse=True):
    print(w, counts[w])
    v = v+1
    if v == int(s):
        break
        
print('')
print('')
print('')
# print the results
print('history articls: ' + str(history_coutn))
print('')
print(listh)
cur.execute('UPDATE pages SET got=Null')
