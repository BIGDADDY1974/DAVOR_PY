from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def homepage():
    title =  "Sviki Diki is the best"
    paragraph = [" SO FUCK THE REST !!! SO FUCK THE REST !!! SO FUCK THE REST !!!"," SO FUCK THE REST !!! SO FUCK THE REST !!! SO FUCK THE REST !!!"]
    return render_template("index.html",title = title, paragraph = paragraph)
if __name__ == "__main__":
    app.run()