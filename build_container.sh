#!/bin/bash

CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

source ${CURRENT_DIR}/.vscode/source_spotify.sh

docker build . -t playbox --rm --build-arg SPOTIFY_USER=${SPOTIFY_USER} \
--build-arg SPOTIFY_PASS=${SPOTIFY_PASS} \
--build-arg SPOTIFY_CLIENT_ID=${SPOTIFY_CLIENT_ID} \
--build-arg SPOTIFY_CLIENT_SECRET=${SPOTIFY_CLIENT_SECRET}
