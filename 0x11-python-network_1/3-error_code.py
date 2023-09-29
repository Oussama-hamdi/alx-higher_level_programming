#!/usr/bin/python3
"""Sends a request to the URL and displays the body of the response"""

import urllib.request
import urllib.error
import sys

url = sys.argv[1]
try:
    with urllib.request.urlopen(url) as response:
        content = response.read().decode('utf-8')
        print(content)
except urllib.error.HTTPError as err:
    print("Error code: {}".format(err.code))
