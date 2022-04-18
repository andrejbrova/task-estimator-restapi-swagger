from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix


# Gaussian model, doesn't give good results :(
model = GaussianNB()
fitted_model = model.fit(train_dataframe, train_target_variable)
score = fitted_model.score(test_dataframe, test_target_variable)
print("Score:", score)
#expected = test_dataframe
#predicted = fitted_model.predict(train_dataframe)
#print(metrics.classification_report(expected, predicted))
#print(metrics.confusion_matrix(expected, predicted))
predicted = fitted_model.predict(test_dataframe)
predictedProbability = fitted_model.predict_proba(test_dataframe)
print(predicted)
print(predictedProbability)


# Bernoulli model
BernNB = BernoulliNB(binarize=True)
fitted_BernNB = BernNB.fit(train_dataframe, train_target_variable)
print(fitted_BernNB)
y_expect = test_target_variable
y_bern_pred = fitted_BernNB.predict(test_dataframe)
print(y_bern_pred)
print(accuracy_score(y_expect, y_bern_pred))
bern_conf_mat = confusion_matrix(y_expect, y_bern_pred)
print(bern_conf_mat)


# Multinominal model
MultiNB = MultinomialNB()
fitted_MultiNB = MultiNB.fit(train_dataframe, train_target_variable)
print(fitted_MultiNB)
y_multi_pred = fitted_MultiNB.predict(test_dataframe)
print(y_multi_pred)
print(accuracy_score(y_expect, y_multi_pred))
multi_conf_mat = confusion_matrix(y_expect, y_multi_pred)
print(multi_conf_mat)
