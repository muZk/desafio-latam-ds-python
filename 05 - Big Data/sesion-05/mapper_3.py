#!/usr/bin/python3.6

import re, sys

feed_document = sys.stdin

for line_in_document in feed_document:
  line = line_in_document.strip()
  if len(line) > 0:
    (user_id, movie_id, rating, timestamp) = line.split(',')
    print(f"{movie_id}\t{rating}")
