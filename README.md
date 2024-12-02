# Breast Cancer Diagnosis Model

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/cancer-main.git
   cd cancer-main
   ```

2. **Create a virtual environment** (optional, recommended):
   ```bash
   conda create --name breast-cancer-diagnosis python=3.9
   conda activate breast-cancer-diagnosis
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Download the dataset** (if not already available):
   - Make sure to download the breast cancer dataset and place it in the appropriate folder.

## Running the Code

1. **Train the model** (if you haven't trained the model yet):
   ```bash
   python train_model.py
   ```

2. **Test the model** with the test data:
   ```bash
   python test_model.py
   ```

3. **Test the model with edge cases**:
   ```bash
   python test_edge_cases.py
   ```

## Files in the Project

- **train_model.py**: Script to train the model using the breast cancer dataset.
- **test_model.py**: Script to test the model on unseen test data.
- **test_edge_cases.py**: Script to test the model with edge case inputs.

## Model Performance

- After running `test_model.py`, you'll see the predictions and ground truth values printed on the console, indicating how well the model performs.
  
  Example output:
  ```bash
  Predictions: [1 0]
  Ground Truth: [0, 1]
  ```

- After running `test_edge_cases.py`, the edge case predictions will be shown. Example:
  ```bash
  Edge Case Input: [[17.99, 10.38, 122.8, 1001, 0.1184, 0.2776, 0.3001, 0.1471, 0.2419, 0.07871, 0.9053, 1.011, 8.589, 153.4, 0.006399, 0.04904, 0.05373, 0.01587, 0.03003, 0.006193, 25.38, 17.33, 184.6, 2019, 0.1622, 0.6656, 0.7119, 0.2654, 0.4601, 0.1189]]
  Predicted Label: [1]
  ```

## Notes
- Make sure the data file is placed correctly and the paths in the code are set properly.
- If you encounter any errors related to feature names or scaling, please ensure you pass the correct input format and column names to the model.
```
