
# Further research: https://www.datacamp.com/tutorial/understanding-logistic-regression-python
# https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html


from statsmodels.stats.proportion import proportions_ztest
import scipy.stats as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.metrics import classification_report


# df = pd.read_csv('../data/airline_passenger_satisfaction.csv')
df = pd.read_csv('data/airline_passenger_satisfaction.csv')

sample_size = 1000

df_sample = df.sample(n=sample_size)


# X = df_sample[[col for col in df_sample.columns if col not in ['ID', 'Satisfaction']]] # Features
X = df_sample[['Age', 'Flight Distance', 'Departure Delay']] # Features

y = df_sample['Satisfaction'] # Target variable

# split X and y into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=16)


# instantiate the model (using the default parameters)
logreg = LogisticRegression(random_state=16)


# fit the model with data
logreg.fit(X_train, y_train)


y_pred = logreg.predict(X_test)

cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
cnf_matrix


target_names = ['Satisfied', 'Neutral or Dissatisfied']
print(classification_report(y_test, y_pred, target_names=target_names))


y_pred_proba = logreg.predict_proba(X_test)[::, 1]
fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba)
auc = metrics.roc_auc_score(y_test, y_pred_proba)
plt.plot(fpr,tpr,label="data 1, auc="+str(auc))
plt.legend(loc=4)
plt.show()


