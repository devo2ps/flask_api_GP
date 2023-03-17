# app.py

from flask import render_template #got rid of import Flask for this stage
import connexion

app = connexion.App(__name__, specification_dir="./") #removed import Flask up top to instead use connexion.App
app.add_api("swagger.yml")

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

