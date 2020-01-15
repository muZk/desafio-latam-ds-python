# coding=utf-8

import sys

feed_mapper_output = sys.stdin

# generamos un identificador de la palabra previa
previous_counter = None

# generamos un contador de la cantidad de palabras
total_word_count = 0

# para cada una de las líneas en el standard input del paso previo
for line_ocurrence in feed_mapper_output:
  word, ocurrence = line_ocurrence.split('\t')
  if word != previous_counter:
    if previous_counter is not None:
      print(str(total_word_count) +'\t'+previous_counter)
    previous_counter = word
    total_word_count = 0
  total_word_count += int(ocurrence)

print(previous_counter+'\t'+str(total_word_count))
