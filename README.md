## Dark Matter Halo Prediction Using Machine Learning Models
This repository contains the results and code from my research internship, focused on predicting dark matter halo concentration using various advanced Machine Learning (ML) models, including Linear Regression, Forest, XGBoost, and CatBoost. The models were trained and evaluated on the Bolshoi simulation dataset, a large cosmological simulation widely used in astrophysical research. This project aims to compare the performance of different ML techniques in predicting dark matter halo properties and make these trained models easily accessible for future research.

Additionally, I have built a web-based app using **Streamlit** (frontend) and **FastAPI** (backend) to allow users to easily upload their datasets and generate predictions for dark matter halo concentration using the trained ML models. This app makes the process user-friendly and provides tools to visualize model performance, download results, and convert raw simulation data into CSV format.

You can access the Web-App here [Dark Matter Halo Concentration Prediction](https://dark-matter-concentration-prediction.streamlit.app/).

## Key Features:
- **Model Implementation**: Code for training multiple ML models (AdaBoost, XGBoost, CatBoost) for predicting dark matter halo concentration.
- **Performance Comparison**: Comprehensive comparison of model performances using evaluation metrics such as cross-validation scores and feature importance analysis.

- **Preprocessing Pipeline**: Custom preprocessing steps for feature scaling based on their statistical characteristics, ensuring optimal performance.

- **API Integration**: The API.py script allows seamless access to the trained models, enabling researchers to input their data and obtain predictions.

- **Interactive Streamlit App**: The streamlit.py script provides an interactive web application using Streamlit, allowing users to test the models and visualize predictions without extensive coding knowledge.

- **Test Suite**: The test.py file contains unit tests to validate the accuracy and robustness of the ML pipeline, ensuring that it works as expected with new data.

## Contents:
- **Bolshoi Simulation Data**: Utilizes the dark matter halo properties from the Bolshoi simulation for training and evaluation.

- **Model Training**: Implementation of multiple boosting algorithms with hyperparameter tuning.

- **Model Comparison**: Performance metrics and results, helping to identify the most effective approach for halo concentration prediction.

- **API Usage**: Simple instructions to use the pre-trained models via the API for your own dark matter simulation datasets.

- **Streamlit Web App**: A user-friendly interface for accessing the model predictions and visualizing results in real-time.
  
## Tech Stack

- **Frontend**: 
  - Streamlit for user interface.
  - Custom CSS and background for an improved user experience.
  
- **Backend**: 
  - FastAPI to handle model predictions and data processing.
  
- **Machine Learning Models**:
  - XGBoost, CatBoost, AdaBoost, etc.

- **Data**: 
  - Cosmological datasets from the [Bolshoi Simulation Catalogue](https://www.slac.stanford.edu/~behroozi/Bolshoi_Catalogs/).

## Setup
### Backend Setup (FastAPI)

1. Clone the repository:
   ```bash
   git clone https://github.com/Rishavdovakiin/DM-Regression.git
   cd DM-Regression
   ```
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the FastAPI backend:
   ```bash
   uvicorn api:app --reload
   ```
   The backend should now be running on `http://127.0.0.1:8000`.

### Frontend Setup (Streamlit)
1. Navigate to the project folder:
   ```bash
   cd DM-Regression
   ```
2. Install Streamlit if you haven’t already:
   ```bash
   pip install streamlit
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run streamlit_frontend.py
   ```
   The app will open in your web browser.

## Convert Raw Data to CSV
To convert raw data from the Bolshoi Simulation Catalogue into a well-structured CSV format, use the `Convert_to_CSV.py` script. This will preprocess the raw data and save it into CSV format with appropriate columns.
```bash
python Convert_to_CSV.py
```

## Future Work:
Researchers working with the Bolshoi simulation or similar dark matter halo datasets can use this repository to:

- Train new models on additional or updated simulation data.
- Apply the trained models to make predictions for their research.
- Use the Streamlit app for quick testing of different halo property datasets.

## Acknowledgements
- **Original Work**: Our work is inspired from the repository: ```https://github.com/abhmalik/halo_conc-regression-ML/tree/master ```
                    We applied different models and aimed to create an app for future use.
- **Bolshoi Simulation Catalogue**: The cosmological data used in this project is sourced from the Bolshoi Simulation Catalogue.
                                  The link to the catalogue: 
                                  ```
                                  https://www.slac.stanford.edu/~behroozi/Bolshoi_Catalogs/
                                  ```
- **Streamlit**: For building the app frontend.
- **FastAPI**: For the backend API used to handle model predictions.

## Getting Started:
To get started with using the models, the API, or the Streamlit app, refer to the respective documentation in the repository for detailed instructions.
