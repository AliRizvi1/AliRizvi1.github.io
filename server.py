"""
This is the file that 'runs' the server.
AliRizvi99.pythonanywhere.com
"""
from flask import Flask, request, send_file, render_template

app = Flask(__name__)

visited = 0;

@app.route("/")
def home():
    global visited
    visited = visited + 1
    #return "Hello World!" + name
    return render_template("index.html", visited=visited)

