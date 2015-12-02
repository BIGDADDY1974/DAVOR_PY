from flask import Flask,request,render_template,url_for,redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'TWO' or request.form['password'] != 'FUNDUROS':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('homepage'))
    return render_template('login.html', error=error)

@app.route('/index')
def homepage():
    return render_template("index.html")

@app.route('/page1')
def page1():
    return render_template("page1.html")

@app.route('/page2')
def page2():
    return render_template("page2.html")

@app.route('/page3')
def page3():
    return render_template("page3.html")

if __name__ == "__main__":
    app.run()

