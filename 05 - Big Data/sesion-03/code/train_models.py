# train_models.py - entrenar modelos
import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.naive_bayes import BernoulliNB
from preproc_data import preproc_data

df_train = pd.read_csv('train_delivery_data.csv', header=None)
df_train.columns = ['deliverer_id', 'delivery_zone', 'subscription_type', 'monthly_app_usage','paid_price', 'customers_size', 'menu', 'delay_time']

df_train['delay_time'] = np.where(
    df_train['delay_time'] > df_train['delay_time'].mean(), 1, 0)

df_train = preproc_data(df_train)

y = df_train.pop('delay_time')

X_train, X_test, y_train, y_test = train_test_split(
    df_train, y, test_size=.33, random_state=11238)

logreg = LogisticRegression().fit(X_train, y_train)
rf = RandomForestClassifier().fit(X_train, y_train)
nb = BernoulliNB().fit(X_train, y_train)
tree = DecisionTreeClassifier().fit(X_train, y_train)
gboost = GradientBoostingClassifier().fit(X_train, y_train)

print("Logistic Regression")
print(classification_report(y_test, logreg.predict(X_test)))
print("Random Forest")
print(classification_report(y_test, rf.predict(X_test)))
print("Naive Bayes")
print(classification_report(y_test, nb.predict(X_test)))
print("Decision Tree")
print(classification_report(y_test, tree.predict(X_test)))
print("Gradient Boosting")
print(classification_report(y_test, gboost.predict(X_test)))

pickle.dump(tree, open('bestmodel.pkl', 'wb'))
