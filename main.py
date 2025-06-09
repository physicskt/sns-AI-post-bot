from datetime import datetime
from dotenv import load_dotenv
# module 配下全て読み込み
from module.module_loader import *

# .envファイルを強制的に読み込む
load_dotenv()
spreadsheet_url = os.getenv("SPREADSHEET_URL")
spreadsheet = get_spreadsheet(spreadsheet_url)

def main():
    settings = get_sps_data2(spreadsheet, "設定")[0]
    post_interval = settings["連続投稿間隔(s)"]

    # 未投稿を全て取得
    pending_posts = fetch_pending_posts()

    if not pending_posts:
        log_less_message("未投稿の投稿はありません。")
        return

    # 未投稿の数だけループ
    for row_index, row in pending_posts:
        log_message(f'投稿まで {post_interval} 秒待機 ....')
        time.sleep(post_interval)

        log_less_message(f"{row_index} 行目を処理中:")
        log_less_message(f"keyword: {row["keyword"]}")
        dateTime = row['date'] + " " + row['time']
        scheduled_datetime = datetime.strptime(dateTime, "%Y/%m/%d %H:%M:%S")
        now = datetime.now()

        log_less_message(f"現在時刻 {now}")
        log_less_message(f"予約時刻 {scheduled_datetime}")
        if now <= scheduled_datetime:
            log_less_message("まだ投稿時刻じゃないのでスキップ")
            continue

        # 投稿文の生成
        text = row['text'] if row['text'] else generate_post_text(row['keyword'])
        
        log_less_message(text)
        log_less_message("投稿作業を試みます")

        # SNS種別で処理を分岐（Twitterのみ）
        if row['sns'] == "X":
            tweet_url = post_to_twitter(text)
            if tweet_url is not False:
                update_post_status(row_index, text, "投稿完了", True, tweet_url)
                msg = f"✅ 投稿完了（Twitter）:\n{text}"
            else:
                msg = f"⚠️ Twitter投稿失敗:\n{text}"
        else:
            msg = f"❌ 未対応SNS:\n{row['sns']}"

        log_less_message(msg)
        notify_slack(msg)

if __name__ == "__main__":
    while True:
        try:
            settings = get_sps_data2(spreadsheet, "設定")[0]
            script_interval = settings["スクリプト実行間隔(s)"]

            main()
            log_message(f'次のスクリプト実行まで {script_interval} 秒待機 ....')
            time.sleep(script_interval)

        except Exception as e:
            log_less_message(repr(e))
            logging.error("エラーが起きました。30秒待機します。")
            time.sleep(30)
