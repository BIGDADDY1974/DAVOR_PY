from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def homepage():
    return render_template("index.html",title = " Sviki Diki is the best", paragraph = " SO FUCK THE REST !!!")
if __name__ == "__main__":
    app.run()