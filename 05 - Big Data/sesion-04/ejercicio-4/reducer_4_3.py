# coding=utf-8

import sys

feed_mapper_output = sys.stdin

# generamos un identificador de la palabra previa
previous_counter = None

# generamos un contador de la cantidad de palabras
total_word_count = 0
total_words = 0

# para cada una de las líneas en el standard input del paso previo
for line_ocurrence in feed_mapper_output:
  word, ocurrence = line_ocurrence.split('\t')
  ocurrence = int(ocurrence)
  if word != previous_counter:
    if previous_counter is not None and total_word_count > 0:
      average = total_word_count / total_words
      print(previous_counter + '\t' + str(round(average)))
    previous_counter = word
    total_word_count = 0
    total_words = 0
  # solo contamos si la cantidad de positivos es mayor al 60%
  if ocurrence > 0.6 * 50:
    total_word_count += ocurrence
    total_words += 1

if total_word_count > 0:
  average = total_word_count / total_words
  print(previous_counter + '\t' + str(round(average)))
