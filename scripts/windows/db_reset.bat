@echo off
call .venv\Scripts\activate
alembic downgrade base
alembic upgrade head
python apps\backend\app\seed.py
