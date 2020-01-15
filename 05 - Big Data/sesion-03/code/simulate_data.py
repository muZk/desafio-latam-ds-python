import sys
import random
import csv
import numpy as np

if len(sys.argv) >= 4:

  amount = int(sys.argv[1])
  filename = sys.argv[2]
  seed = int(sys.argv[3])

  print(f'Simulating data...\n  rows: {amount}\n  seed: {seed}\n  output file: {filename}')

  np.random.seed(seed)

  header = [
    'deliverer_id',
    'delivery_zone',
    'monthly_app_usage',
    'subscription_type',
    'paid_price',
    'customer_size',
    'menu',
    'delay_time'
  ]
  rows = [header]

  with open(filename, 'w') as output_file:
      writer = csv.writer(output_file)

      for _ in range(amount):
        rows.append([
          np.random.choice(range(100), 1)[0],
          np.random.choice(['I', 'II', 'III', 'IV', 'V', 'VI','VII', 'VIII']),
          np.random.poisson(15),
          np.random.choice(['Free','Prepaid','Monthly','Trimestral', 'Semestral', 'Yearly'], 1,[.30, .20, 10,.15, .20, .05])[0],
          np.random.normal(25.45, 10),
          np.random.poisson(2) + 1,
          np.random.choice(['Asian', 'Indian', 'Italian','Japanese','French', 'Mexican'],1)[0],
          np.random.normal(10,3.2)
        ])

      writer.writerows(rows)
