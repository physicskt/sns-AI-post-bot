import logging
import config

# ログ設定（ファイルとコンソールの両方に出力）
log_file = config.LOG_FILE_NAME
logging.basicConfig(
    level=getattr(logging, config.LOG_LEVEL), 
    format=config.LOG_FORMAT,
    handlers=[
        logging.FileHandler(log_file, mode="a", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

def log_message(message: str):
    """メッセージをログファイルに記録し、同時に出力する"""
    logging.info("")
    logging.info("########################################")
    logging.info(f"# {message}")
    logging.info("########################################")

def log_less_message(message: str):
    """メッセージをログファイルに記録し、同時に出力する"""
    logging.info(f"{message}")