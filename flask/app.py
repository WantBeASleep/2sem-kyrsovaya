from crypt import methods
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route('/user/<string:name>/<int:id>')
def user(name,id):
    return "User page: " + name + " - " + str(id)

if __name__ == "__main__":
    app.run(debug=True)