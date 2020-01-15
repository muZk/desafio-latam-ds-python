#!/usr/bin/python3.6

import sys

feed_mapper_output = sys.stdin
total_count = 0
total_sum = 0
previous_movie_id = None

for line_ocurrence in feed_mapper_output:
  movie_id, rating = line_ocurrence.split('\t')
  rating = float(rating)

  if movie_id != previous_movie_id:
    if previous_movie_id is not None and total_count > 0:
      average = current_sum / total_count
      print(f"{previous_movie_id}\t{total_count}\t{average}")
    
    previous_movie_id = movie_id
    total_count = 0
    current_sum = 0

  total_count += 1
  current_sum += rating

if total_count > 0:
  average = current_sum / total_count
  print(f"{previous_movie_id}\t{average}")
