from flask import Flask, jsonify, render_template
from decouple import config

from routes import product_category, iris


app = Flask(__name__)
app.secret_key = config('SECRET_KEY')


## App routes ##
@app.route('/')
def index():
    """Index route. Load index page."""
    return render_template('index.html')


## Register app routes ##
app.register_blueprint(iris.iris_bp, url_prefix='/predict/')
app.register_blueprint(product_category.product_category_bp, url_prefix='/predict/')


## App start ##
if __name__ == '__main__':
    app.run(
        debug=config('FLASK_DEBUG'), 
        host='0.0.0.0', 
        port=config('FLASK_RUN_PORT')
    )

