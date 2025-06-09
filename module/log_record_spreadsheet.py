import gspread
from datetime import datetime
import pytz
from oauth2client.service_account import ServiceAccountCredentials


def log_record_spreadsheet(argument, SPREADSHEET_URL, GCP_JSON_KEY, max_rows_count=2000):
    """
    引数を、'実行記録' シートのA列に記録する
    - シートがなければ作成
    - 最大 max_rows_count まで記録し、超えた場合は先頭100行を削除
    """
    recordSheetName = "実行記録"
    # Google Sheets API のスコープ設定
    scope = ["https://spreadsheets.google.com/feeds", 
             "https://www.googleapis.com/auth/spreadsheets", 
             "https://www.googleapis.com/auth/drive"]
    
    # 認証情報の読み込み
    creds = ServiceAccountCredentials.from_json_keyfile_name(GCP_JSON_KEY, scope)
    client = gspread.authorize(creds)

    # スプレッドシートを開く
    spreadsheet = client.open_by_url(SPREADSHEET_URL)
    
    # "実行記録" シートを取得または作成
    try:
        sheet = spreadsheet.worksheet(recordSheetName)
    except gspread.exceptions.WorksheetNotFound:
        sheet = spreadsheet.add_worksheet(title=recordSheetName, rows=str(max_rows_count), cols="2")

    # 現在のシートの列数を取得
    current_cols = len(sheet.row_values(1))  # 1行目の列数を取得

    # 2列未満の場合、2列に拡張
    if current_cols < 2:
        sheet.resize(rows=max_rows_count, cols=2)

    # 現在のデータを取得
    data = sheet.col_values(1)  # A列の全データを取得
    jst = pytz.timezone('Asia/Tokyo')
    execution_time = datetime.now(jst).strftime("%Y-%m-%d %H:%M:%S")

    # データを追加
    sheet.append_row([execution_time, argument])
    
    # max_rows_count 行を超えていたら先頭100行を削除
    if len(data) >= max_rows_count:
        sheet.delete_rows(1, 100)  # 1〜100行目を削除

    # print(f"{argument}")


def log_record_spreadsheet_head(argument, SPREADSHEET_URL, GCP_JSON_KEY, max_rows_count=2000):
    """
    引数を、'実行記録' シートのA列に記録する
    - シートがなければ作成
    - 最大 max_rows_count まで記録し、超えた場合は先頭100行を削除
    """
    recordSheetName = "実行記録"
    # Google Sheets API のスコープ設定
    scope = ["https://spreadsheets.google.com/feeds", 
             "https://www.googleapis.com/auth/spreadsheets", 
             "https://www.googleapis.com/auth/drive"]
    
    # 認証情報の読み込み
    creds = ServiceAccountCredentials.from_json_keyfile_name(GCP_JSON_KEY, scope)
    client = gspread.authorize(creds)

    # スプレッドシートを開く
    spreadsheet = client.open_by_url(SPREADSHEET_URL)
    
    # "実行記録" シートを取得または作成
    try:
        sheet = spreadsheet.worksheet(recordSheetName)
    except gspread.exceptions.WorksheetNotFound:
        sheet = spreadsheet.add_worksheet(title=recordSheetName, rows=str(max_rows_count), cols="2")

    # 現在のシートの列数を取得
    current_cols = len(sheet.row_values(1))  # 1行目の列数を取得

    # 2列未満の場合、2列に拡張
    if current_cols < 2:
        sheet.resize(rows=max_rows_count, cols=2)

    # 現在のデータを取得
    data = sheet.col_values(1)  # A列の全データを取得
    jst = pytz.timezone('Asia/Tokyo')
    execution_time = datetime.now(jst).strftime("%Y-%m-%d %H:%M:%S")

    # データを追加
    sheet.insert_row([execution_time, argument], 1)

    row_count = len(sheet.col_values(1))  # 1列目のデータ数
    
    # max_rows_count 行を超えていたら 後ろ100行を削除
    if row_count > max_rows_count:
        sheet.delete_rows(max_rows_count -100, row_count)  # max_rows_count+1行目以降を削除

    # print(f"{argument}")