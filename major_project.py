# Import necessary libraries
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Create dataset
dataset = []
row0 = {
    'step': 1,
    'type': 'PAYMENT',
    'amount': 9839.64,
    'nameOrig': 'C1231006815',
    'oldbalanceOrig': 170136.0,
    'newbalanceOrig': 160296.36,
    'nameDest': 'M1979787155',
    'oldbalanceDest': 0.0,
    'newbalanceDest': 0.0,
    'isFraud': 0,
    'isFlaggedFraud': 0
}

row1 = {
    'step': 1,
    'type': 'PAYMENT',
    'amount': 1864.28,
    'nameOrig': 'C1666544295',
    'oldbalanceOrig': 21249.0,
    'newbalanceOrig': 19384.72,
    'nameDest': 'M2044282225',
    'oldbalanceDest': 0.0,
    'newbalanceDest': 0.0,
    'isFraud': 0,
    'isFlaggedFraud': 0
}

row2 = {
    'step': 1,
    'type': 'TRANSFER',
    'amount': 181.0,
    'nameOrig': 'C1305486145',
    'oldbalanceOrig': 181.0,
    'newbalanceOrig': 0.0,
    'nameDest': 'C553264065',
    'oldbalanceDest': 0.0,
    'newbalanceDest': 0.0,
    'isFraud': 1,
    'isFlaggedFraud': 0
}

row3 = {
    'step': 1,
    'type': 'CASH_OUT',
    'amount': 181.0,
    'nameOrig': 'C840083671',
    'oldbalanceOrig': 181.0,
    'newbalanceOrig': 0.0,
    'nameDest': 'C38997010',
    'oldbalanceDest': 21182.0,
    'newbalanceDest': 0.0,
    'isFraud': 1,
    'isFlaggedFraud': 0
}

row4 = {
    'step': 1,
    'type': 'PAYMENT',
    'amount': 11668.14,
    'nameOrig': 'C2048537720',
    'oldbalanceOrig': 41554.0,
    'newbalanceOrig': 29885.86,
    'nameDest': 'M1230701703',
    'oldbalanceDest': 0.0,
    'newbalanceDest': 0.0,
    'isFraud': 0,
    'isFlaggedFraud': 0
}

dataset.append(row0)
dataset.append(row1)
dataset.append(row2)
dataset.append(row3)
dataset.append(row4)

# Create DataFrame
df = pd.DataFrame(dataset)
df.info()

# Encode 'type' column
type_dict = {"PAYMENT": 0, "CASH_OUT": 1, "TRANSFER": 2}
df['type'] = df['type'].map(type_dict)

# Define features and target
X = df.drop(columns=['nameOrig', 'nameDest', 'isFraud', 'isFlaggedFraud'])
y = df['isFraud']

# Instantiate and fit the Decision Tree Classifier
model = DecisionTreeClassifier()
model.fit(X, y)

# Function to take user input and predict fraud
def predict_fraud():
    # Take user input
    step = int(input("Enter step: "))
    nameOrig = input("Enter sender's account id: ")
    nameDest = input("Enter receiver's account id: ")
    type_input = input("Enter type of transaction (PAYMENT, CASH_OUT, TRANSFER): ")
    amount = float(input("Enter transaction amount: "))
    oldbalanceOrig = float(input("Enter old balance of sender's account: "))
    newbalanceOrig = float(input("Enter new balance of sender's account: "))
    oldbalanceDest = float(input("Enter old balance of receiver's account: "))
    newbalanceDest = float(input("Enter new balance of receiver's account: "))
    
    # Convert 'type' input into its corresponding numeral
    type_encoded = type_dict.get(type_input, -1)
    
    # Create input DataFrame
    input_data = pd.DataFrame({
        'step': [step],
        'type': [type_encoded],
        'amount': [amount],
        'oldbalanceOrig': [oldbalanceOrig],
        'newbalanceOrig': [newbalanceOrig],
        'oldbalanceDest': [oldbalanceDest],
        'newbalanceDest': [newbalanceDest]
    })
    
    # Predict and display the result
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        print("The transaction is predicted to be fraudulent.")
    else:
        print("The transaction is predicted to be not fraudulent.")

# Function call
predict_fraud()
