import git
from flask import Flask, render_template, url_for, flash, redirect, request

from flask import Flask
app = Flask(__name__)                    # this gets the name of the file so Flask knows it's name

@app.route("/")                          # this tells you the URL the method below is related to
def hello_world():
    return "<p>Hello, World Again!!!</p>"        # this prints HTML to the webpage

@app.route("/update_server", methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('/home/Elizabeth152/Web_Frameworks')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400
if __name__ == '__main__':               # this should always be at the end
    app.run(debug=True, host="0.0.0.0")