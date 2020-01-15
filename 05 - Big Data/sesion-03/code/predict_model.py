#predict_model.py
import pandas as pd
import pickle
from preproc_data import preproc_data

df_test = pd.read_csv('test_delivery_data.csv')
df_test.columns = ['deliverer_id', 'delivery_zone', 'subscription_type','monthly_app_usage','paid_price', 'customers_size','menu']
df_test_process = preproc_data(df_test)

tree = pickle.load(open('bestmodel.pkl', 'rb'))
df_test['predict'] = tree.predict(df_test_process)

print("Predict 1")
print(df_test.groupby('delivery_zone')['predict'].mean().sort_values())
print("Predict 2")
print(df_test.groupby('deliverer_id')['predict'].mean().sort_values())
print("Predict 3")
print(df_test.groupby('menu')['predict'].mean().sort_values())
print("Predict 4")
print(df_test.groupby('subscription_type')['predict'].mean().sort_values())
