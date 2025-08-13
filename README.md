# Civil Stage Zero

## Quick start

### Windows (no Docker)
1. `scripts\windows\setup.bat`
2. `scripts\windows\start_all.bat`

### Docker dev
1. `docker-compose -f docker-compose.dev.yml up --build`

### Docker prod
1. `docker-compose -f docker-compose.prod.yml up --build -d`

## Troubleshooting on Windows
- Ensure virtual environment path: `.venv\\Scripts\\activate`.
- Enable long paths: `REG ADD HKLM\\SYSTEM\\CurrentControlSet\\Control\\FileSystem /v LongPathsEnabled /t REG_DWORD /d 1 /f`
- Use `SETX` to persist env vars.
- Run terminals as Administrator if permission errors occur.

## Common tasks
- Run migrations: `alembic upgrade head`
- Seed data: `python apps\\backend\\app\\seed.py` or `scripts\\windows\\seed.bat`
- Regenerate OpenAPI client: `scripts/windows/gen_client.bat` or `scripts/unix/gen_client.sh`

## Adding a new panel and endpoint
1. Create SQLAlchemy model in `apps/backend/app/models`.
2. Add Pydantic schema in `apps/backend/app/schemas`.
3. Implement router under `apps/backend/app/api/v1/routers`.
4. Expose route via `api_router` in `apps/backend/app/api/v1/__init__.py`.
5. Create frontend route under `apps/frontend/src/app`.
