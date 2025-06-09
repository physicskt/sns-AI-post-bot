from oauth2client.service_account import ServiceAccountCredentials
import gspread
import os
from module.load_file import *


def get_email_settings(GCP_JSON_KEY, SPREADSHEET_URL):
    """
    指定されたGoogleスプレッドシートの「設定」シートから送信・受信メールアドレスを取得する。
    アプリパスワードは環境変数GMAIL_APP_PASSWORDから取得する。
    return sender_email, receiver_email, gmail_app_password
    """
    # Google Sheets API のスコープ設定
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    # 認証情報の読み込み
    creds = ServiceAccountCredentials.from_json_keyfile_name(GCP_JSON_KEY, scope)
    client = gspread.authorize(creds)

    # スプレッドシートを開く
    spreadsheet = client.open_by_url(SPREADSHEET_URL) 
    sheet = spreadsheet.worksheet("設定")
    data = sheet.get_all_values()
    sender_email, receiver_email, gmail_app_password = "", "", ""

    # A列をスキャンして「送信メールアドレス」「受信メールアドレス」を探す
    for row in data:
        if len(row) < 2:  # B列が存在しない（A列だけの行）場合はスキップ
            continue

        key, value = row[0].strip(), row[1].strip()  # A列とB列の値を取得
        if key == "送信メールアドレス":
            sender_email = value
        elif key == "受信メールアドレス":
            receiver_email = value
        elif key == "送信メールアドレス_アプリパスワード":
            gmail_app_password = value
    
    # 環境変数からGmailアプリパスワードを取得（優先）
    env_app_password = os.getenv("GMAIL_APP_PASSWORD")
    if env_app_password:
        gmail_app_password = env_app_password

    print(f"送信メールアドレス: {sender_email}")
    print(f"受信メールアドレス: {receiver_email}")
    print()
    return sender_email, receiver_email, gmail_app_password


def get_settings_all(GCP_JSON_KEY, SPREADSHEET_URL):
    """
    指定されたGoogleスプレッドシートの「設定」シートから送信・受信メールアドレスを取得する。
    return sender_email, receiver_email
    """
    # Google Sheets API のスコープ設定
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    # 認証情報の読み込み
    creds = ServiceAccountCredentials.from_json_keyfile_name(GCP_JSON_KEY, scope)
    client = gspread.authorize(creds)

    # スプレッドシートを開く
    spreadsheet = client.open_by_url(SPREADSHEET_URL) 
    sheet = spreadsheet.worksheet("設定")
    all_setting_data = sheet.get_all_values()

    return all_setting_data


def search_and_get_setting_value(search_key_list:list, GCP_JSON_KEY, SPREADSHEET_URL):
    all_setting_data = get_settings_all(GCP_JSON_KEY, SPREADSHEET_URL)
    return_values = []
    # A列をスキャンして「送信メールアドレス」「受信メールアドレス」を探す
    for row in all_setting_data:
        if len(row) < 2:  # B列が存在しない（A列だけの行）場合はスキップ
            continue

        key, value = row[0].strip(), row[1].strip()  # A列とB列の値を取得
        for search_key in search_key_list:
            if key == search_key:
                return_values.append(value)

    return return_values