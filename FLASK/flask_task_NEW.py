### THIS IS A FLASK TASK

from flask import Flask
app = Flask(__name__)
wsgi_app = app.wsgi_app


@app.route("/")
def hello():
    return "HELLO WORLD !!!!!!!!"

@app.route("/user/<username>")
def callback(username):
    return "HELLO " + username + " WORLD !!!"

@app.route("/about")
def about():
    return "HELLO THERE !!!"

if __name__ == "__main__":
    app.run()

