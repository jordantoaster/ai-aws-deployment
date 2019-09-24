import pickle
import joblib

# with open('periscope_aws_deployment/models/model.pkl', 'rb') as pickle_file:
#     model = pickle.load(pickle_file)

#     print(model)

model = joblib.load('periscope_aws_deployment/models/model.joblib')

print(model)