#!/usr/bin/env python3.6
import urllib.request
from urllib.error import URLError,HTTPError

request = urllib.request.Request("http://localhost/ace/test.html")

try:
    urllib.request.urlopen(request,timeout=3)
except HTTPError as e:
    print(e.code)
    print(e.reason)
except URLError as e:
    if hasattr(e,"reason"):
        print(e.reason)
finally:
    print("finally...")