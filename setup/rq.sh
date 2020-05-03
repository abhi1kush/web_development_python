#!/bin/bash
NAME="rq"
ROOTDIR=/flask_setup/

cd $ROOTDIR

exec flask rq worker low