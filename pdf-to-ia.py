"""
usage: python3 pdf-to-ia.py <filename> <title> <date> <description> <creator> <subject> ...

uploads a pdf to internet archive, with metadata fields as listed
"""

import sys
from internetarchive import upload

MY_ACCESS_KEY = "v5SsdIdwUq8VAWL5"
MY_SECRET_KEY = "sXvuqvKZH6TvOBmb"

filename = sys.argv[1]
title = sys.argv[2]
date = sys.argv[3]
desc = sys.argv[4]
creator = sys.argv[5]
subjects = sys.argv[5:]

md = {'collection': 'opensource', 'mediatype': 'texts', 'title': title, 'date': date, 'description': desc, 'creator': creator, 'subject': subjects}
print(md)
r = upload(filename[:-4], files=[filename], metadata=md, access_key=MY_ACCESS_KEY, secret_key=MY_SECRET_KEY)
print("internet archive upload status:", r[0].status_code)
