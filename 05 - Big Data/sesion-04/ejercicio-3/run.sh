#!/bin/bash

cd richardson_clarissa

for filename in *.txt; do
  cat $filename | python ../mapper.py | sort -k1,1 | python ../reducer.py > "../namecount/name_count_$filename"
done
