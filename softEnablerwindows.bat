pip install virtualenv
virtualenv .venv
call .venv\Scripts\activate
pip install -r requirements.txt
py main.py
pause