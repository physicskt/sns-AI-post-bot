import os
import logging
from .log_module_mine import *

def load_file(filepath):
    """
    filename から 内容を読み取りリターン
    """
    # script_dir = os.path.dirname(os.path.abspath(__file__))
    # filepath = os.path.join(script_dir, filename)

    if os.path.exists(filepath) == False:
        msg = f"error: filepath {filepath} が存在しません"
        logging.error(msg)
        raise ValueError(msg)

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read().strip()
        log_less_message(f"{filepath} の読み込みに成功しました")
        # log_less_message(content)
        return content  # 前後の改行・空白を削除

    msg = f"error: filepath {filepath} の読み込みに失敗しました"
    logging.error(msg)
    raise ValueError(msg)