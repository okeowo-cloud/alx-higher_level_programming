#!/usr/bin/python3
"""5-hbtn_header Module"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    r = requests.get(url)
    print("{}".format(r.headers.get("X-Request-Id")))
