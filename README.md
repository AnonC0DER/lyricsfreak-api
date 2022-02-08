# lyricsfreak-api
 An unofficial API for lyricsfreak.com using django and django rest framework.



## Usage
```
from requests import get
import json

query = 'nothing else matters metallica' 
url = f"http://127.0.0.1:8000/api/search-lyrics/{query}"

req = get(url).text

req = json.loads(req)

print(req)
```
