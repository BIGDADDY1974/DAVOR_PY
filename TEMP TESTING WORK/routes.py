from flask import Flask, url_for, request, render_template
from app import app
import redis

r=redis.StrictRedis('localhost',6379,0, decode_responses=True,charset='utf-8');

@app.route('/')
def hello():
    return """
<html>
  <body>
  <div class="nav">
    <div class="container">
	<ul>
	  <li>Davor Svilar</li>
	  <li>Browse</li>
	</ul>
	<ul>
	<li>Sign Up</li>
	<li>Log in</li>
	<li>Help</li>
	</ul>
	</div>
	<div class="jumbotron">
	    <div>
	    <h3>"Travel"</h3>
	    <p>"From apartments and rooms to treehouses and boats: stay in unique spaces in 192 countries."</p>
	    <p>
	        <a href="#">"See how to travel on Airbnb"</a>
	    </p>
	    </div>
	    <div class="container">
	       <h1>"Find a place to stay."</h1>
	       <p>"Rent from people in over 34,000 cities and 192 countries."</p>
        </div>
        <div>
            <h3>Subheading</h3>
            <p>Description text.</p>
            <p>
                <a href="#">Link text</a>
            </p>
        </div>
    </div>
  </div>
  </body>
</html>"""
    url = url_for('about');
    link = '<a href="' + url + '">About us!</a>';
    return link;

@app.route('/about')
def about():
    return 'We are the knights who say Ni!!';

@app.route('/question/<title>', methods=['GET', 'POST'])
def question(title):
    if request.method == 'GET':
        question = r.get(title+':question')
        return render_template('AnswerQuestion.html',
                               question = question)
    elif request.method == 'POST':
        submittedAnswer = request.form['submittedAnswer'];

        answer=r.get(title+':answer')

        if submittedAnswer == answer:
            return render_template('Correct.html');
        else:
            return render_template('Incorrect.html',
                                   answer = answer,
                                   submittedAnswer = submittedAnswer);

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'GET':
        return render_template('CreateQuestion.html');
    elif request.method == 'POST':
        question = request.form['question'];
        answer = request.form['answer'];
        title = request.form['title'];

        r.set(title+':question',question);
        r.set(title+':answer',answer);

        return render_template('CreatedQuestion.html',
                               question = question);
    return;