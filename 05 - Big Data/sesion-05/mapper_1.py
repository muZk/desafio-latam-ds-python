#!/usr/bin/python3.6

import re, sys

feed_document = sys.stdin

for line_in_document in feed_document:
  line = line_in_document.strip()
  if len(line) > 0:
    (movie_id, tag_id, relevance) = line.split(',')
    print(f"{tag_id}\t{relevance}")
