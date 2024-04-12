from flask import Flask, render_template


app = Flask(__name__)
@app.route('/')
def print_h():
    return render_template("index.html")

app.run()