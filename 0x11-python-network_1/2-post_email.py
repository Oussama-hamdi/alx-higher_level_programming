#!/usr/bin/python3
"""Sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)"""

import urllib.request
import urllib.parse
import sys

url, email = sys.argv[1], sys.argv[2]

data = urllib.parse.urlencode({"email": email}).encode("utf-8")
with urllib.request.urlopen(url, data=data) as req:
    print(r.read().decode("utf-8"))
