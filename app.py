import pickle
from flask import Flask, render_template

app = Flask(__name__)


## Import prediction models
#iris_model = pickle.load(open('models/modelo.pkl', 'rb'))


## App routes ##
@app.route('/')
def index():
    """Index route. Load index page."""
    return render_template('index.html')

@app.route('/predict/iris/')
def predict():
    """Returns the predictions based on the input data."""
    return render_template()

## App config ##
app.debug = True


## App start ##
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)