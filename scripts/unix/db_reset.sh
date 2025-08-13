#!/usr/bin/env bash
source .venv/bin/activate
alembic downgrade base
alembic upgrade head
python apps/backend/app/seed.py
