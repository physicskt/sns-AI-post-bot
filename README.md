# SNS AI投稿ボット

SNSへの自動投稿を行うPythonアプリケーションです。Googleスプレッドシートで投稿内容を管理し、AIを使用してテキストを生成できます。

## 機能

- 🤖 **AI投稿文生成**: OpenAI GPTを使用してキーワードから投稿文を自動生成
- 📊 **スプレッドシート連携**: Googleスプレッドシートで投稿スケジュールと内容を管理
- 🐦 **Twitter投稿**: X(Twitter)への自動投稿機能
- 📧 **通知機能**: Slackへの投稿結果通知
- ⏰ **スケジュール機能**: 指定日時での自動投稿
- 📝 **ログ記録**: 詳細な実行ログをファイルとスプレッドシートに記録

## 必要な環境

- Python 3.8以上
- Googleアカウント（スプレッドシート・サービスアカウント用）
- OpenAI APIキー
- Twitter Developer アカウント
- Slack Webhook URL（通知機能を使用する場合）

## セットアップ手順

### 1. リポジトリのクローン
```bash
git clone https://github.com/physicskt/sns-AI-post-bot.git
cd sns-AI-post-bot
```

### 2. 仮想環境の作成と有効化
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

### 3. 依存関係のインストール
```bash
pip install -r requirements.txt
```

### 4. 環境変数の設定
`.env.example.txt`を参考に、`.env`ファイルを作成してください：

```env
GOOGLE_SERVICE_ACCOUNT_JSON=credentials.json
SPREADSHEET_URL=あなたのスプレッドシートURL
OPENAI_API_KEY=あなたのOpenAI APIキー
TWITTER_CONSUMER_KEY=あなたのTwitter Consumer Key
TWITTER_CONSUMER_SECRET=あなたのTwitter Consumer Secret
TWITTER_ACCESS_TOKEN=あなたのTwitter Access Token
TWITTER_ACCESS_TOKEN_SECRET=あなたのTwitter Access Token Secret
SLACK_WEBHOOK_URL=あなたのSlack Webhook URL
GMAIL_APP_PASSWORD=あなたのGmailアプリパスワード
```

### 5. Google サービスアカウントの設定
1. [Google Cloud Console](https://console.cloud.google.com/)でプロジェクトを作成
2. Google Sheets API と Google Drive API を有効化
3. サービスアカウントを作成し、JSONキーをダウンロード
4. ダウンロードしたJSONファイルを`credentials.json`として保存
5. サービスアカウントのメールアドレスに、使用するスプレッドシートの編集権限を付与

### 6. Googleスプレッドシートの準備
以下のシートを作成してください：

#### 「投稿管理」シート
| 列名 | 説明 |
|------|------|
| date | 投稿日 (YYYY/MM/DD) |
| time | 投稿時刻 (HH:MM:SS) |
| keyword | AIが投稿文生成に使用するキーワード |
| text | 直接投稿したいテキスト（空白の場合はAIが生成） |
| sns | 投稿先SNS（現在は"X"のみ対応） |
| status | 投稿状況（未投稿/投稿完了） |
| postURL | 投稿URL（自動入力） |
| 完了日時 | 投稿完了日時（自動入力） |
| 通知済み | 通知済みフラグ（自動入力） |

#### 「設定」シート
| 設定項目 | 値 |
|----------|-----|
| 連続投稿間隔(s) | 投稿間の待機時間（秒） |
| スクリプト実行間隔(s) | スクリプトのループ間隔（秒） |

#### 「promptへの指示」シート（オプション）
| 列名 | 説明 |
|------|------|
| SNS | 投稿先SNS（X、Instagram、Facebook など） |
| 指示 | AIへの追加指示（例：「フレンドリーな感じで」、「30代向けに」） |

この表に記載された指示は、各SNSでの投稿文生成時にAIプロンプトに自動的に追加されます。シートが存在しない場合や該当するSNSの指示が設定されていない場合は、通常のプロンプトが使用されます。

## 使用方法

### 基本的な使用方法
1. スプレッドシートの「投稿管理」シートに投稿データを入力
2. アプリケーションを実行
```bash
python main.py
```

### Windows用簡単起動
Windowsユーザー向けに簡単セットアップ用のバッチファイルを用意しています：
```bash
softEnablerwindows.bat
```

## 設定のカスタマイズ

`config.py`ファイルで各種設定をカスタマイズできます：

```python
# AI関連設定
OPENAI_MODEL = "gpt-3.5-turbo"  # 使用するGPTモデル
SNS_CHARACTER_LIMIT = 140       # 投稿文字数制限

# ログ設定
LOG_LEVEL = "INFO"              # ログレベル
LOG_FILE_NAME = "_log_output.log"  # ログファイル名

# その他タイミング設定
ERROR_RETRY_INTERVAL = 30       # エラー時の再試行間隔
```

## トラブルシューティング

### よくある問題

**1. 認証エラー**
- `.env`ファイルの設定を確認
- サービスアカウントのJSONファイルのパスが正しいか確認
- スプレッドシートの共有設定を確認

**2. OpenAI APIエラー**
- APIキーが有効か確認
- API使用量の上限を確認

**3. Twitter投稿エラー**
- Twitter API認証情報を確認
- API利用制限に達していないか確認

### ログの確認
実行ログは以下の場所で確認できます：
- ファイル: `_log_output.log`
- スプレッドシート: 「実行記録」シート（自動作成）

## ファイル構成

```
sns-AI-post-bot/
├── main.py                    # メインプログラム
├── config.py                  # 設定ファイル
├── requirements.txt           # 依存関係
├── .env.example.txt          # 環境変数テンプレート
├── softEnablerwindows.bat    # Windows簡単セットアップ
├── update.bat                # アップデート用バッチファイル
└── module/                   # モジュールディレクトリ
    ├── generate.py           # AI投稿文生成
    ├── post.py              # SNS投稿
    ├── sheet.py             # スプレッドシート操作
    ├── notify.py            # 通知機能
    └── ...                  # その他のモジュール
```

## 更新方法

プロジェクトを最新版に更新するには：

### 手動更新
```bash
git stash  # 変更を一時保存
git pull   # 最新版を取得
git stash pop  # 変更を復元（競合時は手動解決）
```

### Windows用自動更新
```bash
update.bat
```

## ライセンス

このプロジェクトは[MITライセンス](LICENSE)の下で公開されています。

## 貢献

プルリクエストやイシューの報告を歓迎します。

## サポート

問題や質問がある場合は、[GitHub Issues](https://github.com/physicskt/sns-AI-post-bot/issues)でお知らせください。