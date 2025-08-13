@echo off
python -m venv .venv
call .venv\Scripts\activate
pip install -e apps\backend
pnpm install
cd apps\backend
alembic upgrade head
cd ..\..
python apps\backend\app\seed.py
