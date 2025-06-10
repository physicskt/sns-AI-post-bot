import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import config

def get_spreadsheet(spreadsheet_url):
    scope = config.GOOGLE_SHEETS_SCOPE
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON"), scope)
    client = gspread.authorize(creds)
    # スプレッドシートを開く

    spreadsheet = client.open_by_url(spreadsheet_url) 
    return spreadsheet


def get_sheet(sheet_name=config.DEFAULT_POST_SHEET_NAME):
    spreadsheet = get_spreadsheet(os.getenv("SPREADSHEET_URL")) 
    sheet = spreadsheet.worksheet(sheet_name)
    return sheet


def fetch_pending_posts():
    sheet = get_sheet()
    rows = sheet.get_all_records()
    pending_posts = []

    for i, row in enumerate(rows):
        if row['status'] == config.POST_STATUS_PENDING:
            row_index = i + 2  # シートの行番号（1行目はヘッダーなので+2）
            pending_posts.append((row_index, row))

    return pending_posts


def update_post_status(row_index, text, status, notified=True, tweet_url=config.DEFAULT_URL_MESSAGE):
    sheet = get_sheet()
    from datetime import datetime
    now = datetime.now().strftime(config.DATETIME_FORMAT_SHORT)

    headers = sheet.row_values(1)  # 1行目のヘッダーを取得

    def col_index(header_name):
        return headers.index(header_name) + 1  # A列=1

    sheet.update_cell(row_index, col_index("text"), text)
    sheet.update_cell(row_index, col_index("postURL"), tweet_url)
    sheet.update_cell(row_index, col_index("status"), status)
    sheet.update_cell(row_index, col_index("完了日時"), now if status==config.POST_STATUS_COMPLETED else "")
    sheet.update_cell(row_index, col_index("通知済み"), "Yes" if notified else "No")


def get_prompt_instructions():
    """
    promptへの指示シートからSNS別の指示を取得する
    返り値: SNSをキー、指示を値とする辞書
    """
    try:
        sheet = get_sheet(config.DEFAULT_PROMPT_INSTRUCTIONS_SHEET_NAME)
        rows = sheet.get_all_records()
        instructions = {}
        for row in rows:
            sns = row.get('SNS', '').strip()
            instruction = row.get('指示', '').strip()
            if sns and instruction:
                instructions[sns] = instruction
        return instructions
    except Exception as e:
        # シートが存在しない場合や読み取りエラーの場合は空の辞書を返す
        return {}
