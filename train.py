from sklearn import datasets
from sklearn.ensemble import GradientBoostingClassifier
import joblib
import pickle

# import data
iris = datasets.load_iris()
X = iris.data[:, :2]  # only take the first two features.
Y = iris.target

# init model
clf = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=2, random_state=0)

# fit model
clf.fit(X, Y)

# save model
joblib.dump(clf, 'periscope_aws_deployment/models/model.pkl')