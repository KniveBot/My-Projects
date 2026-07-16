import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google
gscope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
gcredentials = 'creds.json'
gdocument = 'Denta Bot List'

name = 'N P'
phone = '+7 777'
dName = 'Ann'
usluga = 'Zuby'
date = '01.01.11 11.11'

# Запись в Google Sheet
def add_to_gsheet(name, phone, dname, usluga, date):
    credentials = ServiceAccountCredentials.from_json_keyfile_name(gcredentials, gscope)
    gc = gspread.authorize(credentials)
    wks = gc.open(gdocument).sheet1
    wks.append_row(
        [name, phone, dname, usluga, date])

add_to_gsheet(name, phone, dName, usluga, date)