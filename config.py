# -*- coding: utf-8 -*-
"""
設定ファイル
ハードコーディングされた値をここに集約
"""

# ============================================
# 時間関連の設定
# ============================================
# エラー発生時の待機時間（秒）
ERROR_RETRY_INTERVAL = 30

# メール送信でエラーが発生した時の再試行待機時間（秒）
MAIL_ERROR_RETRY_INTERVAL = 10

# 日時フォーマット
DATETIME_FORMAT = "%Y/%m/%d %H:%M:%S"
DATETIME_FORMAT_SHORT = "%Y/%m/%d %H:%M"
LOG_DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

# ============================================
# AI生成関連の設定
# ============================================
# OpenAI GPTモデル
OPENAI_MODEL = "gpt-3.5-turbo"

# GPT最大トークン数
OPENAI_MAX_TOKENS = 4096

# SNS投稿文字数制限
SNS_CHARACTER_LIMIT = 140

# GPTプロンプトテンプレート
GPT_PROMPT_TEMPLATE = "以下のキーワードに基づいてSNS投稿文を生成してください（{char_limit}字以内）: {keyword}"

# ============================================
# メール関連の設定
# ============================================
# Gmailサーバー設定
GMAIL_SMTP_SERVER = "smtp.gmail.com"
GMAIL_SMTP_PORT = 465

# メール件名
MAIL_SUBJECT = "sns-AI-post-bot 実行結果"

# ============================================
# ログ関連の設定
# ============================================
# ログファイル名
LOG_FILE_NAME = "_log_output.log"

# ログフォーマット
LOG_FORMAT = "[%(asctime)s] - %(levelname)s - %(message)s"

# ログレベル（INFO, DEBUG, WARNING, ERROR）
LOG_LEVEL = "INFO"

# ============================================
# スプレッドシート関連の設定
# ============================================
# Google Sheets APIスコープ
GOOGLE_SHEETS_SCOPE = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets", 
    "https://www.googleapis.com/auth/drive"
]

# デフォルトシート名
DEFAULT_POST_SHEET_NAME = "投稿管理"
DEFAULT_LOG_SHEET_NAME = "実行記録"
DEFAULT_SETTINGS_SHEET_NAME = "設定"
DEFAULT_PROMPT_INSTRUCTIONS_SHEET_NAME = "promptへの指示"

# 投稿ステータス
POST_STATUS_PENDING = "未投稿"
POST_STATUS_COMPLETED = "投稿完了"

# デフォルトメッセージ
DEFAULT_URL_MESSAGE = "urlの入力がありませんでした。"

# ログ記録関連
LOG_SHEET_MAX_ROWS = 2000
LOG_SHEET_DELETE_ROWS_COUNT = 100

# ============================================
# Twitter関連の設定
# ============================================
# Twitter URL フォーマット
TWITTER_URL_FORMAT = "https://twitter.com/{username}/status/{tweet_id}"

# ============================================
# その他の設定
# ============================================
# タイムゾーン
TIMEZONE = 'Asia/Tokyo'