from flask import Flask, url_for, request, render_template;
from TriviaMVAApp import app;

from TriviaMVAApp.models.sqlclient import Client;

# server/
@app.route('/')
def hello():
    return render_template('starter.html');


# server/create
@app.route('/create1', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('CreateQuestion1.html');
    elif request.method == 'POST':
        title = request.form['title'];
        question = request.form['question'];
        answer = request.form['answer'];

        client = Client();
        client.saveQuestion(title, question, answer);
    
        return render_template('CreatedQuestion1.html', question = question,title = title);
    else:
        return "<h2>Invalid request</h2>";

# server/question/<title>
@app.route('/question1/<title>', methods=['GET', 'POST'])
def question(title):
    if request.method == 'GET':
        client = Client();
        question = client.getQuestion(title);
        return render_template('AnswerQuestion1.html', question = question);
    elif request.method == 'POST':
        submittedAnswer = request.form['submittedAnswer'];

        client = Client();
        answer = client.getAnswer(title)

        if submittedAnswer == answer:
            return render_template('Correct1.html');
        else:
            return render_template('Incorrect1.html', submittedAnswer = submittedAnswer, answer = answer);
    else:
        return '<h2>Invalid request</h2>';