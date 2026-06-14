#!/bin/bash

COMMAND=$1

case "$COMMAND" in #https://www.opennet.ru/docs/RUS/bash_scripting_guide/x5210.html
  build_generator)
    docker build -t csv-generator .
    ;;

  run_generator)
    docker run --rm -v "$(pwd)/data:/data" csv-generator #https://docs.docker.com/engine/storage/bind-mounts
    ;;

  create_local_data)
    python3 generate.py local_data
    ;;

  build_reporter)
    docker build -f Dockerfile.reporter -t csv-reporter .
    ;;

  run_reporter)
    docker run --rm -v "$(pwd)/data:/data" csv-reporter #https://docs.docker.com/engine/storage/bind-mounts
    ;;

  structure)
    find . | sort
    ;;

  clear_data)
    mkdir -p data
    rm -f data/*.csv
    rm -f data/*.html
    ;;

  inside_generator)
    docker run --rm -v "$(pwd)/data:/data" --entrypoint sh csv-generator -c "ls -la /data" 
    #https://docs.docker.com/engine/storage/bind-mounts
    #https://docs.docker.com/engine/containers/run
    #https://pubs.opengroup.org/onlinepubs/9799919799/utilities/sh.html
    ;;

  inside_reporter)
    docker run --rm -v "$(pwd)/data:/data" --entrypoint sh csv-reporter -c "ls -la /data"
    #https://docs.docker.com/engine/storage/bind-mounts
    #https://docs.docker.com/engine/containers/run
    #https://pubs.opengroup.org/onlinepubs/9799919799/utilities/sh.html
    ;;

  report_server)
    docker compose up report_server

esac