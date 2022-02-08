from urllib.parse import urlencode, urlunparse
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import random
import json


def Random_user_agent():
    '''Get random user agent'''
    
    file = open('API/user_agents/user_agents.txt', 'r')
    data = file.read()

    user_agents = data.split('\n') 

    User_agents_list = []
    for user in user_agents:
        try:
            User_agents_list.append(user)
        except:
            pass
        
    return {'User-Agent' : random.choice(User_agents_list)}


def Get_lyrics(query):
    '''Get lyrics using lyrics freak'''

    lyricsFreak = 'https://www.lyricsfreak.com'
    # Prepare url
    url = urlunparse(('https', 'www.lyricsfreak.com', '/search.php', '', urlencode({'q': query}), ''))
    # make request
    req = Request(url, headers=Random_user_agent())
    page = urlopen(req)
    # Read html page
    soup = BeautifulSoup(page.read(), 'lxml')

    # Find links
    links = soup.findAll('a', {'class' : 'song'})
    # Find artists
    artists = soup.findAll('div', {'class' : 'lf-list__cell lf-list__title--secondary'})

    MusicLinks = []
    artistsStr = []

    for music in links:
        MusicLinks.append(music['href'])

    for artist in artists:
        artistsStr.append(artist.text.replace('·     ', ''))
	
    
    try:
        # Prpare url
        WebUrls = [lyricsFreak + MusicLinks[0]]
    
    except:
        pass
    
    # Get new user agent
    LyricsText = []

    try:
        for url in WebUrls:
            # make request
            req = Request(url, headers=Random_user_agent())
            page = urlopen(req)
            soup = BeautifulSoup(page.read(), 'lxml')
            lyrictxt = soup.findAll('div', {'class' : 'lyrictxt js-lyrics js-share-text-content'})

            TextStr = []

            # Append each line to the list
            for line in lyrictxt:
                TextStr.append(line.text)

            LyricsText.append(' '.join(TextStr))
        
        return LyricsText[0]
    
    except UnboundLocalError:
        return 'Not Found'