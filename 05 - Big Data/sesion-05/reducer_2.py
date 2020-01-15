#!/usr/bin/python3.6

import sys

feed_mapper_output = sys.stdin
total_count = 0
total_sum = 0
previous_user_id = None

for line_ocurrence in feed_mapper_output:
  user_id, rating = line_ocurrence.split('\t')
  rating = float(rating)

  if user_id != previous_user_id:
    if previous_user_id is not None and total_count > 0:
      average = current_sum / total_count
      print(f"{previous_user_id}\t{total_count}\t{average}")
    
    previous_user_id = user_id
    total_count = 0
    current_sum = 0

  total_count += 1
  current_sum += rating

if total_count > 0:
  average = current_sum / total_count
  print(f"{previous_user_id}\t{average}")
