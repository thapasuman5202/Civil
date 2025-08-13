#!/usr/bin/env bash
python -m venv .venv
source .venv/bin/activate
pip install -e apps/backend
pnpm install
cd apps/backend
alembic upgrade head
cd ../..
python apps/backend/app/seed.py
