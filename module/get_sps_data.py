from oauth2client.service_account import ServiceAccountCredentials
import gspread


def get_sps_data(GCP_JSON_KEY, SPREADSHEET_URL, sheet_name) :
    """
    スプレッドシートのデータをリストで返す
    """
    # Google Sheets API のスコープ設定
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    # 認証情報の読み込み
    creds = ServiceAccountCredentials.from_json_keyfile_name(GCP_JSON_KEY, scope)
    client = gspread.authorize(creds)

    # スプレッドシートを開く
    spreadsheet = client.open_by_url(SPREADSHEET_URL) 
    sheet = spreadsheet.worksheet(sheet_name)
    data = sheet.get_all_records()
    
    return data


def get_sps_data2(spreadsheet, sheet_name):
    """
    スプレッドシートのデータをリストで返す
    spreadsheet には事前に取得した spreadsheet を指定する
    """
    sheet = spreadsheet.worksheet(sheet_name)
    data = sheet.get_all_records()
    
    return data