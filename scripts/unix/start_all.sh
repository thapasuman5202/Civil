#!/usr/bin/env bash
scripts/unix/start_backend.sh &
scripts/unix/start_frontend.sh &
wait
