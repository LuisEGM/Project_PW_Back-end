#!/bin/bash
while !</dev/tcp/db/5432; do sleep 1; done;

# Run migrations
alembic upgrade head

#Start app
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload