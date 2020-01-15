#!/bin/bash

cat survey_data.txt | python mapper_4_1.py | sort -k1,1 | python reducer_4_1.py > 4_1.txt
cat survey_data.txt | python mapper_4_2.py | sort -k1,1 | python reducer_4_2.py > 4_2.txt
cat survey_data.txt | python mapper_4_3.py | sort -k1,1 | python reducer_4_3.py > 4_3.txt