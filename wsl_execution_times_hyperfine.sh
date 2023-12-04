#!/usr/bin/env bash

for file in *.py; do
  file_mod=$(echo "$file" | cut -d. -f1);
  echo "$file";
  echo "part_one():"; sleep 3;
  hyperfine --warmup 10 "python3 -c 'from $file_mod import *; the_input = the_setup(); print(part_one(the_input))'";
  echo "part_two()"; sleep 3;
  hyperfine --warmup 10 "python3 -c 'from $file_mod import *; the_input = the_setup(); print(part_two(the_input))'";
done
