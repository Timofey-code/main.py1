import random
facts_list = ["Random fact 1",
              "Random fact 2",
              "Random fact 3",
              "random fact 4"]
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Главная страница</h1>"

@app.route("/secret")
def secret():
    return "<h1>You found da secret page! well done.</h1>"

@app.route("/hello/<name>")
def name(name):
    return f"Hello, {name}"
app.run(debug=True)