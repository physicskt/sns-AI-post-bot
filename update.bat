chcp 65001 >nul
@echo off
echo =====================================
echo    SNS AI Post Bot アップデート
echo =====================================
echo.

echo 変更を一時保存しています...
git stash
if %errorlevel% neq 0 (
    echo エラー: 変更の一時保存に失敗しました。
    pause
    exit /b 1
)

echo.
echo 最新版を取得しています...
git pull origin main
if %errorlevel% neq 0 (
    echo エラー: 最新版の取得に失敗しました。
    echo 手動でリポジトリの状態を確認してください。
    pause
    exit /b 1
)

echo.
echo 一時保存した変更を復元しています...
git stash list | findstr /r "^stash@{0}" >nul
if %errorlevel% equ 0 (
    git stash pop
    if %errorlevel% neq 0 (
        echo 警告: 変更の復元で競合が発生しました。
        echo 手動で競合を解決してください。
        echo.
        echo 競合ファイルを確認するには:
        echo   git status
        echo.
        echo 競合解決後に実行:
        echo   git add .
        echo   git commit -m "競合解決"
        pause
        exit /b 1
    )
    echo 変更が正常に復元されました。
) else (
    echo 一時保存された変更はありませんでした。
)

echo.
echo 依存関係を更新しています...
pip install -r requirements.txt --upgrade
if %errorlevel% neq 0 (
    echo 警告: 依存関係の更新で問題が発生しました。
    echo 手動で確認してください: pip install -r requirements.txt
)

echo.
echo =====================================
echo    アップデート完了！
echo =====================================
echo.
echo 変更内容を確認するには:
echo   git log --oneline -10
echo.
echo プログラムを実行するには:
echo   python main.py
echo または
echo   softEnablerwindows.bat
echo.
pause