#!/bin/sh

# WGET
wget localhost:8000/predict
echo "Result of the wget request:"
cat predict
rm predict

echo -e "\n\nRunning python requests lib tests..."
python reqs.py
echo -e "\nAll tests passed!"
