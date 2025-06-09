import time
import sys
import smtplib
from email.mime.text import MIMEText

from .log_record_spreadsheet import *
from .log_module_mine import *

def mail_login_checker(SENDER_EMAIL, GMAIL_APP_PASSWORD):
    ##################################################
    # ログインの可否判定

    print("ログイン可否判定中")
    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(SENDER_EMAIL, GMAIL_APP_PASSWORD)
        print("✅ メールサーバーへのログイン成功")
        server.quit()

    except smtplib.SMTPAuthenticationError:
        error_msg = "❌ 認証エラー: パスワードまたはアカウント設定を確認してください"
        print(error_msg)
        # log_message("error_log.txt", error_msg)
        print(error_msg)
        print("プログラムを終了します。")
        sys.exit(1)  # 認証エラーなら即終了

    except Exception as e:
        error_msg = f"⚠️ その他のエラー: {e}"
        print(error_msg)
        # log_message("error_log.txt", error_msg)
        print(error_msg)
        print("10秒後に再試行します...")
        time.sleep(10)  # 少し待って再試行


def mail_sender(SENDER_EMAIL, GMAIL_APP_PASSWORD, RECEIVER_EMAIL, mail_honbun):
    ##################################################
    # mail_honbun を メールで送信する
    
    msg = MIMEText(mail_honbun)
    msg["Subject"] = "賃貸自動申し込みプログラム"
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL

    print("メールを送信しています")
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SENDER_EMAIL, GMAIL_APP_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        print("✅ メールを送信しました！")
