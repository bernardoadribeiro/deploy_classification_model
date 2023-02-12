# Interface for a classification model

**Objective:**
This project implements a interface (with form) to use trainned models to predict the classification based on inputed data by user.
We are using Python/Flask + Jinja2 + Bootsrap to provide APIs and a friendly UI.

**Technologies**
- Python + Flask + Jinja2
- HTML + Bootstrap
- Scikit-learn
- Pickle
- *Google Cloud (soon)*

And also, we will deploy this interface for classification soon...

### **Load Models**

**Dificult to upload model large file**

The GitHub limit file fize is 100MB. So to upload the model to github I created functions to compress and decompress the pickle file and make it possible.
You can find the code and instructions [**here**](models/load_models.py).