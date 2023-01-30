import streamlit as st


from app_pages.multi_pages import MultiPage
from app_pages.data_correlation import data_corr_body
from app_pages.feature_engineering import feat_eng_body


# Create an instance
app = MultiPage(app_name="This is my first multi-page Streamlit App")

# Add your app pages here using .add_page()
app.add_page("Data Correlation", data_corr_body)
app.add_page("Feature Engineering", feat_eng_body)

app.run()