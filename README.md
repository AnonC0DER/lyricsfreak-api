# lyricsfreak-api
 An unofficial API for lyricsfreak.com using django and django rest framework. <br>
 I created this API using web scraping, Django and Django rest framework.


## Usage
```python
from requests import get
import json

query = 'nothing else matters metallica' 
url = f"http://127.0.0.1:8000/api/search-lyrics/{query}?format=json"

req = get(url).text

req = json.loads(req)

print(req)
```
