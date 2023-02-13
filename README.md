# Interface for a classification model with Flask

### **Objective:**
This project implements a interface (with form) to use trainned models to predict the classification based on inputed data by user.

Click (here)[https://classification-model-webapp.uw.r.appspot.com/] to check the deployed application.

### **Technologies**
- **Python with Flask** in the backend to provide APIs.
- **HTML + Bootstrap + Jinja2** to create the pages.
- **Scikit-learn and Pickle** to load the Machine Learning models.
- **Google Cloud App Engine** to deploy and host this application.


### **Load Models**

**Dificult to upload model large file**

The GitHub limit file fize is 100MB. So to upload the model to github I created functions to compress and decompress the pickle file and make it possible.
You can find the code and instructions [**here**](models/load_models.py).