

env setup for dev 

python -m venv .venv

.venv\Scripts\Activate.ps1

pip install -r requirements.txt

aplication run 

uvicorn app.main:app --reload