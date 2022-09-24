#!/usr/bin/python3
"""10-my_github Module"""

if __name__ == "__main__":
    from sys import argv
    import requests
    from requests.auth import HTTPBasicAuth

    username, password = (argv[1], argv[2])
    url = "https://api.github.com/user"
    r = requests.get(url, auth=HTTPBasicAuth(username, password))
    print(r.json().get('id'))
