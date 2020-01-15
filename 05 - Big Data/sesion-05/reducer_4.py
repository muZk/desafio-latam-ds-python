#!/usr/bin/python3.6

import sys

filters = [2, 3, 4, 5, 6, 7, 8, 9, 10]

feed_mapper_output = sys.stdin
total_count = 0
previous_genre_count = None

for line_ocurrence in feed_mapper_output:
  genre_count, movie_id = line_ocurrence.split('\t')
  genre_count = int(genre_count)

  if genre_count != previous_genre_count:
    if previous_genre_count is not None:
      if previous_genre_count in filters:
        print(str(previous_genre_count) + "\t" + str(total_count))
    
    previous_genre_count = genre_count
    total_count = 0

  total_count += 1

if previous_genre_count in filters:
  print(str(previous_genre_count) + "\t" + str(total_count))
