#!/usr/bin/with-contenv bashio
set -e

export RTSP_PASSWORD="$(bashio::config 'rtsp_password')"

bashio::log.info "Starting Yosee Wizard on port 7789..."
exec uvicorn main:app --host 0.0.0.0 --port 7789
