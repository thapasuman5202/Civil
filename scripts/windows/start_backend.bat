@echo off
call .venv\Scripts\activate
uvicorn app.main:app --app-dir apps\backend --reload
