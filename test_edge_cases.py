# import pickle

# # Define edge case input (30 features in the same order as training data)
# edge_case = [[17.99, 10.38, 122.8, 1001, 0.1184, 0.2776, 0.3001, 0.1471, 0.2419, 0.07871,
#               0.9053, 1.011, 8.589, 153.4, 0.006399, 0.04904, 0.05373, 0.01587, 0.03003, 0.006193,
#               25.38, 17.33, 184.6, 2019, 0.1622, 0.6656, 0.7119, 0.2654, 0.4601, 0.1189]]

# # Load the model and scaler
# with open('model/model.pkl', 'rb') as model_file:
#     model = pickle.load(model_file)
# with open('model/scaler.pkl', 'rb') as scaler_file:
#     scaler = pickle.load(scaler_file)

# # Preprocess edge case input
# edge_case_scaled = scaler.transform(edge_case)

# # Predict the label for the edge case
# edge_case_prediction = model.predict(edge_case_scaled)
# print(f"Edge Case Input: {edge_case}")
# print(f"Predicted Label: {edge_case_prediction}")
import pickle

# Define edge case input (30 features in the same order as training data)
edge_case = [[17.99, 10.38, 122.8, 1001, 0.1184, 0.2776, 0.3001, 0.1471, 0.2419, 0.07871,
              0.9053, 1.011, 8.589, 153.4, 0.006399, 0.04904, 0.05373, 0.01587, 0.03003, 0.006193,
              25.38, 17.33, 184.6, 2019, 0.1622, 0.6656, 0.7119, 0.2654, 0.4601, 0.1189]]

# Load the model and scaler
with open('model/model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)
with open('model/scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# Preprocess edge case input
edge_case_scaled = scaler.transform(edge_case)

# Predict the label for the edge case
edge_case_prediction = model.predict(edge_case_scaled)
print(f"Edge Case Input: {edge_case}")
print(f"Predicted Label: {edge_case_prediction}")
