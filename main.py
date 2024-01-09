import gspread
from oauth2client.service_account import ServiceAccountCredentials


scopes = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive',
'https://www.googleapis.com/auth/drive.file'
]

creds = ServiceAccountCredentials.from_json_keyfile_name("C:\\Users\\TraRe\\OneDrive\\Desktop\\Volontariato - CAI\\Projects\\InteractiveMap\\secret_key.json", scopes=scopes)

file = gspread.authorize(creds)
workbook = file.open_by_url("https://docs.google.com/spreadsheets/d/1MCzzOIeIIGrxoGy3MemLS1aY0qCQdBHZ_RbYgH-f1pk/edit#gid=1685296195")
# sheet = workbook.sheet1

# print(sheet.get_all_records)