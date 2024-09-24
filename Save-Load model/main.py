from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/', methods =['POST'])
def getdata():
    Predictor = int(request.form['Predictor'])

    #-----------------------------------------
    import pickle
    with open('model_pickle', 'rb') as file:

        md = pickle.load(file)

        # print(md.coef_)
        # print(md.intercept_)
        result = int(md.predict([[Predictor]]))
    #-----------------------------------------

    #return render_template('pass.html', p=result)
    return render_template('index.html', p=result)

if __name__ == "__main__":
    app.run(debug=True)