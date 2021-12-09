#!/usr/bin/env bash

for file in *.py; do
  file_mod=$(echo "$file" | cut -d. -f1);
  echo "$file";
 echo "part_one():";
  { time python3 -c "from $file_mod import *; the_input = the_setup(); print(part_one(the_input))"; } 2>&1 | grep real;
  echo "part_two()";
  { time python3 -c "from $file_mod import *; the_input = the_setup(); print(part_two(the_input))"; } 2>&1 | grep real;
done
