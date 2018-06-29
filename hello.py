#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup

s = requests.session()
response = s.get('https://github.com/login')

soup = BeautifulSoup(response.text)
for n in soup('input'):
    if n['name'] == 'authenticity_token':
        token = n['value']
        break

    # now post to that login page with some valid credentials and the token
auth = {
    'login': 'g.thuku15@live.com'
    , 'password': 'thukgeoW123'
    , '_csrf_token': token
}
s.post('https://github.com/login', data=auth)

response = s.get('https://github.com/settings/emails')
print(response.text)
