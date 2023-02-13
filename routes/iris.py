from flask import Blueprint, render_template, request, jsonify
import pickle


iris_bp = Blueprint(
    'iris', __name__,
    template_folder='templates'
)


"""
    Iris Decision Tree Model Routes
"""
@iris_bp.route('/iris/<float:sw>/<float:sl>/<float:pw>/<float:pl>', methods=['GET'])
def get_iris_predict(sw, sl, pw, pl):
    """
        Returns the predictions based on the input data as JSON.

        sw: <float> SepalWidth 
        sl: <float> SepalLeight
        pw: <float> PetalWidth
        pl: <float> PetalLeight
    """

    iris_model = pickle.load(open('models/iris_decision_tree_model.pkl', 'rb'))
    result = iris_model.predict([[sw, sl, pw, pl]])

    if result[0] == 0:
        result_class = 'Iris setosa'
    elif result[0] == 1:
        result_class = 'Iris versicolour'
    else:
        result_class = 'Iris virginica'

    return jsonify({'Class_name': result_class})


@iris_bp.route('/iris/form/', methods=['GET', 'POST'])
def iris_predict_form():
    """
        Implements a form page to predict iris flowers.

        GET: Returns the form page
        POST: Returns the result class using the inputed data in the form
            Body: Form-data with:
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

        iris_model = pickle.load(open('models/iris_decision_tree_model.pkl', 'rb'))
        result = iris_model.predict([[sepall, sepalw, petall, petalw]])

        if result[0] == 0:
            result_class = 'Iris setosa'
        elif result[0] == 1:
            result_class = 'Iris versicolour'
        else:
            result_class = 'Iris virginica'

        return render_template('iris/index.html', result = result_class)
