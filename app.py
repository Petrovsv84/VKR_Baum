from flask import Flask, render_template,request
from processing import load_scaler,load_rast,load_upr

app = Flask(__name__)

@app.route('/',methods=['get','post'])#127.0.0.1:5000/
def main():
    scaler=load_scaler()
    pred_rast=load_rast()
    pred_upr=load_upr()

    message="Введите показатели"
    if request.method == 'POST':
        x1 = request.form.get('x1')
        x2 = request.form.get('x2')
        x3 = request.form.get('x3')
        x4 = request.form.get('x4')
        x5 = request.form.get('x5')
        x6 = request.form.get('x6')
        x7 = request.form.get('x7')
        x8 = request.form.get('x8')
        x9 = request.form.get('x9')
        x10 = request.form.get('x10')
        x11 = request.form.get('x11')
        x12 = request.form.get('x12')

        try:
            x1=float(x1)
            x2=float(x2)
            x3=float(x3)
            x4=float(x4)
            x5=float(x5)
            x6=float(x6)
            x7=float(x7)
            x8=float(x8)
            x9=float(x9)
            x10=float(x10)
            x11=float(x11)
            x12=float(x12)
            X_ML=[x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12]
            y_upr_pred=y_upr_pred(X_ML)
            y_rast_pred= y_rast_pred(X_ML)
            message = f'Прогнозные значения для:/nМодуль упругости при растяжении, ГПа: {y_upr_pred}/n/nПрочность при растяжении, МПа: {y_rast_pred}'
        except:
            message="ОЙ"

        print(x1)

    return render_template("index.html", message=message)




app.run()