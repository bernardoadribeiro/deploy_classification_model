from flask import Blueprint, render_template, request, jsonify
import pickle


breast_cancer_bp = Blueprint(
    'breast_cancer', __name__,
    template_folder='templates'
)


@breast_cancer_bp.route('/breast_cancer/', methods=['GET', 'POST'])
def breast_cancer_predict():
    """
        Implements a form page to predict breast cancer.

        GET: Returns the form page
        POST: Returns the result class using the inputed data in the form
            Body: Form-data
    """

    if request.method == 'GET':
        fields = ['mean_radius', 'mean_texture', 'mean_perimeter', 'mean_area', 'mean_smoothness', 
                  'mean_compactness', 'mean_concavity', 'mean_concave_points', 'mean_symmetry', 
                  'mean_fractal_dimension', 'radius_error', 'texture_error', 'perimeter_error', 
                  'area_error', 'smoothness_error', 'compactness_error', 'concavity_error', 
                  'concave_points_error', 'symmetry_error', 'fractal_dimension_error', 'worst_radius', 
                  'worst_texture', 'worst_perimeter', 'worst_area', 'worst_smoothness', 'worst_compactness', 
                  'worst_concavity', 'worst_concave_points', 'worst_symmetry', 'worst_fractal_dimension'
        ]

        return render_template('breast_cancer/index.html', title='Predict', fields=fields)

    if request.method == 'POST':

        # Return error if no form data provided
        if request.want_form_data_parsed != True:
            return jsonify({
                'error': 'No content inputed',
                'message': 'You need to input some valid form data. This endpoint expects 30 features to predict.',
            }), 400

        data = request.form.to_dict()
        
        # convert to float
        data_float = {k: float(v) for k, v in data.items()}

        breast_cancer_mlpclassifier = pickle.load(open('models/breast_cancer_mlpclassifier.pkl', 'rb'))
        
        # extracts the values from the data_float dictionary and converts them to a list of float values 
        # that can be passed to the predict() method of the model.
        result = breast_cancer_mlpclassifier.predict([ list(data_float.values()) ])

        if result[0] == 0:
            result_class = 'Malignant'
        elif result[0] == 1:
            result_class = 'Benign'

        return jsonify({
            'breast_cancer_classification': result_class
        })
