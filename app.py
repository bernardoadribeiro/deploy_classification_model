import pickle
from flask import Flask, jsonify, render_template, request

## Import prediction models
iris_model = pickle.load(open('models/iris_decision_tree_model.pkl', 'rb'))


app = Flask(__name__)


## App routes ##
@app.route('/')
def index():
    """Index route. Load index page."""
    return render_template('index.html')

@app.route('/predict/iris/<float:sw>/<float:sl>/<float:pw>/<float:pl>', methods=['GET'])
def get_iris_predict(sw, sl, pw, pl):
    """
        Returns the predictions based on the input data as JSON.

        sw: <float> SepalWidth 
        sl: <float> SepalLeight
        pw: <float> PetalWidth
        pl: <float> PetalLeight
    """
    
    result = iris_model.predict([[sw, sl, pw, pl]])

    if result[0] == 0:
        result_class = 'Iris setosa'
    elif result[0] == 1:
        result_class = 'Iris versicolour'
    else:
        result_class = 'Iris virginica'

    return jsonify({'Class_name': result_class})

@app.route('/predict/iris/form/', methods=['GET', 'POST'])
def iris_predict_form():
    """
        Implements a form page to predict iris flowers.

        GET: Returns the form page
        POST: Returns the result class using the inputed data in the form
            params: 
            - sepall: <float> SepalWidth
            - sepalw: <float> SepalLeight
            - petall: <float> PetalWidth
            - petalw: <float> PetalLeight
    """

    if request.method == 'GET':
        return render_template('iris/index.html', title='Predict')

    if request.method == 'POST':
        sepall = request.form.get('sepall')
        sepalw = request.form.get('sepalw')
        petall = request.form.get('petall')
        petalw = request.form.get('petalw')

        result = iris_model.predict([[sepall, sepalw, petall, petalw]])

        if result[0] == 0:
            result_class = 'Iris setosa'
        elif result[0] == 1:
            result_class = 'Iris versicolour'
        else:
            result_class = 'Iris virginica'

        return render_template('iris/index.html', result = result_class)


## App config ##
app.debug = True


## App start ##
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, host='0.0.0.0')