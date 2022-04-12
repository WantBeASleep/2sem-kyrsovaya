# from crypt import methods
from flask import Flask, render_template, request
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    pngFlag = 0
    message = 'Gipoteza'
    HTTPmethod=request.method
    if request.method == 'POST':
        A = np.array([float(item) for item in request.form.get('area1').split()])
        B = np.array([float(item) for item in request.form.get('area2').split()])
        
        alpha = 0.05

        mean_A = A.mean()
        mean_B = B.mean()

        size_A = A.shape[0]
        size_B = B.shape[0]

        S_2_A = A.var(ddof=1)
        S_2_B = B.var(ddof=1)

        t = (mean_A-mean_B)/np.sqrt((S_2_A/size_A+S_2_B/size_B))
        df = (S_2_A/size_A+S_2_B/size_B)**2 / ((S_2_A/size_A)**2/(size_A-1)+(S_2_B/size_B)**2/(size_B-1))
        pvalue = 1 - (stats.t.cdf(t,df) - stats.t.cdf(-t,df))

        if pvalue/2<alpha:
            message = 'accept gipoteza'
        else:
            message = 'not accept gipoteza'

        x = np.linspace(mean_A-np.sqrt(S_2_A)*4,mean_A+np.sqrt(S_2_A)*4,200)

        pdf1 = stats.norm.pdf(x,mean_A,np.sqrt(S_2_A))
        pdf2 = stats.norm.pdf(x,mean_B,np.sqrt(S_2_B))

        plt.plot(x,pdf1 , color = 'red')
        plt.plot(x,pdf2 , color = 'blue')        
        plt.savefig('static/plot.png')
        pngFlag = 1
    return render_template("index.html", HTTPmethod=HTTPmethod, message=message, pngFlag=pngFlag)

# @app.route('/user/<string:name>/<int:id>')
# def user(name,id):
#     return "User page: " + name + " - " + str(id)

if __name__ == "__main__":
    app.run(debug=True)