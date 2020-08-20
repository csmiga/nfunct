#!/usr/bin/env python

import requests

# Get cookie from response
url = 'https://pluto.tv'
requests.get(url)
requests.get(url).cookies

# Give cookie back to server on subsequent request
#url = 'https://pluto.tv'
#cookies = dict(cookies_are='working')
#get_url = requests.get(url, cookies=cookies)`
