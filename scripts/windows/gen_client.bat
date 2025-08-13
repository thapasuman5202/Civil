@echo off
curl http://localhost:8000/openapi.json -o openapi.json
pnpm --dir packages\shared run generate
