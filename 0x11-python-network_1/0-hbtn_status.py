!#/usr/bin/python3
"""Ascript that
- fetches  https://alx-intranet.hbtn.io/status ans uses urllib package
"""


if __name__ == "__main__":
    import urllib.request


    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        body = res.read()
        print("- type: {}".format(type(body)))
        print("- content: {}".format(body))
        print("- utf8 content: {}".format(body.decode('utf-8')))
