from sklearn import datasets
from sklearn.ensemble import GradientBoostingClassifier
import joblib

# import data
iris = datasets.load_iris()
X = iris.data[:, :2]  # only take the first two features.
Y = iris.target

# init model
clf = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=2, random_state=0)

# fit model
clf.fit(X, Y)

# save model
joblib.dump(clf, 'models/model.joblib')