#!/usr/bin/env bash

set -eoux pipefail

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

docker run \
    -v ${DIR}/.data:/var/lib/postgresql/data \
    -e POSTGRES_PASSWORD=mysecretpassword \
    -p 5432:5432 \
    -it --rm  --name petshop-postgres \
    postgres:11.3-alpine
