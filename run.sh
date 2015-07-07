#!/bin/bash

gunicorn --worker-class 'socketio.sgunicorn.GeventSocketIOWorker' chat:app
