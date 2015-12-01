from flask import Flask, render_template,url_for

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/page1')
def page1():
    return render_template("index1.html")

if __name__ == "__main__":
    app.run()

