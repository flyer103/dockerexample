#!/bin/bash
set -e

if [ "$1" = "python" ]; then
    shift
    python3 "$@"
elif [ "$1" = "pip" ]; then
    shift 2
    exec pip3 install --install-option="--prefix=${PIPLOCATION}" "$@"
else
    exec "$@"
fi
