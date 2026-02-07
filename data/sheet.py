import gspread
import streamlit as st
from google.oauth2.service_account import Credentials

def get_worksheet(worksheet='Wheel of Life'):
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = Credentials.from_service_account_info(
        st.secrets['gcp_service_account'],
        scopes=scopes
    )
    client = gspread.authorize(creds)
    return client.open("RE:ACT").worksheet(worksheet)