# coding=utf-8

import sys,re

# vamos a leer los datos que provengan del standard input del sistema
feed_document = sys.stdin

# para cada una de las líneas en los datos

for line_in_document in feed_document:
  # obtenemos la subscripcion
  subscription = line_in_document[-2]
  
  # vamos a generar un print con la siguiente nomenclatura:
  # # <subscripcion>    1
  print(subscription + '\t' + "1")