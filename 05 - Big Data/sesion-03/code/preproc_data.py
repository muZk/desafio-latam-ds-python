import pandas as pd

def preproc_data(x):

  zone_binarized = pd.get_dummies(x['delivery_zone'], drop_first=True)

  subscription_binarized = pd.get_dummies(x['subscription_type'], drop_first=True)

  menu_binarized = pd.get_dummies(x['menu'], drop_first=True)

  x = x.drop(columns=['delivery_zone', 'subscription_type', 'menu'])

  x = pd.concat(
      [x, zone_binarized, subscription_binarized, menu_binarized], axis=1)

  return x
