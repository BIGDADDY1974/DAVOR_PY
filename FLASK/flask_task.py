### THIS IS A FLASK TASK

from flask import Flask
app = Flask(__name__)

wsgi_app = app.wsgi_app

@app.route("/")
def hello():
    return "HELLO WORLD !!!!!!!!"

if __name__ == "__main__":
    app.run()

