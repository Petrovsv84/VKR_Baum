from flask import Flask, render_template,request


app = Flask(__name__)

@app.route('/',methods=['get','post'])#127.0.0.1:5000/
def main():
    if request.method == 'POST':
        x1 = request.form.get('x1')
        print(x1)
    return render_template("index.html")




app.run()