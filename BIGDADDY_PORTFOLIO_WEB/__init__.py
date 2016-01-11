from flask import Flask, url_for, redirect, request, render_template;
import redis;
r = redis.StrictRedis('localhost',6379,0,charset="UTF-8",decode_responses=True);

app = Flask(__name__)

# This is a main route to main site Svilar davor portfolio
@app.route('/')
def portfolio():
    return render_template('index.html')

# This is a route to holistic site towards holistic.html
@app.route('/holistic')
def holistic():
    return render_template('holistic.html')

# This is a route to two funduros site towards login.html
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'TWO' or request.form['password'] != 'FUNDUROS':
            error = 'Site is under construction, come again later !!!'
        else:
            return redirect(url_for('funduros'))
    return render_template('login.html', error=error)

@app.route('/funduros')
def funduros():
    return render_template("twofunduros.html")

@app.route('/page1')
def page1():
    return render_template("page1.html")

@app.route('/page2')
def page2():
    return render_template("page2.html")

@app.route('/page3')
def page3():
    return render_template("page3.html")

# This is a route to quiz site towards create question redis answer

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':

        return render_template('CreateQuestion.html');
    elif request.method == 'POST':

        title = request.form['title'];
        question = request.form['question'];
        answer = request.form['answer'];
        r.set(title +':question', question)
        r.set(title +':answer', answer)
        return render_template('CreatedQuestion.html', question = question,title = title, answer = answer);
    else:
        return "<h2>Invalid request</h2>";

@app.route('/question/<title>', methods=['GET', 'POST'])
def question(title):
    if request.method == 'GET':
        question = r.get(title+':question')
        return render_template('AnswerQuestion.html', question = question,title = title);
    elif request.method == 'POST':
        submittedAnswer = request.form['submittedAnswer'];
        answer = r.get(title+':answer')
        if submittedAnswer == answer:
            return render_template('Correct.html');
        else:
            return render_template('Incorrect.html', submittedAnswer = submittedAnswer, answer = answer);
    else:
        return '<h2>Invalid request</h2>';

# This is a route to quiz site WHOS ZOUR DADDY

@app.route("/main")
def main():
    return render_template("main.html")

@app.route("/wrong")
def wrong():
    return render_template("wrong.html")

@app.route("/right")
def right():
    return render_template("right.html")

if __name__ == '__main__':
    app.run()

