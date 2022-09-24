#!/usr/bin/python3
"""1-hbtn_header Module"""

if __name__ == "__main__":
    import urllib.request
    import sys

    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print("{}".format(response.getheader("X-Request-Id")))
