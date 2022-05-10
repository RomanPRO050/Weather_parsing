import cgitb
import pathlib
from pathlib import Path
from peewee import *
from flask import Flask
import weather

app = Flask(__name__)


@app.route("/")
def base_output():
    cgitb.enable()
    dir_path = pathlib.Path.home()
    path = Path(dir_path, 'PycharmProjects', 'Weather_parsing', 'weather.sqlite')
    db = SqliteDatabase(path)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Weather")
    result = cursor.fetchall()
    print(f"Content-Type: text/html; charset=utf-8\n\n")
    overall = ""
    for results in result:
        # print("Content-type: text/html")
        print()
        str1 = " | ".join(map(str, results))
        overall += str1 + f"<br>"
    return f'{overall}'


weather.DatabaseUpdater.base_updater()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4567)
