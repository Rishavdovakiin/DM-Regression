# Dark Matter Halo Concentration Prediction App
### Overview
This Streamlit app allows users to predict dark matter halo concentrations by leveraging machine learning models. Using data from the Bolshoi Simulation Catalogue, the app enables regression analysis on dark matter halos, providing insights into one of the most fundamental aspects of cosmology.

Users can upload a CSV file containing relevant features, and the app will generate predictions, visualize the results, and provide performance metrics.

The machine learning model runs on a FastAPI backend, and this frontend interacts with it to handle user input and display outputs.



### Features
- **Predict dark matter halo concentration**: Upload a CSV file with the required features, and the app will provide predictions.
- **Advanced machine learning models**: The app uses regression models trained on data from the Bolshoi Simulation Catalogue.
- **Visualization**: Compare predictions against actual values using plots.
- **Sample data**: Download a sample dataset to test the functionality.
- **User-friendly interface**: The app features an intuitive design, with helpful descriptions and easy-to-follow steps.
### How to Use the App
- Run the App
Install Streamlit by running:
```bash
pip install streamlit
```
Save the Python file (streamlit_frontend.py) locally and run:
```arduino
streamlit run streamlit_frontend.py
```
- Use the App
Once the app is running, you can follow these steps:

#### Step 1: Download the Sample Data
- You can test the app by downloading a sample dataset of the Bolshoi Simulation Catalogue. Click the Download Sample Data button on the app to get the sample CSV file.
#### Step 2: Upload a CSV File
- Use the file uploader to upload a CSV file containing relevant features from the Bolshoi Simulation dataset or your own dataset. The app will display a preview of the uploaded file.
#### Step 3: Make Predictions
- After uploading the CSV file, click the Predict button to make predictions. The app sends the data to the backend FastAPI model for prediction.
#### Step 4: Visualize and Download Predictions
- Once the prediction is complete:
  - You can view the Root Mean Square Error (RMSE) score, which evaluates the accuracy of the model.
  - Download the predicted results in CSV format.
  - View a plot that compares the predicted values with actual values.
### Required Libraries
Make sure the following libraries are installed:

- **Streamlit**: For building the frontend of the app.
- **Requests**: For sending and receiving data from the FastAPI backend.
- **Pandas**: For handling CSV file operations.

Install them via pip:

```bash

pip install streamlit requests pandas
```
### API Integration
This Streamlit app interacts with a FastAPI backend, hosted at:

```arduino
https://dark-matter-halo-concentration.onrender.com/
```
Ensure that the FastAPI backend is running properly and replace the ```API_URL``` in the ```streamlit_frontend.py``` file if you deploy it on a different host.

### Backend API Endpoints
- **/predict/**: Accepts a CSV file and returns predictions along with RMSE score.
- **/download_csv**: Endpoint to download the CSV file containing the predicted results.
- **/download_plot**: Endpoint to fetch the prediction vs. labels plot.

### Customization
You can customize the app as follows:

- **Background Image**: The app currently uses a galaxy-themed background. You can replace the image URL in the ```page_bg_img``` variable with another image of your choice.
- **Prediction Models**: Update the FastAPI backend with your preferred machine learning models for better accuracy or different approaches to regression analysis.

### Known Issues
- If the API or the CSV file format isn't correct, the app will display an error message.
- Ensure your dataset aligns with the expected format of the backend model to avoid prediction errors.

### Contributing
Feel free to contribute to this project. If you encounter issues or have suggestions for improvements, open an issue or submit a pull request on the GitHub repository.

This ```README.md``` provides clear instructions for users to run, use, and understand the functionality of the Dark Matter Halo Concentration Prediction app. You can further modify this file based on additional features or updates to the project.