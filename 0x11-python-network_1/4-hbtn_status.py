#!/usr/bin/python3
"""4-hbtn_status Module"""

if __name__ == "__main__":
    import requests

    url = "https://alx-intranet.hbtn.io/status"
    r = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
