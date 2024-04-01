#!/bin/bash

set -m  # Enable job control

#Silence
exec > /dev/null 2>&1

# Start the Grafana Agent
setsid ./grafana-agent-linux-arm64 -config.file agent-config.yaml &
a_pgid=$!

# Run the sensor.py script
. .venv/bin/activate
setsid python -u ./sensor.py &

trap "kill -- -$a_pgid" SIGINT SIGTERM SIGKILL

wait


