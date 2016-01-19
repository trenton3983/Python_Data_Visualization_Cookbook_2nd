import requests
from pprint import pprint
url = 'https://api.github.com/users/justglowing'
r = requests.get(url)
json_obj = r.json()
pprint(json_obj)
