#!/bin/bash

export PYTHONPATH=$PWD

python -m a1 dev &
A1=$!
echo "wav-test-agent PID: $A1"

python -m a2 dev &
A2=$!
echo "tested-agent PID: $A2"

python -m dispatch


wait $A1
