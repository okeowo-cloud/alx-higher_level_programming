#!/usr/bin/python3
"""8-json_api Module"""

if __name__ == "__main__":
    from sys import argv
    import requests

    url = "http://0.0.0.0:5000/search_user"
    var = "" if len(argv) == 1 else argv[1]
    r = requests.post(url, data={'q': var})
    try:
        dic = r.json()
        if dic:
            print(f"[{dic.get('id')}] {dic.get('name')}")
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid JSON")
