#!/usr/bin/env python3
import cgi
import cgitb
import pathlib
from pathlib import Path
from peewee import *

cgitb.enable()
dir_path = pathlib.Path.home()
path = Path(dir_path, 'PycharmProjects', 'Weather_parsing', 'weather.sqlite')
db = SqliteDatabase(path)
cursor = db.cursor()
cursor.execute("SELECT * FROM Weather")
result = cursor.fetchall()
print(f"Content-Type: text/html; charset=utf-8\n\n")
for results in result:
    # print("Content-type: text/html")
    print()
    print(f"<h1>{results}</h1>")
