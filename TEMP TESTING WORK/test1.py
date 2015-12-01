from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def homepage():
    title =  "Sviki Diki is the best"
    paragraph = [" SO FUCK THE REST !!! SO FUCK THE REST !!! SO FUCK THE REST !!!"," SO FUCK THE REST !!! SO FUCK THE REST !!! SO FUCK THE REST !!!"]
    return render_template("index.html",title = title, paragraph = paragraph)

@app.route('/about')
def aboutpage():
    title =  "About this site"
    paragraph = ["blah blah blah memememememmemememe blah blah blah"]
    pagetype = "about"
    return render_template("index.html",title = title, paragraph = paragraph, pagetype = pagetype)
if __name__ == "__main__":
    app.run()