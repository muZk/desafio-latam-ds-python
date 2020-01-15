# coding=utf-8

import sys,re

# vamos a leer los datos que provengan del standard input del sistema
feed_document = sys.stdin

# para cada una de las líneas en los datos

for line_in_document in feed_document:
  # reemplazamos los valores no alfanuméricos por espacios.
  line_in_document = re.sub(r'^\W+|\W+$', '', line_in_document)
  
  # convertimos el string en una lista de strings
  words_in_line = re.split(r'\W+',line_in_document)
  
  # para cada palabra en la lista de strings
  for word in words_in_line:
    # vamos a generar un print con la siguiente nomenclatura:
    # # <palabra>    1
    print(word.lower() +'\t'+"1")
