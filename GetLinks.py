import requests
from bs4 import BeautifulSoup
import re
import urllib.parse
from urllib.parse import urlparse

def googleSearch(query):
    g_clean = [ ] #this is the list we store the search results
    url = 'https://www.google.com/search?client=ubuntu&channel=fs&q={}&ie=utf-8&oe=utf-8'.format(query)#this is the actual query we are going to scrape
    try:
            html = requests.get(url)
            if html.status_code==200:
                soup = BeautifulSoup(html.text, 'lxml')
                a = soup.find_all('a') # a is a list
                for i in a:
                    k = i.get('href')
                    try:
                        m = re.search("(?P<url>https?://[^\s]+)", k)
                        n = m.group(0)
                        rul = n.split('&')[0]
                        domain = urlparse(rul)
                        if(re.search('google.com', domain.netloc)):
                            continue
                        else:
                            g_clean.append(rul)
                    except:
                        continue
    except Exception as ex:
        print(str(ex))
    finally:
        return g_clean
queries = [
'weather -wiki -youtube -google -amazon',
'maps -wiki -youtube -google -amazon',
'translate -wiki -youtube -google -amazon',
'calculator -wiki -youtube -google -amazon',
'speed -wiki -youtube -google -amazon',
'test -wiki -youtube -google -amazon',
'news -wiki -youtube -google -amazon',
'thesaurus -wiki -youtube -google -amazon',
'powerball -wiki -youtube -google -amazon',
'donald trump -wiki -youtube -google -amazon',
'nfl -wiki -youtube -google -amazon',
'g -wiki -youtube -google -amazon',
'f -wiki -youtube -google -amazon',
'periodic table -wiki -youtube -google -amazon',
'face -wiki -youtube -google -amazon',
'olympics -wiki -youtube -google -amazon',
'internet -wiki -youtube -google -amazon',
'cool math -wiki -youtube -google -amazon',
'dictionary -wiki -youtube -google -amazon',
'y -wiki -youtube -google -amazon',
'timer -wiki -youtube -google -amazon',
'hapyp wheels -wiki -youtube -google -amazon',
'tonka -wiki -youtube -google -amazon',
'overwatch -wiki -youtube -google -amazon',
'league of legends -wiki -youtube -google -amazon',
'restaurants -wiki -youtube -google -amazon',
'calendar -wiki -youtube -google -amazon',
'discover -wiki -youtube -google -amazon',
'movies -wiki -youtube -google -amazon',
'hillary clinton -wiki -youtube -google -amazon',
'game of thrones -wiki -youtube -google -amazon',
'cheap flights -wiki -youtube -google -amazon',
'animal jam -wiki -youtube -google -amazon',
'games mortgage calculator -wiki -youtube -google -amazon',
'bernie sanders -wiki -youtube -google -amazon',
'spanish to english -wiki -youtube -google -amazon',
'entertainment  -wiki -youtube -google -amazon',
'translator rick and morty -wiki -youtube -google -amazon',
'spotify web player -wiki -youtube -google -amazon',
'flights -wiki -youtube -google -amazon',
'english to spanish -wiki -youtube -google -amazon',
'irs -wiki -youtube -google -amazon',
'star wars -wiki -youtube -google -amazon',
'deadpool -wiki -youtube -google -amazon',
'sports -wiki -youtube -google -amazon',
'bitcoin -wiki -youtube -google -amazon',
'what is my ip -wiki -youtube -google -amazon',
'prodigy -wiki -youtube -google -amazon',
'suicide squad -wiki -youtube -google -amazon',
'spectrum -wiki -youtube -google -amazon',
'hurrican irma -wiki -youtube -google -amazon',
'taylor swift -wiki -youtube -google -amazon',
'go -wiki -youtube -google -amazon',
'happy birthday -wiki -youtube -google -amazon',
'weather radar -wiki -youtube -google -amazon',
'email -wiki -youtube -google -amazon',
'wonder woman -wiki -youtube -google -amazon',
'north korea -wiki -youtube -google -amazon',
'the -wiki -youtube -google -amazon',
'solitaire -wiki -youtube -google -amazon',
'apa citation -wiki -youtube -google -amazon',
'carrie fisher -wiki -youtube -google -amazon',
'audible -wiki -youtube -google -amazon',
'tis the season -wiki -youtube -google -amazon',
'directions -wiki -youtube -google -amazon',
'ariana grande -wiki -youtube -google -amazon',
'stranger things -wiki -youtube -google -amazon',
'powerball winning numbers -wiki -youtube -google -amazon',
'town of salem -wiki -youtube -google -amazon',
'nfl schedule -wiki -youtube -google -amazon',
'selena gomez -wiki -youtube -google -amazon',
'great clips -wiki -youtube -google -amazon',
'winter olympics -wiki -youtube -google -amazon',
'the walking dead -wiki -youtube -google -amazon',
'black panther -wiki -youtube -google -amazon',
'itunes -wiki -youtube -google -amazon',
'prince -wiki -youtube -google -amazon'
]
results = []
for query in queries:
    google_results = googleSearch(query)
    for google_result in google_results:
        results.append(google_result)

for result in results:
    print(result)
