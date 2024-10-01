# streamlit_frontend.py
# Author: Rishav Bhattacharjee
# Date: 9th September, 2024
# Streamlit frontend for interacting with the FastAPI model prediction API.
#https://c4.wallpaperflare.com/wallpaper/681/554/339/abstract-planet-space-purple-wallpaper-preview.jpg

import streamlit as st
import requests
import pandas as pd
from io import StringIO

# Set the FastAPI backend URL
API_URL = "https://dark-matter-halo-concentration.onrender.com/"  # Update this if running on a different host/port

# Add custom CSS for the gray background in the description container
st.markdown("""
    <style>
    .description-container {
        background-color: #333333;  /* Dark gray shade */
        color: white;               /* White text for contrast */
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Add custom CSS to set a galaxy background image (you can replace the URL with your own image)
page_bg_img = '''
<style>
.stApp {
    background-image: url("https://c4.wallpaperflare.com/wallpaper/681/554/339/abstract-planet-space-purple-wallpaper-preview.jpg");
    background-size: cover;
    background-position: center;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# Title of the app
st.title("Dark Matter Halo Concentration Prediction")

#st.write("""
#This app allows you to predict dark matter halo concentrations using advanced machine learning models. 
#Simply upload a CSV file containing the relevant data, and the model will process it to generate predictions. 
#You can also download a sample dataset to try it out.
#""")

# Description container for better readability with gray background
with st.container():
    st.markdown("""
        <div class="description-container">
        <h2>Dark Matter Halo</h2>
        <p>
            A <strong>Dark Matter Halo</strong> is an invisible, gravitationally dominant region surrounding galaxies and galaxy clusters. 
            It contains dark matter, a substance that doesn't emit or interact with electromagnetic radiation, making it undetectable through conventional observational means. 
            Despite its elusiveness, dark matter plays a crucial role in the formation, structure, and evolution of galaxies by influencing their rotation and the movement of visible matter.
        </p>
        <h2>About the App</h2>
        <p>
            This app is designed to undertake <strong>regression analysis</strong> on dark matter halos using data from the 
            <a href="https://www.slac.stanford.edu/~behroozi/Bolshoi_Catalogs/" target="_blank" style="color: lightblue;">Bolshoi Simulation Catalogue</a>, 
            one of the most detailed cosmological simulations of dark matter structures. By uploading a CSV file with the appropriate features, users can:
        </p>

        <ul>
            <li>Predict <strong>dark matter halo concentration</strong>.</li>
            <li>Leverage advanced machine learning models for more accurate predictions.</li>
            <li>Visualize predictions against actual values, allowing researchers to evaluate the model's performance.</li>
        </ul>
        <p>
            This tool is especially beneficial for early-career researchers examining large-scale datasets from the Bolshoi Simulation Catalogue,
            facilitating a more efficient analysis of dark matter halo properties and enhancing their understanding of this crucial aspect of cosmology.
        </p>
        </div>
    """, unsafe_allow_html=True)

#st.markdown("[Download Sample Data](https://raw.githubusercontent.com/Rishavdovakiin/DM-Regression/refs/heads/main/hlist_0.13835.csv)", unsafe_allow_html=True)


# Provide a button to download the sample data directly from GitHub
sample_data_url = "https://raw.githubusercontent.com/Rishavdovakiin/DM-Regression/refs/heads/main/hlist_0.13835.csv"

try:
    response = requests.get(sample_data_url)
    response.raise_for_status()  # Check if the request was successful
    sample_data = response.content  # Get the content of the file

    # Provide a download button for the sample data
    st.download_button(
        label="Download Sample Data",
        data=sample_data,
        file_name="sample_data.csv",
        mime="text/csv"
    )
except requests.exceptions.RequestException as e:
    st.error(f"Failed to download sample data: {e}")

st.write("Upload your CSV file to make predictions and visualize results.")

# File uploader for CSV files
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# Display a preview of the uploaded CSV file
if uploaded_file is not None:
    st.write("Preview of the uploaded file:")
    file_contents = uploaded_file.getvalue().decode("utf-8")
    test_data = pd.read_csv(StringIO(file_contents))
    st.write(test_data)

    # Trigger the prediction when the "Predict" button is clicked
    if st.button("Predict"):
        with st.spinner("Making predictions..."):
            try:
                # Step 1: Send the CSV file to FastAPI backend for predictions
                files = {"file": uploaded_file.getvalue()}
                response = requests.post(f"{API_URL}/predict/", files=files)

                # Step 2: Handle the response from FastAPI
                if response.status_code == 200:
                    result = response.json()
                    st.success("Prediction completed successfully!")

                    # Step 3: Display RMSE score if available
                    if "RMSE_Score" in result:
                        st.write(f"RMSE Score: {result['RMSE_Score']}")

                    # Step 4: Display download button for CSV output
                    csv_output_path = result.get("csv_output")
                    if csv_output_path:
                        st.write("Download the predicted results:")
                        csv_download_link = f"{API_URL}/download_csv"
                        st.download_button(
                            label="Download CSV",
                            data=requests.get(csv_download_link).content,
                            file_name="predictions_output.csv",
                            mime="text/csv"
                        )

                    # Step 5: Display predictions vs labels plot if available
                    plot_output_url = f"{API_URL}/download_plot"
                    try:
                        image_data = requests.get(plot_output_url).content
                        st.image(image_data, caption="Predictions vs Labels", use_column_width=True)
                    except Exception as e:
                        st.error(f"Error while fetching plot: {e}")
                else:
                    # Step 6: Handle errors returned by the backend
                    st.error(f"Error from backend: {response.json()['detail']}")

            except Exception as e:
                st.error(f"Error while making predictions: {e}")
