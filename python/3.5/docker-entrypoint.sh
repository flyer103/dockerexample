#!/bin/bash
set -e

if [ "$1" = "python" ]; then
    shift
    python3 "$@"
elif [ "$1" = "pip" ]; then
    shift
    exec pip3 "$@"
fi

exec "$@"
