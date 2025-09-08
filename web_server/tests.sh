#!/bin/sh

# WGET
wget localhost:8000/predict
echo "Result of the request:"
cat predict
rm predict
