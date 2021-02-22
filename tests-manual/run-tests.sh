#!/bin/bash

# Run all scrots
FILES=*.py
for f in $FILES
do
  echo "Running $f..."
  # take action on each file. $f store current file name
  python $f
done
