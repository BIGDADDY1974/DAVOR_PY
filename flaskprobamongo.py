from flask import Flask, render_template, request, redirect
import os
from pymongo import MongoClient

def connect():
# Substitute the 5 pieces of information you got when creating
# the Mongo DB Database (underlined in red in the screenshots)
# Obviously, do not store your password as plaintext in practice
    connection = MongoClient("ds053128.mongolab.com",53128)
    handle = connection["demo"]
    handle.authenticate("demo-user","12345678")
    return handle

app = Flask(__name__)
handle = connect()


@app.route("/index" ,methods=['GET'])
@app.route("/", methods=['GET'])
def index():
    userinputs = [x for x in handle.mycollection.find()]
    return render_template('index.html', userinputs=userinputs)

@app.route("/write", methods=['POST'])
def write():
    userinput = request.form.get("userinput")
    oid = handle.mycollection.insert({"message":userinput})
    return redirect ("/")

@app.route("/deleteall", methods=['GET'])
def deleteall():
    handle.mycollection.remove()
    return redirect ("/")

# Remove the "debug=True" for production
if __name__ == "__main__":
   app.run()