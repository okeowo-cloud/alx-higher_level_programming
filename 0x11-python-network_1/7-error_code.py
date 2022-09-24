#!/usr/bin/python3
"""7-error_code Module"""

if __name__ == "__main__":
    import requests
    import sys

    try:
        r = requests.get(sys.argv[1])
        o = r.text if r.status_code == 200 else f"Error code: {r.status_code}"
        print(o)
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(e.code))
