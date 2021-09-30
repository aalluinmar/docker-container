#!/bin/bash

# wait for PSQL to server to start
sleep 2
echo "Copying Source files to the local directory ..."

echo "Executing the Python Script ..."
python /code/file_operations.py

echo "Printing the output file ..."
echo ""
cat /code/result.txt
