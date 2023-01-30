import streamlit as st
from app_pages.multiple_pages import MultiPage
from app_pages.correlation_study import correlation_study_body
from app_pages.feature_engineering_study import feature_engineering_study_body

app = MultiPage("Housing Price Report")

app.add_page("Correlation study", correlation_study_body)
app.add_page("Feature engineering study", feature_engineering_study_body)

app.run()