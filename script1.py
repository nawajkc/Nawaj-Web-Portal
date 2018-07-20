
from flask import Flask, render_template, url_for

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return render_template("FRONT.html") #html files should be in a template folder in the directory

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/algorithms/')
def algorithms():
    return render_template("algorithms.html")

@app.route('/projects/')
def projects():
    return render_template("projects.html")

if __name__ == "__main__":
    app.run(debug=True)
