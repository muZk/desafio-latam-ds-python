#!/usr/bin/python3.6

import re, sys, csv

feed_document = sys.stdin

for line_in_document in feed_document:
  line = list(csv.reader(line_in_document.strip()))
  if len(line) > 0:
    (movie_id, title, genres) = line
    genres_count = genres.split('|')
    if genres != '(no genres listed)':
      genres_count = 1

    # ya que en el reducer contaremos por genero
    print(f"{genres_count}\t{movie_id}")
