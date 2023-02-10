import pickle
from flask import Flask, render_template

## Import prediction models
iris_model = pickle.load(open('models/iris_decision_tree_model.pkl', 'rb'))


app = Flask(__name__)


## App routes ##
@app.route('/')
def index():
    """Index route. Load index page."""
    return render_template('index.html')

@app.route('/predict/iris/<float:sw>/<float:sl>/<float:pw>/<float:pl>', methods=['GET'])
def predict(sw, sl, pw, pl):
    """
        Returns the predictions based on the input data.

        sw: SepalWidth
        sl: SepalLeight
        pw: PetalWidth
        pl: PetalLeight
    """
    result = iris_model.predict([[sw, sl, pw, pl]])
    return "Class: {}".format(result)

## App config ##
app.debug = True


## App start ##
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, host='0.0.0.0')