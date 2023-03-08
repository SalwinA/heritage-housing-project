import streamlit as st
import pandas as pd
import numpy as np
import joblib


@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_housing_data():
    """
    Loads House Price dataset as DataFrame
    """
    df = pd.read_csv("outputs/datasets_collection/housing_prices.csv")
    return df


@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_heritage_data():
    df_h = pd.read_csv("inputs/housing_prices_datasets/house-price-20211124T154130Z-001/house-price/inherited_houses.csv")
    return df_h



def load_pkl_file(file_path):
    """
    Loads saved ML pipeline for dashboard use
    """
    return joblib.load(filename=file_path)