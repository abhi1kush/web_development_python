#!/bin/bash
NAME="dynamic"
ROOTDIR=/flask_setup/

cd $ROOTDIR

exec python -m app.redis.dynamic_rq_worker