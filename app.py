# app.py

from flask import render_template #got rid of import Flask for this stage


# Remove: import connexion

import config

from models import Person


app = config.connex_app

app.add_api(config.basedir / "swagger.yml")


@app.route("/")

def home():

    people = Person.query.all()

    return render_template("home.html", people=people)


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=8000, debug=True)


""" (old form prior to p2)
import connexion

app = connexion.App(__name__, specification_dir="./") #removed import Flask up top to instead use connexion.App
app.add_api("swagger.yml")

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
"""
