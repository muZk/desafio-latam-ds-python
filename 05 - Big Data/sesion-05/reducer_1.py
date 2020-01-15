#!/usr/bin/python3.6

import sys

feed_mapper_output = sys.stdin
total_count = 0
total_sum = 0
previous_tag_id = None

for line_ocurrence in feed_mapper_output:
  tag_id, relevance = line_ocurrence.split('\t')
  relevance = float(relevance)

  if tag_id != previous_tag_id:
    if previous_tag_id is not None and total_count > 0:
      average = current_sum / total_count
      print(f"{previous_tag_id}\t{average}")
    
    previous_tag_id = tag_id
    total_count = 0
    current_sum = 0

  total_count += 1
  current_sum += relevance

if total_count > 0:
  average = current_sum / total_count
  print(f"{previous_tag_id}\t{average}")
