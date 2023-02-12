import pickle
from flask import Flask, jsonify, render_template, request
from models import load_models
from decouple import config


## Import prediction models
iris_model = pickle.load(open('models/iris_decision_tree_model.pkl', 'rb'))
product_category_model = load_models.decompress_pickle('./models/productcategory_randtree_ros.pbz2') # decompress pbz2 (compressed pickle file) to the model

app = Flask(__name__)
app.secret_key = config('SECRET_KEY')

## App routes ##
@app.route('/')
def index():
    """Index route. Load index page."""
    return render_template('index.html')


"""
    Iris Decision Tree Model Routes
"""
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


"""
    Otto Group Product Category Classification Model Routes
"""
@app.route('/predict/product_category/', methods=['GET', 'POST'])
def product_category():
    if request.method == 'GET':
        return render_template('product_category/index.html')

    if request.method == 'POST':
        # Return error if no form data provided
        if request.want_form_data_parsed != True:
            return jsonify({
                'error': 'No content inputed',
                'message': 'You need to input some valid form data. This endpoint expects 93 feat_ to predict. Expected format: feat_N:value',
            }), 400

        # Read form data provided
        data = request.form.to_dict()

        # Predict the product category
        result_class = product_category_model.predict([[
            data['feat_1'], data['feat_2'], data['feat_3'], data['feat_4'], data['feat_5'], data['feat_6'], data['feat_7'], data['feat_8'], data['feat_9'],
            data['feat_10'], data['feat_11'], data['feat_12'], data['feat_13'], data['feat_14'], data['feat_15'], data['feat_16'], data['feat_17'], data['feat_18'], data['feat_19'], 
            data['feat_20'], data['feat_21'], data['feat_22'], data['feat_23'], data['feat_24'], data['feat_25'], data['feat_26'], data['feat_27'], data['feat_28'], data['feat_29'], 
            data['feat_30'], data['feat_31'], data['feat_32'], data['feat_33'], data['feat_34'], data['feat_35'], data['feat_36'], data['feat_37'], data['feat_38'], data['feat_39'], 
            data['feat_40'], data['feat_41'], data['feat_42'], data['feat_43'], data['feat_44'], data['feat_45'], data['feat_46'], data['feat_47'], data['feat_48'], data['feat_49'], 
            data['feat_50'], data['feat_51'], data['feat_52'], data['feat_53'], data['feat_54'], data['feat_55'], data['feat_56'], data['feat_57'], data['feat_58'], data['feat_59'], 
            data['feat_60'], data['feat_61'], data['feat_62'], data['feat_63'], data['feat_64'], data['feat_65'], data['feat_66'], data['feat_67'], data['feat_68'], data['feat_69'], 
            data['feat_70'], data['feat_71'], data['feat_72'], data['feat_73'], data['feat_74'], data['feat_75'], data['feat_76'], data['feat_77'], data['feat_78'], data['feat_79'], 
            data['feat_80'], data['feat_81'], data['feat_82'], data['feat_83'], data['feat_84'], data['feat_85'], data['feat_86'], data['feat_87'], data['feat_88'], data['feat_89'], 
            data['feat_90'], data['feat_91'], data['feat_92'], data['feat_93']
        ]])

        return jsonify({
            'product_category': result_class[0],
        })


## App start ##
if __name__ == '__main__':
    app.run(
        debug=config('FLASK_DEBUG'), 
        host='0.0.0.0', 
        port=config('FLASK_RUN_PORT')
    )
