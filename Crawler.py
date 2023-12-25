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


# Create the Data Base
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

comm = sqlite3.connect('web-cralwer.sqlite')
cur = comm.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Pages
    (id INTEGER PRIMARY KEY, url TEXT UNIQUE, html TEXT,
     error INTEGER, title TEXT, headers TEXT UNIQUE, got INTEGER)''')





x = input("Url here --> ")
pastxs = []


while True:
    try:
        if ( len(x) < 1 ) : x = 'https://en.wikipedia.org/wiki/Bonnie_J._Dunbar'
        if ( x.endswith('/') ) : x = x[:-1]
        web = x
        print(x)
        if ( x.endswith('.htm') or x.endswith('.html') ) :
                pos = x.rfind('/')
                web = x[:pos]

        # Get the data
        document = urlopen(x, context=ctx)
        
        #Check for errors
        html = document.read()
        if document.getcode() != 200 :
            print("Error on page: ",document.getcode())
            x = random.choice(p_href)
            continue
                 #   cur.execute('UPDATE Pages SET error=? WHERE url=?', (document.getcode(), url) )

        if 'text/html' != document.info().get_content_type() :
            x = random.choice(p_href)
            print("Ignore non text/html page")
            continue
            
        if x == 'https://en.wikipedia.org/wiki/Main_Page' :
            x = random.choice(p_href)
            print("No main page") # Has weird formating with h2 tags
            continue
        
        cut = x[9:] 
        if cut.find(':') != -1: 
            p_ref.remove(x)
            x = random.choice(p_href)
            print('Ignore special pages')
            continue
                  
        
        # Make the data readable
        soup = BeautifulSoup(html, "html.parser")
       
        cur.execute('INSERT OR IGNORE INTO Pages (url, html) VALUES ( ?, ?)', ( x, html) )
       
    
    except KeyboardInterrupt:
        print('')
        print('Program interrupted by user...')
        comm.commit()
        break    
   

    except:
        x = random.choice(p_href) # replace
        continue        
    
        

    p_href = []
    a_tags = soup('a')
    for tag in a_tags:   # Cleans anchor tags to only links
            href = tag.get('href', None)
            if ( href is None ) : continue
            # Resolve relative references like href="/contact"
            up = urlparse(href)
            if ( len(up.scheme) < 1 ) :
                href = urljoin(x, href)
            ipos = href.find('#')
            if ( ipos > 1 ) : href = href[:ipos]
            if ( href.endswith('.png') or href.endswith('.jpg') or href.endswith('.gif') ) : continue
            if ( href.endswith('/') ) : href = href[:-1]
            # print href
            if ( len(href) < 1 ) : continue
            if (href.startswith(x[:15]) == True):
                if href.find('index.php') == -1 :
                    p_href.append(href) # replace with insert statment
            #else:
                #print(href)










    h1_tags = soup('span')
    for tag in h1_tags:  #Looks for 'mw-page-title-main' class in span
        fct = tag.get('class')
        if fct != None:
            for n in fct:
                if n == 'mw-page-title-main':
                    tag = str(tag)
                    pos = tag.find('>')
                   # print(pos)
                    near = tag[pos+1:]
                    clost = near.find('<')
                    heading = (near[:clost])
                    if heading.find(':') == -1:
                        print(heading) # replace with insert
                        break
                    else:
                        x = random.choice(p_href)
                        continue
        else:
            pass








    #grabs h2 tags
    headers = []
    h2 = soup('h2')
    for tag in h2: # Cleas h2 tags to just contents
        stag = str(tag)
        stag = stag[4:]
        pos = stag.find('>')
        #print(stag)
        #print(pos)
        #print(stag[pos:])
        near = stag[pos:]
        if near.startswith('><span'): #more thatn one span sometimes
            near = near[5:]
            d = near.find('span')
            #print(d)
            near = near[d+4:]
        if near.startswith('></span>'): # idk why this happeds
            near = near[8:]
            g = near.find('>')
            near = near[g:]
        if near.startswith('><i'): #sombody put italics in the headers
            near = near[2:]
            #print(near)
            v = near.find('</i>')
            fp = near[1:v]
            sp = near[v+4:]
            #print(fp)
            #print(sp)
            near = fp + sp
        #print(near)
        far = near.find('<')
        
       
        s = near[1:far]
        
        headers.append(near[1:far])
        print(near[1:far])
       # print('header')
    try: # update everything
        cur.execute('UPDATE Pages SET error=? WHERE url=?', (document.getcode(), x) )
        cur.execute('UPDATE Pages SET title=? WHERE url=?', (heading, x) )
        cur.execute('UPDATE Pages SET headers=? WHERE url=?', (str(headers), x) )
    except:
        pass
    
    pastxs.append(x)
    comm.commit
    
    
    while True:
        x = random.choice(p_href)
        if x in pastxs: # Check if we allready visited the page
            pass
            p_href.remove(x)
            print("skipping")
        else:
            break
     
    #break
    

























