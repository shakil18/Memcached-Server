#!/bin/bash
cd /a2p05/
export PYTHONPATH=$PYTHONPATH:$/a2p05/
dude run
dude sum
Rscript graphs.R
