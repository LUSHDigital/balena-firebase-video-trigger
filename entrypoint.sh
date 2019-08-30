#!/bin/bash

# Start the run once job.
echo "Docker container has been started"

cron
python -u src/main.py
