#!/bin/bash

CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# create python package
source .venv/bin/activate
python3 setup.py sdist
source .venv/bin/deactivate

source ${CURRENT_DIR}/.vscode/source_spotify.sh
echo "[spotify]" > ${CURRENT_DIR}/.vscode/spotify.conf
echo "password = ${SPOTIFY_PASS}" >> ${CURRENT_DIR}/.vscode/spotify.conf
echo "username = ${SPOTIFY_USER}" >> ${CURRENT_DIR}/.vscode/spotify.conf
echo "client_id = ${SPOTIFY_CLIENT_ID}" >> ${CURRENT_DIR}/.vscode/spotify.conf
echo "client_secret = ${SPOTIFY_CLIENT_SECRET}" >> ${CURRENT_DIR}/.vscode/spotify.conf

docker build . -t playbox --rm


