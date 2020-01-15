#!/bin/bash

cd richardson_clarissa

for filename in *.txt; do
  cat $filename | python ../mapper.py | sort -k1,1 | python ../reducer.py > "../wordcounts/word_count_$filename"
done
