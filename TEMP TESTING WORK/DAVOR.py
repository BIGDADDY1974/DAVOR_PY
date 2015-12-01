from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/wrong")
def wrong():
    return render_template("wrong.html")

@app.route("/right")
def right():
    return render_template("right.html")

if __name__ == "__main__":
    app.run()