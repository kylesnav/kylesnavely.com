from flask import Flask, render_template
import os
from dotenv import load_dotenv

load_dotenv()

# = os.getenv('#')

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("pages/index.html", title="Home")

@app.route("/links")
def links():
    return render_template("pages/links.html", title="Links")

@app.route("/resume")
def resume():
    return render_template("pages/resume.html", title="Resume")

@app.route("/about")
def about():
    return render_template("pages/about.html", title="About")

@app.route("/contact")
def contact():
    return render_template("pages/contact.html", title="Contact")

if __name__ == "__main__":
    app.run(debug=True)