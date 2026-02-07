import gspread
import streamlit as st
from google.oauth2.service_account import Credentials

# def get_worksheet(worksheet='Tabellenblatt1'):
#     scopes = [
#         "https://www.googleapis.com/auth/spreadsheets",
#         "https://www.googleapis.com/auth/drive"
#     ]
#     creds = Credentials.from_service_account_info(
#         st.secrets['gcp_service_account'],
#         scopes=scopes
#     )
#     client = gspread.authorize(creds)

#     return client.open("Demo RE:ACT").worksheet(worksheet)
def get_worksheet(worksheet='Tabellenblatt1'):
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = Credentials.from_service_account_info(
        st.secrets['gcp_service_account'],
        scopes=scopes
    )
    client = gspread.authorize(creds)
    spreadsheet = client.open("Demo RE:ACT")

    try:
        sheet = spreadsheet.worksheet(worksheet)
    except gspread.exceptions.WorksheetNotFound:
        # Nimm das erste Blatt, oder erstelle eins, wenn es keins gibt
        if len(spreadsheet.worksheets()) == 0:
            sheet = spreadsheet.add_worksheet(title="Tabellenblatt1", rows=100, cols=20)
            st.write("Kein Blatt vorhanden – neues Blatt 'Tabellenblatt1' erstellt.")
        else:
            sheet = spreadsheet.get_worksheet(0)
            st.write(f"'Wheel of Life' nicht gefunden. Nutze erstes Blatt '{sheet.title}'")

    return sheet
